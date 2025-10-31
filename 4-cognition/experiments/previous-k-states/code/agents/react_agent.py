import re
from environments.state import State
from common.console import debug


class ReactAgent:
    def __init__(self, model, prompt: str, version: int):
        self.model = model
        self.prompt = prompt
        self.messages = []
        self.step_idx = 0
        self.is_observing = (version > 0)
        self.k_previous_states = version

    def reset(self, task: str):
        self.model.reset()
        system_prompt = self.prompt + f"Task: {task}\n"
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.step_idx = 0

    def act(self, state: State) -> tuple[str, str, str]:

        # Prepare the user prompt
        content = f"State:\n"

        if state.feedback != "":
            content += f"  Feedback: {state.feedback.strip()}\n"

        content += "" \
            + f"  Feedback: {state.feedback.strip()}\n" \
            + f"  Location: {state.location.strip()}\n" \
            + f"  Description: {state.description.strip()}\n" \
            + f"  Inventory: {state.inventory.strip()}\n" \
            + f"  Score: {state.score.strip()}\n"
        prompt_message = {"role": "user", "content": content}
        self.messages.append(prompt_message)

        # Filter out all but the last k states (user messages)
        filtered_messages = self.messages.copy()
        if self.is_observing:
            reversed_messages = reversed(list(enumerate(filtered_messages)))
            user_message_indices = [i for i, msg in reversed_messages if msg["role"] == "user"]
            indices_to_remove = user_message_indices[self.k_previous_states:]
            for index in sorted(indices_to_remove, reverse=True):
                del filtered_messages[index]

        # DEBUG: Report the number of filtered messages by role
        counts = {"system": 0, "user": 0, "assistant": 0}
        for message in filtered_messages:
            role = message["role"]
            counts[role] = counts.get(role, 0) + 1
        debug(f"Messages: system={counts['system']}, user={counts['user']}, model={counts['assistant']}")

        # Get the response from the model
        response = self.model.get_response(filtered_messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        # Get the observation from the response
        observation_match = re.search(r"Observation: (.*?)(?=\nThought:)", response, re.DOTALL)
        observation = observation_match.group(1).strip() if observation_match else ""

        # Get the thought from the response
        thought_match = re.search(r"Thought: (.*?)(?=\nAction:)", response, re.DOTALL)
        thought = thought_match.group(1).strip() if thought_match else ""

        # Get the action from the response
        action_match = re.search(r"Action: (.*)", response, re.DOTALL)
        action = action_match.group(1).strip() if action_match else ""

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        self.step_idx += 1
        return observation, thought, action


# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)