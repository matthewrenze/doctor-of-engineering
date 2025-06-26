import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY']
api_url = os.environ['AZURE_OPENAI_URL']
api_version = "2025-03-01-preview"
model_name = "o3-mini"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

response = client.responses.create(
    model=model_name,
    input="What is the capital of France?")

# Shortcut to response text
print(response.output_text)

input_tokens = response.usage.input_tokens
reasoning_tokens = response.usage.output_tokens_details.reasoning_tokens
output_tokens = response.usage.output_tokens
total_tokens = response.usage.total_tokens

print(input_tokens)