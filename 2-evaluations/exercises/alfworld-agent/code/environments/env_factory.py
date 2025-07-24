from environments.alfworld_tw_env import AlfWorldTwEnv
from environments.alfworld_thor_env import AlfWorldThorEnv

class EnvFactory:

    def create(self, eval_name, evals):
        if eval_name.startswith("alfworld-tw"):
            return AlfWorldTwEnv(evals)
        elif eval_name.startswith("alfworld-thor"):
            return AlfWorldThorEnv(evals)
        else:
            raise ValueError(f"Unknown eval name: {eval_name}.")