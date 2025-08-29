import os
import anthropic

api_key = os.getenv("ANTHROPIC_KEY")

client = anthropic.Anthropic(api_key=api_key)

messages = [
    {"role": "user", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]

response = client.messages.create(
    model="claude-sonnet-4-0",
    max_tokens=4096,
    messages=messages)

print(response.content[0].text)
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")