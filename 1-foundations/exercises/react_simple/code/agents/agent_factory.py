from agents.agent import Agent

class AgentFactory():
    def create(self, model):
        return Agent(model)