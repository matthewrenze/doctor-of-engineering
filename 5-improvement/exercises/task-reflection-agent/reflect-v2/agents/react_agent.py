import re
from common.console import debug
from collections import deque
from environments.state import State

class ReactAgent:
    def __init__(self, model, system_prompt: str, reflect_prompt: str):
        self.model = model
        self.system_prompt = system_prompt
        self.reflect_prompt = reflect_prompt
        self.messages = []
        self.reflections = ""
        self.context = deque(maxlen=5)
        self.step_idx = 0
        self.task = ""

    def set_reflection(self, reflections: str):
        self.reflections = reflections

    def reset(self, task: str):
        self.model.reset()
        self.task = task
        system_prompt = self.system_prompt + f"\n# Task\n{self.task}\n"
        if self.reflections:
            system_prompt += f"\n# Reflections\n{self.reflections}\n"
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.context.clear()
        self.step_idx = 0

    def act(self, state: State) -> tuple[str, str]:

        # Add user prompt to messages
        prompt_message = self.get_user_prompt(state)
        self.messages.append(prompt_message)

        # Build the context with summaries and past state-actions
        current_messages: list[dict] = []

        # Add the system prompt
        current_messages.append(self.messages[0])

        # Add the state-action pairs from the queue
        for pair in self.context:
            current_messages.append(pair["state"])
            current_messages.append(pair["action"])

        # Add the latest user prompt
        current_messages.append(prompt_message)

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
        self.context.append(state_action_pair)

        self.step_idx += 1
        return thought, action

    def reflect(self, state: State):

        # Add user prompt to previous messages
        prompt_message = self.get_user_prompt(state)
        self.messages.append(prompt_message)

        # Copy the previous messages
        previous_messages = self.messages.copy()
        previous_messages.pop(0)

        # Add the system prompt to current messages
        current_messages: list[dict] = []
        review_prompt = self.reflect_prompt + f"\n# Task\n{self.task}\n"
        current_messages.append({"role": "system", "content": review_prompt.strip()})

        # Add the previous messages as a single user message
        user_content = ""
        for msg in previous_messages:
            role = msg["role"]
            role = "Agent" if role == "assistant" else "Environment"
            content = msg["content"]
            user_content += f"# {role}\n{content}\n\n"
        user_message = {"role": "user", "content": user_content}
        current_messages.append(user_message)

        # Get the response from the model
        response = self.model.get_response(current_messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        # Get the success from the response
        success_match = re.search(r"Success: (.*?)(?=\nAnalysis:)", response, re.DOTALL)
        success = success_match.group(1).strip() if success_match else ""

        # Get the analysis from the response
        analysis_match = re.search(r"Analysis: (.*?)(?=\nReason:)", response, re.DOTALL)
        analysis = analysis_match.group(1).strip() if analysis_match else ""

        # Get the reason from the response
        reason_match = re.search(r"Reason: (.*?)(?=\nAdvice:)", response, re.DOTALL)
        reason = reason_match.group(1).strip() if reason_match else ""

        # Get the advice from the response
        advice_match = re.search(r"Advice: (.*)", response, re.DOTALL)
        advice = advice_match.group(1).strip() if advice_match else ""

        return success, analysis, reason, advice


    def get_user_prompt(self, state: State) -> dict[str, str]:
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
        return prompt_message


# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)