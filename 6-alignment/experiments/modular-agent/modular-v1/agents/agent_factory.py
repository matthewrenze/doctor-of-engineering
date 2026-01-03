from common.parameters import Parameters
from models.model import Model
from agents.system_prompts.system_prompt_factory import SystemPromptFactory
from agents.reasoner.reasoner_agent import ReasonerAgent
from agents.actor.actor_agent import ActorAgent

class AgentFactory:
    def __init__(self):
        self.system_prompt_factory = SystemPromptFactory()

    def create(self, subagent: str, params: Parameters, model: Model):

        # Get the prompt elements
        system_prompt = self.system_prompt_factory.create(subagent)

        # Create the agent
        if subagent == "reasoner":
            return ReasonerAgent(model, system_prompt)
        elif subagent == "actor":
            return ActorAgent(model, system_prompt)
        else:
            raise ValueError(f"Unknown agent type: {params.agent_name}")