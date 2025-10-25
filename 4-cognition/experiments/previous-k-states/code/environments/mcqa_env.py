import pandas as pd
from workspaces.workspace import Workspace

class MCQAEnv:
    def __init__(self, params, evals, parser, router, grader):
        self.params = params
        self.evals = evals
        self.action_parser = parser
        self.tool_router = router
        self.grader = grader
        self.workspace = None
        self.episode = None
        self.episode_id = 0
        self.task = ""
        self.step_index = 0

    def reset(self, episode_id):
        self.episode_id = episode_id
        self.episode = self.evals.iloc[episode_id].to_dict()
        self.step_index = 0
        self.workspace = Workspace(self.params, episode_id)
        self.workspace.create()
        if (pd.notna(self.episode["files"])
                and self.episode["files"] != ""):
            file_names = self.episode["files"].split(",")
            file_names = [file_name.strip() for file_name in file_names]
            self.workspace.setup(file_names)
        self.task = "Answer the following multiple-choice question:\n"
        self.task += self.episode["question"]
        self.task += "\n\nOptions:\n"
        choices = self.episode["choices"]
        for idx, key in enumerate(choices):
            self.task += f"{key}: {choices[key]}\n"
        self.task = self.task.replace("\n\n", "\n")
        state = "None"
        return self.task, state

    def step(self, action: str) -> (str, float, bool):
        try:

            state = ""
            reward = 0.0
            is_done = False

            # Parse the action
            action_name, action_args = self.action_parser.parse(action)

            # Route the action
            if action_name == "finish":
                correct_answer = self.episode["answer"]
                predicted_answer = action_args[0]
                is_correct = self.grader.grade(self.task, predicted_answer, correct_answer)
                if is_correct:
                    state = f"Correct answer: {self.episode['answer']}."
                    reward = 1.0
                else:
                    state = f"Incorrect answer. Expected: {self.episode['answer']}, but got: {action_args}."
                    reward = 0.0
                is_done = True

            else:
                state = self.tool_router.route(action_name, action_args, self.workspace)

            self.step_index += 1
            return state, reward, is_done

        except Exception as e:
            return f"Error: {str(e)}", 0.0, False



# # DEBUG:
# evals = [{"question": "What is JHU?", "answer": "Johns Hopkins University"}]
# env = Environment(evals)
# env.reset()
#
# action_1 = "Search[JHU]"
# obs_1, reward_1, is_done_1 = env.step(action_1)
# print(f"Test 1:\n - Observation: {obs_1}\n - Reward: {reward_1}\n - Done: {is_done_1}")
#
# action_2 = "Lookup[Johns Hopkins University, JHU]"
# obs_2, reward_2, is_done_2 = env.step(action_2)
# print(f"Test 2:\n - Observation: {obs_2}\n - Reward: {reward_2}\n - Done: {is_done_2}")
#
# action_3 = "Finish[Johns Hopkins University]"
# obs_3, reward_3, is_done_3 = env.step(action_3)
# print(f"Test 3:\n - Observation: {obs_3}\n - Reward: {reward_3}\n - Done: {is_done_3}")