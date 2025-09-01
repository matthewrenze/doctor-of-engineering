import re

system_prompt_template = """
You are an intelligent agent that completes multi-step tasks.
You will complete the task through a series of steps.
Each step will be subdivided into the following sub-steps:
 - Action - a command that you will execute in your environment.
 - State - the result of executing the Action in the environment.
You will use feedback from the State to refine your Action in subsequent steps.
You must provide only one Action in your response.
Action can be one of the following types:
 - list_files() - lists the files in the current workspace.
 - read_file(file_name) - reads the content of the specified file as text.
 - calculate(expression) - evaluates the mathematical expression using the eval() function in Python.
 - finish(answer) - returns the final answer to the user and ends the task.
When answering questions provide only the final answer value or multiple-choice letter.
You do not have access to any other tools, actions, or commands.
Do not include any other text in your response.
You have {max_steps} steps to complete each task.
Be concise.

# Examples

Task: Answer the following question:
What is the sum of 2 and 2?
Action: calculate("2 + 2")
State: 4
Action: finish("4")
"""

class BaselineAgent:
    def __init__(self, model):
        self.model = model
        self.messages = []
        self.step_idx = 0

    def reset(self, task, max_steps):
        self.model.reset()
        system_prompt = system_prompt_template.format(max_steps=max_steps)
        system_prompt = system_prompt + f"\nTask: {task.strip()}"
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.step_idx = 0

    def act(self, state: str) -> tuple[str, str]:

        # Add the prompt to the messages
        state = state.strip()
        prompt_message = {"role": "user", "content": state}
        self.messages.append(prompt_message)

        # Get the response from the model
        response = self.model.get_response(self.messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        # Get the thought from the response
        thought = ""

        # Get the action from the response
        action_match = re.search(r"Action: (.*)", response)
        action = action_match.group(1).strip() if action_match else ""

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        self.step_idx += 1
        return thought, action


# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)