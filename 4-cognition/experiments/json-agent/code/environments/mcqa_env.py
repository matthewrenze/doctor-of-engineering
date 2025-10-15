import pandas as pd
from workspaces.workspace import Workspace

class MCQAEnv:
    def __init__(self, params, evals, router, grader):
        self.params = params
        self.evals = evals
        self.tool_router = router
        self.grader = grader
        self.workspace = None
        self.episode = None
        self.episode_id = 0
        self.task = ""
        self.step_index = 0

    def reset(self, episode_id) -> dict:
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
        self.task = "Answer the following multiple-choice question:"
        question = self.episode["question"]
        options = self.episode["choices"]
        state = {"task": self.task, "question": question, "options": options}
        return state

    def step(self, action: dict) -> (str, float, bool):
        try:

            state = ""
            reward = 0.0
            is_done = False

            # Get the action components
            action_name = action.get("name", "")
            action_args = action.get("args", {})

            # Route the action
            if action_name == "finish":
                correct_answer = self.episode["answer"]
                predicted_answer = action_args.get("answer")
                is_correct = self.grader.grade(self.task, predicted_answer, correct_answer)
                reward = 1.0 if is_correct else 0.0
                state = {"is_correct": is_correct, "correct_answer": correct_answer}
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