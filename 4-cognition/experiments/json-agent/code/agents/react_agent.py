import re
import json
from typing import Any, Dict, Tuple, Union

class ReactAgent:
    def __init__(self, model, prompt):
        self.model = model
        self.prompt = prompt
        self.messages = []
        self.step_idx = 0

    def reset(self):
        self.model.reset()
        system_prompt = self.prompt
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.step_idx = 0

    def act(self, state: dict) -> tuple[str, str]:
        content = json.dumps(state, ensure_ascii=False)
        prompt_message = {"role": "user", "content": content}
        self.messages.append(prompt_message)

        # Get the response from the model
        response = self.model.get_response(self.messages)
        response = response.strip()
        result = json.loads(response)

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        self.step_idx += 1
        return result


# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)