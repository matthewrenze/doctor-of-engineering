from pandas import DataFrame
from common.parameters import Parameters
from environments.action_parser import ActionParser
from environments.open_qa_env import OpenQAEnv
from environments.mcqa_env import MCQAEnv
from graders.grader_factory import GraderFactory
from tools.tool_router import ToolRouter

class EnvFactory:

    def __init__(self):
        self.grader_factory = GraderFactory()

    def create(self, params: Parameters, eval: DataFrame):

        # Create components
        grader = self.grader_factory.create(params)
        parser = ActionParser()
        router = ToolRouter(params.top_k)

        # Create environment
        if params.env_name == "mcqa":
            return MCQAEnv(params, eval, parser, router, grader)

        elif params.env_name == "open-qa":
            return OpenQAEnv(params, eval, parser, router, grader)

        else:
            raise ValueError(f"Unknown eval name: {params.env_name}")
