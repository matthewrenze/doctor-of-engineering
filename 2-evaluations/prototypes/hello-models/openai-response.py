from openai import OpenAI

# model_name = "gpt-4.1-mini"
# model_name = "gpt-4.1"
# model_name = "o3-mini"  # (temperature not supported)
# model_name = "o3"  # (temperature not supported)
# model_name = "gpt-5-mini"
model_name = "gpt-5"

client = OpenAI()

message = "What is the capital of France?"

response = client.responses.create(
    model=model_name,
    input=message)

print(f"Response: {response.output_text}")
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")