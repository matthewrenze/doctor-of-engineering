from graders.mcqa_grader import MCQAGrader
from graders.open_qa_grader import OpenQAGrader
from common.parameters import Parameters

class GraderFactory:
    def create(self, params=Parameters):
        if params.env_name == "open-qa":
            return OpenQAGrader()
        elif params.env_name == "mcqa":
            return MCQAGrader()
        else:
            return None