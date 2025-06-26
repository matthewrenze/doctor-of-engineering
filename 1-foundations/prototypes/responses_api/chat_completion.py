import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY']
api_url = os.environ['AZURE_OPENAI_URL']
api_version = "2025-01-01-preview"
model_name = "gpt-4o-mini"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

response = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": "What is the capital of France?"}])

print(response.choices[0].message.content)