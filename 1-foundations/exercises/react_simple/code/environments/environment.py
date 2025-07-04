from tools.search_tool import SearchTool
from tools.lookup_tool import LookupTool

class Environment:
    def __init__(self, evals):
        self.evals = evals
        self.task = None
        self.task_index = 0
        self.step_index = 0

    def reset(self):
        self.task = self.evals[self.task_index]
        question = self.task["question"]
        obs = f"Question: {question}\n"
        print(obs)
        self.task_index += 1
        self.step_index = 0
        return obs

    def step(self, action: str) -> (str, float, bool):
        obs = ""
        reward = 0.0
        is_done = False

        # Get the action and the parameter from the action string
        action_parts = action.split('[')
        action_name = action_parts[0].strip()
        action_args = action_parts[1].rstrip(']') if len(action_parts) > 1 else ""

        if action_name == "Search":
            tool = SearchTool()
            obs = tool.execute(action_args)

        elif action_name == "Lookup":
            tool = LookupTool()
            entity = action_args.split(',')[0].strip()
            keyword = action_args.split(',')[1].strip()
            obs = tool.execute(entity, keyword)

        elif action_name == "Finish":
            if action_args == self.task["answer"]:
                obs = f"Correct answer: {self.task['answer']}."
                reward = 1.0
            else:
                obs = f"Incorrect answer. Expected: {self.task['answer']}, but got: {action_args}."
                reward = 0.0
            is_done = True

        else:
            obs = f"Unknown action \"{action_name}\". Please use Search, Lookup, or Finish."

        obs = f"Observation {self.step_index + 1}: {obs}"
        print(obs)
        self.step_index += 1
        return obs, reward, is_done



# # DEBUG:
# evals = [{"question": "What is JHU?", "answer": "Johns Hopkins University"}]
# env = Environment(evals)
# env.reset()
#
# action_1 = "Search[Johns Hopkins University]"
# obs_1, reward_1, is_done_1 = env.step(action_1)
# print(f"Test 1:\n - Observation: {obs_1}\n - Reward: {reward_1}\n - Done: {is_done_1}")
#
# action_2 = "Lookup[JHU]"
# obs_2, reward_2, is_done_2 = env.step(action_2)
# print(f"Test 2:\n - Observation: {obs_2}\n - Reward: {reward_2}\n - Done: {is_done_2}")
#
# action_3 = "Finish[Johns Hopkins University]"
# obs_3, reward_3, is_done_3 = env.step(action_3)
# print(f"Test 3:\n - Observation: {obs_3}\n - Reward: {reward_3}\n - Done: {is_done_3}")