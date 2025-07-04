from environments.environment import Environment

class EnvFactory():

    def create(self, evals, grader):
        return Environment(evals, grader)