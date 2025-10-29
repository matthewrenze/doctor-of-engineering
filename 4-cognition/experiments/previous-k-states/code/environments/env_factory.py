from pandas import DataFrame
from common.parameters import Parameters
from environments.textworld_env import TextWorldEnv

class EnvFactory:

    def create(self, params: Parameters, eval: DataFrame):

        # Create environment
        if params.env_name == "textworld":
            return TextWorldEnv(params, eval)

        else:
            raise ValueError(f"Unknown eval name: {params.env_name}")
