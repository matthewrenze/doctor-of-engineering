from prompts.prompt import Prompt
from prompts.example_factory import ExampleFactory
from prompts.instruction_factory import InstructionFactory
from prompts.strength_factory import StrengthFactory

SYSTEM_PROMPT = """
You are a helpful assistant.
Complete the assigned tasks.
Respond in English.
Do not use any emojis.
{instruction}
Be concise.
"""

EXAMPLE_PROMPT = """
Answer the following question: What is the capital of France?
"""

class PromptFactory:
    def create(self, task, instruction_id, strength_id) -> Prompt:
        instruction_factory = InstructionFactory()
        strength_factory = StrengthFactory()
        example_factory = ExampleFactory()

        instruction = instruction_factory.create(instruction_id)
        instruction = strength_factory.create(instruction, strength_id)
        system_prompt = SYSTEM_PROMPT.format(instruction=instruction).strip()
        example_prompt = EXAMPLE_PROMPT.strip()
        example_response = example_factory.create(instruction_id)
        user_prompt = task

        return Prompt(system_prompt, example_prompt, example_response, user_prompt)