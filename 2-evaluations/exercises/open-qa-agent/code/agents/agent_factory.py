from agents.baseline_agent import BaselineAgent
from agents.react_agent import ReactAgent

class AgentFactory:
    def create(self, agent_name, model):
        if agent_name == 'baseline':
            return BaselineAgent(model)
        elif agent_name == 'react':
            return ReactAgent(model)
        else:
            raise ValueError(f"Unknown agent type: {agent_name}")