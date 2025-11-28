from common.parameters import Parameters
from agents.actions.actions_factory import ActionsFactory
from agents.examples.examples_factory import ExamplesFactory
from agents.prompts.prompt_factory import PromptFactory
from agents.react_agent import ReactAgent
from models.model import Model

class AgentFactory:
    def __init__(self):
        self.prompt_factory = PromptFactory()
        self.actions_factory = ActionsFactory()
        self.examples_factory = ExamplesFactory()

    def create(self, params: Parameters, model: Model):

        # Get the prompt elements
        system_prompt = self.prompt_factory.create()
        actions = self.actions_factory.create(params.env_name)
        examples = self.examples_factory.create(params.env_name)

        # Replace the placeholders in the prompt template
        system_prompt = system_prompt.format(
            actions=actions,
            examples=examples,
            max_steps=params.max_steps)

        # Create the agent
        if params.agent_name.startswith("baseline") \
                or params.agent_name.startswith("memory"):
            return ReactAgent(model, system_prompt)
        else:
            raise ValueError(f"Unknown agent type: {params.agent_name}")