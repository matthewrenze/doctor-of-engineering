import re

system_prompt = """
You are an intelligent agent that completes multi-step tasks for a user.
You will complete the task through a series of steps.
Each step will be subdivided into the following sub-steps:
 - Thought - a step-by-step reasoning process that leads to an Action.
 - Action - a command that you will execute in your environment.
 - Observation - the result of executing the Action in the environment.
You will use feedback from the Observation to refine your Thought and Action in subsequent steps.
You must provide only one Thought and one Action in your response.
Action can be one of the following types:
 - finish(answer) - returns the final answer to the user and ends the task.
Do not include any other text in your response.
You have only 10 steps to complete each task.
Be concise.

Here are some example prompts and responses:

Task: Answer the following question.
Question: What is the sum of 2 and 2?
Thought: 2 + 2 = 4.
Action: finish(4)
"""

class BaselineAgent:
    def __init__(self, model):
        self.model = model
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.step_idx = 0

    def reset(self):
        self.model.reset()
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.step_idx = 0

    def act(self, obs: str) -> str:

        # Add the prompt to the messages
        obs = obs.strip()
        prompt_message = {"role": "user", "content": obs}
        self.messages.append(prompt_message)

        # Get the response from the model
        response = self.model.get_response(self.messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        # Get the action from the response
        action = re.search(r"Action: (.*)", response).group(1)

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        self.step_idx += 1
        print(response)
        return action


# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)