from  environments.qa_env import QAEnv

class EnvFactory():

    def create(self, evals, grader):
        return QAEnv(evals, grader)