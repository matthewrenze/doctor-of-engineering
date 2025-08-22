import pandas as pd
from tools.calculator_tool import CalculatorTool
from tools.list_files_tool import ListFilesTool
from tools.read_file_as_text_tool import ReadFileAsTextTool
from tools.read_file_as_image_tool import ReadFileAsImageTool
from workspaces.workspace import Workspace

class HLEEnv:
    def __init__(self, params, evals, grader):
        self.params = params
        self.evals = evals
        self.grader = grader
        self.workspace = None
        self.episode = None
        self.episode_id = 0
        self.step_index = 0

    def reset(self, episode_id):
        self.episode = self.evals.iloc[episode_id].to_dict()
        self.episode_id = episode_id
        self.step_index = 0
        self.workspace = Workspace(self.params, episode_id)
        self.workspace.create()
        if (pd.notna(self.episode["files"])
                and self.episode["files"] != ""):
            file_names = self.episode["files"].split(",")
            file_names = [file_name.strip() for file_name in file_names]
            self.workspace.setup(file_names)
        task = self.episode["task"]
        task = task.replace("\n\n", "\n")
        state = f"Task: {task}\n"
        print(state)
        return state

    def step(self, action: str) -> (str, float, bool):
        state = ""
        reward = 0.0
        is_done = False

        # Get the action and the parameter from the action string
        action_parts = action.split('(', 1)
        action_name = action_parts[0].strip()
        action_args = action_parts[1] if len(action_parts) > 1 else ""
        action_args = action_args.rstrip(')')
        action_args = action_args.strip("\"")

        if action_name == "calculate":
            tool = CalculatorTool()
            state = tool.execute(action_args)

        elif action_name == "list_files":
            tool = ListFilesTool(self.workspace.folder_path)
            state = tool.execute()

        elif action_name == "read_file_as_text":
            tool = ReadFileAsTextTool(self.workspace.folder_path)
            state = tool.execute(action_args)

        elif action_name == "read_file_as_image":
            tool = ReadFileAsImageTool(self.workspace.folder_path)
            state = tool.execute(action_args)

        elif action_name == "finish":
            task = self.episode["task"]
            correct_answer = self.episode["answer"]
            predicted_answer = action_args
            is_correct = self.grader.grade(task, correct_answer, predicted_answer)
            if is_correct:
                state = f"Correct answer: {self.episode['answer']}."
                reward = 1.0
            else:
                state = f"Incorrect answer. Expected: {self.episode['answer']}, but got: {action_args}."
                reward = 0.0
            is_done = True

        else:
            state = f"Unknown action \"{action_name}\"."

        if isinstance(state, str):
            state = f"State: {state}"
        else:
            state = f"State: [{len(state)} bytes]"
        print(state)
        self.step_index += 1
        return state, reward, is_done



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