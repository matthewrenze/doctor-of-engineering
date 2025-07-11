import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY']
api_url = os.environ['AZURE_OPENAI_URL']
api_version = "2025-01-01-preview"

# model_name = "gpt-4o-mini"
# model_name = "gpt-4.1-mini"
model_name = "o3-mini"
# model_name = "o3"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

message = "What is the capital of France?"

messages = [{"role": "user", "content": message}]

response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    temperature=0.0)

print(f"Response: {response.choices[0].message.content}")
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")