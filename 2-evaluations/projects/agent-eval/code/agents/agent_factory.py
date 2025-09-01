from common.parameters import Parameters
from models.gpt_model import GptModel
from agents.baseline_agent import BaselineAgent
from agents.react_agent import ReactAgent


class AgentFactory:
    def create(self, params: Parameters, model: GptModel):
        if params.agent_name == 'baseline':
            return BaselineAgent(model)
        elif params.agent_name == 'react':
            return ReactAgent(model)
        else:
            raise ValueError(f"Unknown agent type: {params.agent_name}")