import os
import time
import anthropic
from common.console import warn

# TODO: Need to lock the version number of the anthropic models (instead of using aliases)
# TODO: e.g., "claude-sonnet-4-0" => claude-sonnet-4-20250514

class ClaudeModel:
    def __init__(self, model_name):
        self.api_key = os.environ['ANTHROPIC_KEY']
        self.model_name = model_name
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def reset(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def get_response(self, messages):

        # Replace the system role with user role for Anthropic
        for message in messages:
            if message['role'] == 'system':
                message['role'] = 'user'
            if message["content"] == "":
                message["content"] = "[empty]"

        # Set retry variables
        retries = [10, 20, 30, 60, 180, 300, 600, 1200, 1200]  # wait before each retry
        attempts = 0

        while True:
            try:

                # Get the response
                response = self.client.messages.create(
                    model=self.model_name,
                    max_tokens=4096,
                    messages=messages)

                # Get the content
                content = response.content[0].text

                # Accumulate tokens
                self.input_tokens += response.usage.input_tokens
                self.output_tokens += response.usage.output_tokens
                self.total_tokens += response.usage.input_tokens + response.usage.output_tokens

                return content

            except Exception as e:

                if attempts >= len(retries):
                    raise

                delay = retries[attempts]
                warn(f"Retrying LLM API call in {delay} seconds due to error: {e}")
                time.sleep(delay)
                attempts += 1