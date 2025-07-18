import re

system_prompt = """
# Overview
You are an intelligent agent that completes multi-step tasks for a user.
You will complete the task through a series of steps.
Each step will be subdivided into the following sub-steps:
 - Thought - a step-by-step reasoning process that leads to an Action.
 - Action - a command that you will execute in your environment.
 - Observation - the result of executing the Action in the environment.
You will use feedback from the Observation to refine your Thought and Action in subsequent steps.
You must provide only one Thought and one Action in your response.
Do not include any other text in your response.
You have 50 steps to complete each task.
Be concise.

# Actions
The actions available to the actor are:
 - look - describe the current room
 - goal - print the goal of this game
 - inventory - print player's inventory
 - go <direction> - move the player north, east, south or west
 - examine <object> - examine something more closely
 - eat <object> - eat edible food
 - open <object> - open a door or a container
 - close <object> - close a door or a container
 - drop <object> - drop an object on the floor
 - take <object> - take an object that is on the floor
 - put <object> on <supporter> - place an object on a supporter
 - take <object> from <container> - take an object from a container
 - insert <object> into <container> - place an object into a container
 - lock <object> with <key> - lock a door or a container with a key
 - unlock <object> with <key> - unlock a door or a container with a key
 - cut <object> with <tool> - cut an object with a tool
 - chop <object> with <tool> - chop an object with a tool
 - slice <object> with <tool> - slice an object with a tool
 - dice <object> with <tool> - dice an object with a tool
 - cook <object> with <tool> - cook an object with a tool (e.g. stove, oven, grill)
 - prepare meal - prepare a meal from items in your inventory
 - quit - quit the game

# Format
Thought: <thought>
Action: <action_name> <args>

# Example
Task: Make a cup of coffee with the coffee can on the counter.
Observation: A cup, a coffee can, and a coffee maker on the counter.
Thought: I should take the coffee can from the counter.
Action: take coffee can from counter
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

    def act(self, state: str) -> str:

        # Create an observation
        state = state.strip()
        observation = f"Observation: {state}"
        print(observation)

        # Add the prompt to the messages
        prompt_message = {"role": "user", "content": observation}
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


# DEBUG:
if __name__ == "__main__":
    class TestModel:
        def get_response(self, prompt):
            return "Thought: This is a mock thought.\nAction: do something"
    model = TestModel()
    agent = ReactAgent(model)
    action = agent.act("Mock observation for testing.")
    print(agent.messages)
    print(action)