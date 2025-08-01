from common.parameters import Parameters
from pandas import DataFrame
from graders.grader import Grader
from environments.gaia_env import GaiaEnv
from workspaces.workspace import Workspace


class EnvFactory():

    def create(self, params: Parameters, evals: DataFrame, grader: Grader):
        if params.eval_name.startswith("gaia"):
            return GaiaEnv(params, evals, grader)
        else:
            raise ValueError(f"Unknown eval name: {params.eval_name}")
