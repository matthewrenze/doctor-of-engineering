import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get env variables
api_url = os.environ.get("AZURE_AI_URL")
api_key = os.environ.get("AZURE_AI_KEY")
model_name = "grok-3-mini"

# For Serverless API or Managed Compute endpoints
client = ChatCompletionsClient(
    endpoint=f"{api_url}models",
    credential=AzureKeyCredential(api_key),
    api_version="2024-05-01-preview"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]

response = client.complete(
    messages=messages,
    temperature=0.0,
    # max_tokens=2048,
    model=model_name
)

print(response.choices[0].message.content)
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")

