from  environments.qa_env import QAEnv
from environments.mcqa_env import MCQAEnv

class EnvFactory():

    def create(self, eval_name, evals, grader):
        if eval_name.startswith("aqua-rat"):
            return MCQAEnv(evals, grader)
        else:
            return QAEnv(evals, grader)