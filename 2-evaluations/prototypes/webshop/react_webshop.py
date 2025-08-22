# NOTE: Original source code from: https://github.com/ysymyth/ReAct

import os
import sys
import re
from openai import AzureOpenAI
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

system_prompt = """
You are an intelligent agent that completes multi-step tasks.
You will complete the task through a series of steps.
Each step will be subdivided into the following sub-steps:
 - Thought - a step-by-step reasoning process that leads to an Action.
 - Action - a command that you will execute in your environment.
 - State - the result of executing the Action in the environment.
You will use feedback from the State to refine your Thought and Action in subsequent steps.
You must provide only one Thought and one Action in your response.
Action can be one of the following types:
 - click(link) - clicks the specified link which is surrounded in [].
 - search(query) - searches for the specified query terms.
You do not have access to any other tools, actions, or commands.
Do not include any other text in your response.
You have ten steps to complete each task.
Be concise.

# Examples

Instruction:  
i would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars 
[Search]  

Thought: I should search for a 3 ounce bright citrus deodorant for sensitive skin.
Action: search[3 ounce bright citrus deodorant sensitive skin]
State: 
[Back to Search] 
Page 1 (Total results: 50) 
[Next >] 
[B078GWRC1J] 
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B078GTKVXY] 
Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
$10.99 
[B08KBVJ4XN] 
Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men, Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar & Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack) 
$15.95  

Thought: B078GWRC1J and B078GTKVXY are bright citrus deodorant less then 50 dollars. I can check B078GWRC1J first.
Action: click[B078GWRC1J]
State: 
[Back to Search] 
[< Prev] 
scent [assorted scents][bright citrus][calming lavender][ginger fresh][simply non-scents]
size [travel set (4-pack)][3 ounce (pack of 1)][3-ounce (2-pack)]
Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce 
Price: $10.99 
Rating: N.A. 
[Description] 
[Features] 
[Reviews] 
[Buy Now]  

Thought: For 3 ounce bottle of bright citrus deodorant for sensitive skin, the item has options 'bright citrus' and '3 ounce (pack of 1)' and seems good to buy.
Action: click[bright citrus]
State: You have clicked bright citrus. 

Thought: I should select the 3 ounce (pack of 1) option.
Action: click[3 ounce (pack of 1)]
State: You have clicked 3 ounce (pack of 1). 

Thought: Now I can buy the item.
Action: click[Buy Now]
"""

api_key = os.environ['AZURE_OPENAI_KEY']
api_url = os.environ['AZURE_OPENAI_URL']
api_version = "2025-01-01-preview"
model_name = "gpt-4.1-mini"
max_steps = 15

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

def llm(prompt, stop=["\n"]):
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.0,
        top_p=1.0,
        frequency_penalty=0.0,
        stop=stop)

    return response.choices[0].message.content


# # DEBUG: Test the LLM with a simple prompt
# response = llm("Hello, are you there?", stop=["\n"])
# print(response)

WEBSHOP_URL = "http://127.0.0.1:3000"
ACTION_TO_TEMPLATE = {
    'Description': 'description_page.html',
    'Features': 'features_page.html',
    'Reviews': 'review_page.html',
    'Attributes': 'attributes_page.html',
}


def clean_str(p):
    return p.encode().decode("unicode-escape").encode("latin1").decode("utf-8")


def tag_visible(element):
    ignore = {'style', 'script', 'head', 'title', 'meta', '[document]'}
    return element.parent.name not in ignore and not isinstance(element, Comment)


def get_webshop_text(session_id, page_type, query_string='', page_num=1, asin='', options={}, subpage='', **kwargs):
    if page_type == 'init':
        url = f'{WEBSHOP_URL}/{session_id}'
    elif page_type == 'search':
        url = f'{WEBSHOP_URL}/search_results/{session_id}/{query_string}/{page_num}'
    elif page_type == 'item':
        url = f'{WEBSHOP_URL}/item_page/{session_id}/{asin}/{query_string}/{page_num}/{options}'
    elif page_type == 'item_sub':
        url = f'{WEBSHOP_URL}/item_sub_page/{session_id}/{asin}/{query_string}/{page_num}/{subpage}/{options}'
    elif page_type == 'end':
        url = f'{WEBSHOP_URL}/done/{session_id}/{asin}/{options}'

    html = requests.get(url).text
    html_obj = BeautifulSoup(html, 'html.parser')
    texts = html_obj.findAll(text=True)
    visible_texts = list(filter(tag_visible, texts))
    # visible_texts = [str(text).strip().strip('\\n') for text in visible_texts]
    # if page_type == 'end': import pdb; pdb.set_trace()
    if False:
        # For `simple` mode, return just [SEP] separators
        return ' [SEP] '.join(t.strip() for t in visible_texts if t != '\n')
    else:
        # Otherwise, return an observation with tags mapped to specific, unique separators
        observation = ''
        option_type = ''
        options = {}
        asins = []
        cnt = 0
        prod_cnt = 0
        just_prod = 0
        for t in visible_texts:
            if t == '\n':
                continue

            if t.replace('\n', '').replace('\\n', '').replace(' ', '') == '':
                continue

            # if t.startswith('Instruction:') and page_type != 'init': continue
            # print(t.parent.name, t)
            if t.parent.name == 'button':  # button
                processed_t = f'\n[{t}] '
            elif t.parent.name == 'label':  # options
                if f"'{t}'" in url:
                    processed_t = f'[[{t}]]'
                    # observation = f'You have clicked {t}.\n' + observation
                else:
                    processed_t = f'[{t}]'
                options[str(t)] = option_type
                # options[option_type] = options.get(option_type, []) + [str(t)]
            elif t.parent.get('class') == ["product-link"]:  # product asins
                processed_t = f'\n[{t}] '
                if prod_cnt >= 3:
                    processed_t = ''
                prod_cnt += 1
                asins.append(str(t))
                just_prod = 0
            else:  # regular, unclickable text
                processed_t = '\n' + str(t) + ' '
                if cnt < 2 and page_type != 'init': processed_t = ''
                if just_prod <= 2 and prod_cnt >= 4: processed_t = ''
                option_type = str(t)
                cnt += 1
            just_prod += 1
            observation += processed_t
        info = {}
        if options:
            info['option_types'] = options
        if asins:
            info['asins'] = asins
        if 'Your score (min 0.0, max 1.0)' in visible_texts:
            idx = visible_texts.index('Your score (min 0.0, max 1.0)')
            info['reward'] = float(visible_texts[idx + 1])
            observation = 'Your score (min 0.0, max 1.0): ' + (visible_texts[idx + 1])
        return clean_str(observation), info


class WebshopEnv:
    def __init__(self):
        self.sessions = {}

    def step(self, session_id, action):
        done = False
        state_ = None
        if action == 'reset()':
            self.sessions[session_id] = {
                'session_id': session_id,
                'page_type': 'init'}
        elif action.startswith('search('):
            # assert self.sessions[session]['page_type'] == 'init'
            query = action[7:-1]
            self.sessions[session_id] = {
                'session_id': session_id,
                'page_type': 'search',
                'query_string': query,
                'page_num': 1}
        elif action.startswith('click('):
            button = action[6:-1]
            if button == 'Buy Now':
                assert self.sessions[session_id]['page_type'] == 'item'
                self.sessions[session_id]['page_type'] = 'end'
                done = True
            elif button == 'Back to Search':
                assert self.sessions[session_id]['page_type'] in ['search', 'item_sub', 'item']
                self.sessions[session_id] = {'session_id': session_id, 'page_type': 'init'}
            elif button == 'Next >':
                assert False  # ad hoc page limitation
                assert self.sessions[session_id]['page_type'] == 'search'
                self.sessions[session_id]['page_num'] += 1
            elif button == '< Prev':
                assert self.sessions[session_id]['page_type'] in ['search', 'item_sub', 'item']
                if self.sessions[session_id]['page_type'] == 'search':
                    assert False
                    self.sessions[session_id]['page_num'] -= 1
                elif self.sessions[session_id]['page_type'] == 'item_sub':
                    self.sessions[session_id]['page_type'] = 'item'
                elif self.sessions[session_id]['page_type'] == 'item':
                    self.sessions[session_id]['page_type'] = 'search'
                    self.sessions[session_id]['options'] = {}
            elif button in ACTION_TO_TEMPLATE:
                assert self.sessions[session_id]['page_type'] == 'item'
                self.sessions[session_id]['page_type'] = 'item_sub'
                self.sessions[session_id]['subpage'] = button
            else:
                if self.sessions[session_id]['page_type'] == 'search':
                    assert button in self.sessions[session_id].get('asins', [])  # must be asins
                    self.sessions[session_id]['page_type'] = 'item'
                    self.sessions[session_id]['asin'] = button
                elif self.sessions[session_id]['page_type'] == 'item':
                    assert 'option_types' in self.sessions[session_id]
                    assert button in self.sessions[session_id]['option_types'], (button, self.sessions[session_id][
                        'option_types'])  # must be options
                    option_type = self.sessions[session_id]['option_types'][button]
                    if not 'options' in self.sessions[session_id]:
                        self.sessions[session_id]['options'] = {}
                    self.sessions[session_id]['options'][option_type] = button
                    state_ = f'You have clicked {button}.'
        else:
            state = "Invalid action! Action must be one of the following: search(query), click(link)."
            return state, 0.0, False

        state, info = get_webshop_text(**self.sessions[session_id])
        if state_:
            state = state_
        self.sessions[session_id].update(info)
        reward = info.get('reward', 0.0)
        return state, reward, done


env = WebshopEnv()

def run_episode(idx, prompt):
    is_done = False
    reward = 0.0
    response = "Action: reset()"
    action = 'reset()'
    init_prompt = prompt
    state, reward, is_done = env.reset(idx)
    prompt += f'State: {state}\n'

    for i in range(max_steps):

        response = llm(init_prompt + prompt, stop=['\n'])
        prompt += f' {response}\nState: {state}\n'
        print(f'{response}\n')

        action = re.sub(r'Action:\s*', '', response, flags=re.IGNORECASE)
        action = action.strip()

        state, reward, is_done = env.step(idx, action)

        if is_done:
            return reward

    return 0.0


def run_episodes(prompt, n=50):
    results = []
    count = 0
    for i in range(n):
        print('-----------------')
        print(i)
        try:
            result = run_episode(f'fixed_{i}', prompt)
        except AssertionError:
            result = 0
            count += 1
        results.append(result)
        if (i + 1) % 1 == 0:
            result = sum(results) / len(results)
            success_rate = len([_ for _ in results if _ == 1]) / len(results)
            failure_rate = count / len(results)
            print(i + 1, result, success_rate, failure_rate)
            print('-------------')
    result, success_rate, failure_rate = sum(results) / len(results), len([_ for _ in results if _ == 1]) / n, count / n
    print(result, success_rate, failure_rate)
    return results


final_results = run_episodes(system_prompt, 500)