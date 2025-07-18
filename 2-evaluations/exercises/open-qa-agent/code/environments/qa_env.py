from tools.calculator_tool import CalculatorTool

class QAEnv:
    def __init__(self, evals, grader):
        self.evals = evals
        self.grader = grader
        self.task = None
        self.task_index = 0
        self.step_index = 0

    def reset(self):
        self.task = self.evals[self.task_index]
        question = self.task["question"]
        obs = f"Task: Answer the following question.\nQuestion: {question}\n"
        print(obs)
        self.task_index += 1
        self.step_index = 0
        return obs

    def step(self, action: str) -> (str, float, bool):
        obs = ""
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
            obs = tool.execute(action_args)

        elif action_name == "finish":
            question = self.task["question"]
            correct_answer = self.task["answer"]
            predicted_answer = action_args
            is_correct = self.grader.grade(question, correct_answer, predicted_answer)
            if is_correct:
                obs = f"Correct answer: {self.task['answer']}."
                reward = 1.0
            else:
                obs = f"Incorrect answer. Expected: {self.task['answer']}, but got: {action_args}."
                reward = 0.0
            is_done = True

        else:
            obs = f"Unknown action \"{action_name}\". Please use Search, Lookup, or Finish."

        obs = f"Observation: {obs}"
        print(obs)
        self.step_index += 1
        return obs, reward, is_done



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