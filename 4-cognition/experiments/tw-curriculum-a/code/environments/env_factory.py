from pandas import DataFrame
from common.parameters import Parameters
from environments.textworld_env_v0 import TextWorldEnvV0
from environments.textworld_env_v1 import TextWorldEnvV1

class EnvFactory:

    def create(self, params: Parameters, eval: DataFrame):

        # Create environment
        if params.env_name == "textworld":
            if params.agent_version == 0:
                return TextWorldEnvV0(params, eval)
            else: # v1 and v2
                return TextWorldEnvV1(params, eval)

        else:
            raise ValueError(f"Unknown eval name: {params.env_name}")
