import re
from environments.state import State

class OracleAgent:
    def __init__(self, model, prompt: str):
        self.model = model
        self.prompt = prompt
        self.messages = []
        self.solution = []
        self.step_idx = 0

    def reset(self, task: str):
        self.model.reset()
        system_prompt = f"Task: {task}\n"
        system_message = {"role": "system", "content": system_prompt.strip()}
        self.messages = [system_message]
        self.step_idx = 0

    def set_solution(self, solution: str):
        self.solution = solution.split(", ")

    def act(self, state: State) -> tuple[str, str]:

        # Prepare the user prompt
        content = f"State:\n"
        if state.feedback != "":
            content += f"  Feedback: {state.feedback.strip()}\n"
        content += "" \
            + f"  Location: {state.location.strip()}\n" \
            + f"  Description: {state.description.strip()}\n" \
            + f"  Inventory: {state.inventory.strip()}\n" \
            + f"  Score: {state.score.strip()}\n"
        prompt_message = {"role": "user", "content": content}
        self.messages.append(prompt_message)

        # Get the thought
        thought = ""

        # Get the action from the solution
        action = self.solution[self.step_idx]

        # Create the simulated response
        response = f"Thought: \nAction: {action}"

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        self.step_idx += 1
        return thought, action


# # DEBUG:
if __name__ == "__main__":
    class TestModel:
        def reset(self):
            pass
    model = TestModel()
    agent = OracleAgent(model, "")
    task = "Do something"
    solution = "execute 1, execute 2, execute 3"
    state = State("task", "location", "description", "inventory", "score", "feedback")
    agent.reset(task)
    agent.set_solution(solution)
    print(agent.act(state))
    print(agent.act(state))
    print(agent.act(state))