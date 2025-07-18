import re

class HumanAgent:
    def __init__(self):
        pass

    def reset(self):
        pass

    def act(self, state: str) -> str:
        action = input("> ")
        print(f"Action: {action}")
        return action


# DEBUG:
if __name__ == "__main__":
    agent = HumanAgent()
    state = "State: Your goal is to eat an apple."
    result = agent.select_action(state)
    print(result)