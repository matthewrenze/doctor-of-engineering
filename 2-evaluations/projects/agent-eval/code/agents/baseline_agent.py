import re

class BaselineAgent:
    def __init__(self, model, prompt):
        self.model = model
        self.prompt = prompt
        self.messages = []
        self.step_idx = 0

    def reset(self, task):
        self.model.reset()
        system_prompt = self.prompt + f"\nTask: {task.strip()}"
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