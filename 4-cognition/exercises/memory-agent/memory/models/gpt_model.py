import os
import time
from openai import AzureOpenAI
from common.console import warn

class GptModel:
    def __init__(self, model_name):
        # HACK: Use EAST US 2 for gpt-5.1 until EAST US is enabled
        if model_name == "gpt-5.1":
            self.api_url = os.environ["AZURE_OPENAI_URL_EASTUS2"]
            self.api_key = os.environ["AZURE_OPENAI_KEY_EASTUS2"]
        else:
            self.api_url = os.environ["AZURE_OPENAI_URL"]
            self.api_key = os.environ["AZURE_OPENAI_KEY"]

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

    def get_response(self, messages):

        # Create the parameters
        params = {
            "model": self.model_name,
            "messages": messages,
            "top_p": 1.0
        }

        # Don't set temperature on reasoning models
        if "o3" not in self.model_name \
                and "gpt-5" not in self.model_name \
                and "gpt-5.1" not in self.model_name:
            params["temperature"] = 0.0

        # Set retry variables
        retries = [10, 20, 30, 60, 180, 300, 600, 1200, 1200]  # wait before each retry
        attempts = 0

        while True:
            try:
                # Get the response
                response = self.client.chat.completions.create(**params)

                # Get the content
                content = response.choices[0].message.content

                # Accumulate tokens (be defensive)
                self.input_tokens += getattr(response.usage, "prompt_tokens", 0)
                self.output_tokens += getattr(response.usage, "completion_tokens", 0)
                self.total_tokens += getattr(response.usage, "total_tokens", 0)

                return content
            except Exception as e:

                if attempts >= len(retries):
                    raise

                delay = retries[attempts]
                warn(f"Retrying LLM API call in {delay} seconds due to error: {e}")
                time.sleep(delay)
                attempts += 1
