import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY_EASTUS2']
api_url = os.environ['AZURE_OPENAI_URL_EASTUS2']
api_version = "2025-01-01-preview"

model_name = "gpt-5-chat"
# model_name = "gpt-5-mini"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

message = "What is the capital of France?"

messages = [{"role": "user", "content": message}]

response = client.chat.completions.create(
    model=model_name,
    messages=messages)
# Note: temperature is not supported in GPT-5

print(f"Response: {response.choices[0].message.content}")
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")