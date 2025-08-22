from common.parameters import Parameters
from pandas import DataFrame
from graders.grader import Grader
from environments.hle_env import HLEEnv
from workspaces.workspace import Workspace


class EnvFactory():

    def create(self, params: Parameters, evals: DataFrame, grader: Grader):
        if params.eval_name.startswith("hle"):
            return HLEEnv(params, evals, grader)
        else:
            raise ValueError(f"Unknown eval name: {params.eval_name}")
