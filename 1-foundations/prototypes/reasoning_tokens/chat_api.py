import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY']
api_url = os.environ['AZURE_OPENAI_URL']
api_version = "2025-01-01-preview"
# model_name = "gpt-4o-mini"
model_name = "o3-mini"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

response = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    reasoning_effort="high",)

print(f"Response {response.choices[0].message.content}")

# Get token usage
input_tokens = response.usage.prompt_tokens
reasoning_tokens = response.usage.completion_tokens_details.reasoning_tokens
completion_tokens = response.usage.completion_tokens
output_tokens = completion_tokens - reasoning_tokens
total_tokens = response.usage.total_tokens
total_tokens_check = input_tokens + reasoning_tokens + output_tokens

print(f"Input tokens: {input_tokens}")
print(f"Reasoning tokens: {reasoning_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Total tokens: {total_tokens}")
print(f"Total tokens (check): {total_tokens_check}")

print()