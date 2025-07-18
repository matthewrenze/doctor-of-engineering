from environments.textworld_env import TextWorldEnv

class EnvFactory():

    def create(self, eval_name, evals, grader):
        if eval_name.startswith("simple-game")\
                or eval_name.startswith("coin-game")\
                or eval_name.startswith("cooking-game")\
                or eval_name.startswith("treasure-game"):
            return TextWorldEnv(evals, grader)
        else:
            raise ValueError(f"Unknown eval name: {eval_name}.")