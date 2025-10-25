import os
from google import genai

class GeminiModel:
    def __init__(self, model_name):
        self.api_key = os.environ["GOOGLE_API_KEY"]
        self.model_name = model_name
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.client = genai.Client(api_key=self.api_key)

    def reset(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def get_response(self, messages):
        
        # Format messages for Gemini
        for message in messages:
            if message["role"] == "system":
                message["role"] = "user"
            if message["role"] == "assistant":
                message["role"] = "model"
            if "parts" not in message:
                message["parts"] = [{"text": message["content"]}]
                del message["content"]

        # Get the response
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=messages,
        )

        # Get the content
        content = response.text

        # Accumulate tokens
        usage = response.usage_metadata
        self.input_tokens += usage.prompt_token_count
        self.output_tokens += (usage.thoughts_token_count or 0) \
            + (usage.candidates_token_count or 0)
        self.total_tokens += usage.total_token_count

        return content
