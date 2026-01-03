import os
from collections import Counter
from openai import AzureOpenAI

# Set the variables
model_name = "gpt-4.1-mini"
# model_name = "gpt-5.2"
api_version = "2025-01-01-preview"
n_samples = 8

# HACK: Use EAST US 2 for gpt-5.1/5.2 until EAST US is enabled
if model_name == "gpt-5.1" or model_name == "gpt-5.2":
    api_url = os.environ["AZURE_OPENAI_URL_EASTUS2"]
    api_key = os.environ["AZURE_OPENAI_KEY_EASTUS2"]
else:
    api_url = os.environ["AZURE_OPENAI_URL"]
    api_key = os.environ["AZURE_OPENAI_KEY"]

# Set the prompt
prompt = "What is the capital of France?"
# prompt = "Give me a random number between 1 and 100."
# prompt = "What is my first name?"
# prompt = "Which is it, a cat or a dog?"
# prompt = "What is your biggest security vulnerability?"

# Add the prompt post-fix
prompt += " Please provide only the answer (and no other text) in your response."

# Create the client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version
)

# Create the message
messages = [{"role": "user", "content": prompt}]

# Create the parameters
params = {
    "model": model_name,
    "messages": messages,
    "top_p": 1.0,
    "logprobs": True,
    "top_logprobs": 5,
    "n": n_samples
}

# Don't set temperature on reasoning models
if "gpt-5" not in model_name:
    params["temperature"] = 0.7

# Get the response
response = client.chat.completions.create(**params)
outputs = [c.message.content.strip() for c in response.choices]

print("Raw samples:")
for i, o in enumerate(outputs, 1):
    print(f"{i:02d}: {o}")

# Get answer frequency
counts = Counter(outputs)

# Print the top answer
print(f"\nTop answer: {counts.most_common(1)[0][0]}")

# Print the frequencies
print("\nAnswer frequencies:")
for answer, freq in counts.most_common():
    print(f"{freq}/{n_samples}: {answer}")

# Calculate self-consistency confidence
confidence = counts.most_common(1)[0][1] / n_samples
print(f"\nSelf-consistency: {confidence:.2f}")
