import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY_EASTUS2']
api_url = os.environ['AZURE_OPENAI_URL_EASTUS2']
api_version = "2025-03-01-preview"

# model_name = "gpt-5-chat"
model_name = "gpt-5-mini"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

message = "What is the capital of France?"

messages = [{"role": "user", "content": message}]

response = client.responses.create(
    model=model_name,
    input=messages,
    reasoning={"effort": "low"},
    text={"verbosity": "low"},
)
# Note: temperature is not supported in GPT-5

print(f"Response: {response.output_text}")
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")