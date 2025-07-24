import re
import io
import base64
from PIL import Image

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
You must go to a container to interact with objects in or on it.
You have 50 steps to complete each task.
Be concise.

# Actions
The actions available to the actor are:
- look - look around your current location
- inventory - check your current inventory
- go to <container> - move to a container
- open <container> - open a container
- close <container> - close a container
- take <object> from <container> - take an object from a container
- move <object> to <container> - place an object in or on a container
- examine <something> - examine a container or an object
- use <object> - use an object
- heat <object> with <container> - heat an object using a container
- clean <object> with <container> - clean an object using a container
- cool <object> with <container> - cool an object using a container
- slice <object> with <object> - slice an object using a sharp object
- help - provide a list of available actions
- quit - quit the task

# Format
Thought: <thought>
Action: <action_name> <args>

# Example
Task: Make a cup of coffee with the coffee can on the counter.
Observation: You are in a kitchen with a stove 1, a sink 1, and a counter 1.
Thought: I should go to counter 1.
Action: go to counter 1
Observation: A coffee machine 1, a coffee can 1, and coffee cup 1 are on the counter 1.
Thought: I should take the coffee can from the counter.
Action: take coffee can 1 from counter
...
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

    def act(self, state: dict) -> str:

        # Create the content for the prompt
        content = []

        # Add text observation
        state_text = state.get("text", "")
        state_text = state_text.strip()
        state_text = f"State: {state_text}"
        text_content = { "type": "text", "text": state_text }
        content.append(text_content)
        print(state_text)

        # Add image observation
        state_image = state.get("image", None)
        if state_image is not None:
            pil_image = Image.fromarray(state_image)
            buffer = io.BytesIO()
            pil_image.save(buffer, format="PNG")
            image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            image_content = {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
            }
            content.append(image_content)

        # Add the prompt to the messages
        prompt_message = {"role": "user", "content": content}
        self.messages.append(prompt_message)

        # Get the response from the model
        response = self.model.get_response(self.messages)
        response = response.replace("\n\n", "\n")
        response = response.strip()
        print(response)

        # Get the action from the response
        action = re.search(r"Action: (.*)", response).group(1)

        # Add the response to the messages
        response_message = {"role": "assistant", "content": response}
        self.messages.append(response_message)

        # Remove all images from messages if any exist
        # Note: We only want to send the latest image each time
        for message in self.messages:
            content = message.get("content")
            if isinstance(content, list):
                message["content"] = [c for c in content if c.get("type") != "image_url"]

        self.step_idx += 1

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