from common.parameters import Parameters
from agents.actions.actions_factory import ActionsFactory
from agents.examples.examples_factory import ExamplesFactory
from agents.prompts.system_prompt_factory import SystemPromptFactory
from agents.prompts.reflect_prompt_factory import ReflectPromptFactory
from agents.react_agent import ReactAgent
from models.model import Model

class AgentFactory:
    def __init__(self):
        self.system_prompt_factory = SystemPromptFactory()
        self.reflect_prompt_factory = ReflectPromptFactory()
        self.actions_factory = ActionsFactory()
        self.examples_factory = ExamplesFactory()

    def create(self, params: Parameters, model: Model) -> ReactAgent:

        # Get the prompt elements
        system_prompt = self.system_prompt_factory.create(params.is_training)
        reflect_prompt = self.reflect_prompt_factory.create()
        actions = self.actions_factory.create(params.env_name)
        examples = self.examples_factory.create(params.env_name)

        # Replace the placeholders in the system prompt template
        system_prompt = system_prompt.format(
            actions=actions,
            examples=examples,
            max_steps=params.max_steps)

        # Replace the placeholders in the reflect prompt template
        reflect_prompt = reflect_prompt.format(
            max_steps=params.max_steps)

        # Create the agent
        if params.agent_name.startswith("baseline") \
                or params.agent_name.startswith("reflect"):
            return ReactAgent(model, system_prompt, reflect_prompt)
        else:
            raise ValueError(f"Unknown agent type: {params.agent_name}")