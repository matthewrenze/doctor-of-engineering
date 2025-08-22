import re
import io
import base64
from PIL import Image
from typing import Union

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
 - list_files() - lists the files in the current workspace.
 - read_file_as_text(file_name) - reads the content of the specified file as text.
 - read_file_as_image(file_name) - reads the content of the specified file as an image.
 - calculate(expression) - evaluates the mathematical expression using the eval() function in Python.
 - finish(answer) - returns the final answer to the user and ends the task.
You do not have access to any other tools, actions, or commands.
Do not include any other text in your response.
You have ten steps to complete each task.
Be concise.

# Examples

Task: Answer the following question:
What is the sum of 2 and 2?
Thought: I need to calculate 2 + 2.
Action: calculate("2 + 2")
State: 4
Thought: The result is 4, so I can finish now.
Action: finish("4")
"""

class ReactAgent:
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

    def act(self, state: Union[str, bytes]) -> str:
        if isinstance(state, bytes):
            # The content is an image
            image = state.decode("utf-8")
            image_content = {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image}"},
            }
            content = [image_content]
        else:
            # The content is text
            content = state.strip()

        prompt_message = {"role": "user", "content": content}
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