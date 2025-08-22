from openai import OpenAI

# model_name = "gpt-4.1-mini"
# model_name = "gpt-4.1"
# model_name = "o3-mini"  # (temperature not supported)
# model_name = "o3"  # (temperature not supported)
# model_name = "gpt-5-mini"
model_name = "gpt-5"

client = OpenAI()

message = "What is the capital of France?"
messages = [{"role": "user", "content": message}]

response = client.chat.completions.create(
  model=model_name,
  messages=messages)

print(f"Response: {response.choices[0].message.content}")
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")