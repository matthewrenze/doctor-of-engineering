from environments.environment import Environment

class EnvFactory():

    def create(self, evals):
        return Environment(evals)