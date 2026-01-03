from states.global_state import GlobalState

class ReasonerAgent:
    def __init__(self, model, system_prompt: str):
        self.model = model
        self.system_prompt = system_prompt
        self.messages = []

    def reset(self):
        self.model.reset()

    def execute(self, state: GlobalState) -> str:

        # Clear the previous messages
        self.messages = []

        # Add the system prompt
        system_message = {"role": "system", "content": self.system_prompt.strip()}
        self.messages.append(system_message)

        # Add the task to the user prompt
        user_content = f"Task: {state.task}\n"

        # Get the previous five steps (plus current step) from the history
        previous_steps = state.step_history[-6:]

        for index, step in enumerate(previous_steps):
            env_state = step.env_state
            agent_state = step.agent_state
            user_content += f"# Step: {step.step_id}\n"

            # Append the environment state
            user_content += f"Env State:\n" \
                + f"  Feedback: {step.env_state.feedback}\n" \
                + f"  Location: {step.env_state.location}\n" \
                + f"  Description: {step.env_state.description}\n" \
                + f"  Inventory: {step.env_state.inventory}\n" \
                + f"  Score: {env_state.score} of {env_state.max_score}\n" \
                + "\n"

            # For the last step, don't include the observation
            if index == len(previous_steps) - 1:
                continue

            # Append the agent state
            user_content += f"Agent State:\n" \
                + f"  Thought: {agent_state.thought}\n" \
                + f"  Action: {agent_state.action}\n" \
                + "\n"

        user_message = {"role": "user", "content": user_content}

        # Add the user prompt
        self.messages.append(user_message)

        # Get the response from the model
        response = self.model.get_response(self.messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        return response



# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)