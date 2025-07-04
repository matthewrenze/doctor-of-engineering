import os
from openai import AzureOpenAI

class Model:
    def __init__(self, model_name):
        self.api_key = os.environ['AZURE_OPENAI_KEY']
        self.api_url = os.environ['AZURE_OPENAI_URL']
        self.api_version = "2025-01-01-preview"
        self.model_name = model_name
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.client = AzureOpenAI(
            api_key=self.api_key,
            azure_endpoint=self.api_url,
            api_version=self.api_version)

    def reset(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def get_response(self, prompt):

        # Get the response
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            top_p=1.0)

        # Get the content
        content = response.choices[0].message.content

        # Accumulate tokens
        self.input_tokens += response.usage.prompt_tokens
        self.output_tokens += response.usage.completion_tokens
        self.total_tokens += response.usage.total_tokens

        return content
