import os
from google import genai

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    {"role": "user", "parts": [{"text": "You are a helpful assistant."}]},
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
)

print(response.text)
print(f"Input tokens: {response.usage_metadata.prompt_token_count}")
print(f"Thought tokens: {response.usage_metadata.thoughts_token_count}")
print(f"Output tokens: {response.usage_metadata.candidates_token_count}")
print(f"Total tokens: {response.usage_metadata.total_token_count}")