import re
from common.console import debug
from collections import deque
from environments.state import State

class ReactAgent:
    def __init__(self, model, prompt: str, version: int):
        self.model = model
        self.prompt = prompt
        self.messages = []
        self.state_action_queue = deque(maxlen=version)
        self.step_idx = 0
        self.k_full_steps = version

    def reset(self, task: str):
        self.model.reset()
        system_prompt = self.prompt + f"Task: {task}\n"
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.state_action_queue.clear()
        self.step_idx = 0

    def act(self, state: State) -> tuple[str, str]:

        # Prepare the user prompt
        content = f"State:\n"
        content += f"  Step: {self.step_idx + 0}\n"
        if state.feedback != "":
            content += f"  Feedback: {state.feedback.strip()}\n"
        content += "" \
            + f"  Location: {state.location.strip()}\n" \
            + f"  Description: {state.description.strip()}\n" \
            + f"  Inventory: {state.inventory.strip()}\n" \
            + f"  Score: {state.score.strip()}\n"
        prompt_message = {"role": "user", "content": content}
        self.messages.append(prompt_message)

        # Build the context with summaries and past state-actions
        current_messages: list[dict] = []

        # Add the system prompt
        current_messages.append(self.messages[0])

        # Add the state-action pairs from the queue
        for pair in self.state_action_queue:
            current_messages.append(pair["state"])
            current_messages.append(pair["action"])

        # Add the latest user prompt
        current_messages.append(prompt_message)

        # Debug: print message counts
        debug(f"Total messages: {len(self.messages)}, State-Actions: {len(self.state_action_queue)}, Current messages: {len(current_messages)}")

        # # DEBUG: print the first 80 characters of the current messages
        # debug_messages = ""
        # for message in current_messages:
        #     role = message['role']
        #     content = message['content']
        #     content = content.replace("\n", " ")
        #     debug_messages += f" - {role}: {content}\n"
        # debug("Messages:\n" + debug_messages)

        # Get the response from the model
        response = self.model.get_response(current_messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        # Get the thought from the response
        thought_match = re.search(r"Thought: (.*?)(?=\nAction:)", response, re.DOTALL)
        thought = thought_match.group(1).strip() if thought_match else ""

        # Get the action from the response
        action_match = re.search(r"Action: (.*)", response, re.DOTALL)
        action = action_match.group(1).strip() if action_match else ""

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        # Add the state-action pair to the queue
        state_action_pair = {
            "state": prompt_message,
            "action": response_message}
        self.state_action_queue.append(state_action_pair)

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