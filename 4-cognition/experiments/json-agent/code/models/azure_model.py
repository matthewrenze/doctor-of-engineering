import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient

class AzureModel:
    def __init__(self, model_name):
        self.api_url = os.environ['AZURE_AI_URL']
        self.api_key = os.environ['AZURE_AI_KEY']
        self.api_version = "2025-01-01-preview"
        self.model_name = model_name
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.client = ChatCompletionsClient(
            endpoint=f"{self.api_url}models",
            credential=AzureKeyCredential(self.api_key),
            api_version="2024-05-01-preview")

    def reset(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def get_response(self, messages):

        # Get the response
        response = self.client.complete(
            model=self.model_name,
            messages=messages,
            temperature=0.0,
            response_format="json_object")

        # Get the content
        content = response.choices[0].message.content

        # Accumulate tokens
        self.input_tokens += response.usage.prompt_tokens
        self.output_tokens += response.usage.completion_tokens
        self.total_tokens += response.usage.total_tokens

        return content
