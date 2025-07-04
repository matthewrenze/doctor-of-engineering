import re

system_prompt = """
Solve a question answering task with interleaving Thought, Action, Observation steps.
Thought can reason about the current situation, and Action can be one type:
  - Finish[answer] - which returns the answer and finishes the task.
You must only provide one Thought and one Action in your response.
Do not include any other text in your response.
Be concise.

Here are some examples prompts and responses:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought: To answer the question about the elevation range for the area that the eastern sector of the Colorado orogeny extends into, I first need to identify the region this eastern sector covers. The eastern sector is referred to as the Central Plains orogeny and extends into the High Plains. Therefore, I need to determine the elevation range of the High Plains. The High Plains, a subregion of the Great Plains in the United States, rise in elevation from approximately 1,800 to 7,000 feet. Thus, the elevation range for the area that the eastern sector of the Colorado orogeny extends into is 1,800 to 7,000 feet.
Action: Finish[1,800 to 7,000 ft]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought: To answer the question, I need to determine who the character Milhouse from "The Simpsons" was named after. Milhouse’s full name is Milhouse Mussolini Van Houten, and he was created by Matt Groening. The key detail is the origin of the name "Milhouse." It was chosen as a reference to U.S. president Richard Nixon, whose middle name was Milhous. Therefore, Milhouse was named after Richard Nixon.
Action: Finish[Richard Nixon]

Question: Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?
Thought: To determine which documentary is about Finnish rock groups, I first consider the two options: Adam Clayton Powell and The Saimaa Gesture. The film Adam Clayton Powell is a 1989 American documentary focused on the life of the African-American politician Adam Clayton Powell Jr., so it is not related to Finnish rock music. Therefore, the documentary about Finnish rock groups must be The Saimaa Gesture.
Action: Finish[The Saimaa Gesture]

Question: What profession does Nicholas Ray and Elia Kazan have in common?
Thought: To determine the profession Nicholas Ray and Elia Kazan have in common, I first identify their respective professions. Nicholas Ray was a film director, screenwriter, and actor. Elia Kazan was a film and theatre director, producer, screenwriter, and actor. The professions they share are director, screenwriter, and actor.
Action: Finish[director, screenwriter, actor]

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought: To determine which magazine was started first, I need the founding years of each. Arthur's Magazine began publication in 1844, while First for Women was launched in 1989. Since 1844 is earlier than 1989, Arthur's Magazine was started first.
Action: Finish[Arthur's Magazine]

Question: Were Pavel Urysohn and Leonid Levin known for the same type of work?
To determine whether Pavel Urysohn and Leonid Levin were known for the same type of work, I examine their professional fields. Pavel Urysohn was a Soviet mathematician known for his work in dimension theory. Leonid Levin is a Soviet-American mathematician and computer scientist. Since both are recognized as mathematicians, they were known for the same type of work in mathematics.
Action: Finish[yes]
"""

class BaselineAgent:
    def __init__(self, model):
        self.model = model
        self.prompt = system_prompt
        self.step_idx = 0

    def reset(self):
        self.model.reset()
        self.prompt = system_prompt
        self.step_idx = 0

    def act(self, obs: str) -> str:
        obs = obs.strip()
        self.prompt = self.prompt + "\n" + obs
        response = self.model.get_response(self.prompt)
        response = response.replace("\n\n", "\n")
        response = response.strip()

        action = re.search(r"Action: (.*)", response).group(1)

        self.prompt = self.prompt + "\n" + response
        self.step_idx += 1
        print(response)
        return action


# # DEBUG:
# class TestModel:
#     def get_response(self, prompt):
#         return "Thought: This is a mock thought.\nAction: Finish[mock answer]"
# model = TestModel()
# agent = Agent(model)
# action = agent.act("Mock observation for testing.")
# print(agent.prompt)
# print(action)