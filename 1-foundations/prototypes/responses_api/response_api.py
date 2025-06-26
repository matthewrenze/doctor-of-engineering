import os
from openai import AzureOpenAI

api_key = os.environ['AZURE_OPENAI_KEY']
api_url = os.environ['AZURE_OPENAI_URL']
api_version = "2025-03-01-preview"
model_name = "gpt-4o-mini"

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

response = client.responses.create(
    model=model_name,
    input="What is the capital of France?")

# Full nested path to response text
print(response.output[0].content[0].text)

# Shortcut to response text
print(response.output_text)