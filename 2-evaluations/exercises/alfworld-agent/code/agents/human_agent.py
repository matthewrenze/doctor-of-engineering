import re
import matplotlib.pyplot as plt

class HumanAgent:
    def __init__(self):
        pass

    def reset(self):
        pass

    def act(self, state: dict) -> str:
        state_text = state.get("text", "")
        print(f"State: {state_text}")

        state_image = state.get("image", None)
        if state_image is not None:
            plt.imshow(state_image)
            plt.axis("off")
            plt.show()

        action = input("> ")
        print(f"Action: {action}")
        return action


# DEBUG:
if __name__ == "__main__":
    agent = HumanAgent()
    state = "State: Your goal is to eat an apple."
    result = agent.select_action(state)
    print(result)