class Prompt:
    def __init__(self, system_prompt, example_prompt, example_response, user_prompt):
        self.system_prompt = system_prompt
        self.example_prompt = example_prompt
        self.example_response = example_response
        self.user_prompt = user_prompt