# This script demonstrates several measures of token-level uncertainty
# - log-probability - direct measure of how likely the model thought a token was (-0.0 to -inf)
# - token probability - exponentiated log-probability, easier to interpret (0.0 to 1.0)
# - entropy - measure of uncertainty over top alternatives (0.0 to log(N))
# - norm entropy - entropy normalized by log(N) (0.0 to 1.0)
# - margin - difference in probability between top two alternatives (0.0 to 1.0)

import os
import math
from openai import AzureOpenAI

# Set variables
# model_name = "gpt-4.1-mini"
model_name = "gpt-5.2"
api_version = "2025-01-01-preview"

# Prompt prefix
prompt = """
Answer the following question.
If you are certain of the answer, respond with the answer.
If you are uncertain of the answer, respond with "I don't know".
Do not provide any additional text beyond the answer or "I don't know".
---

"""

# Scenario 1 - certain answer
# prompt += "What is the capital of France?"

# Scenario 2 - exact vs approximate answer
# prompt += "What is the exact population of Paris?"
# prompt += "What is the rough population of Paris?"

# Scenario 3 - uncertain answer
# prompt += "What is the temperature in Las Vegas today in Fahrenheit?"

# Scenario 4 - ambiguous answer
# prompt += "Is it a cat or a dog?"

# Scenario 5 - ambiguous answer no context


# HACK: Use EAST US 2 for gpt-5.1/5.2 until EAST US is enabled
if model_name == "gpt-5.1" or model_name == "gpt-5.2":
    api_url = os.environ["AZURE_OPENAI_URL_EASTUS2"]
    api_key = os.environ["AZURE_OPENAI_KEY_EASTUS2"]
else:
    api_url = os.environ["AZURE_OPENAI_URL"]
    api_key = os.environ["AZURE_OPENAI_KEY"]

# Create the client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

# Create the messages
messages = [{"role": "user", "content": prompt}]

# Create the parameters
params = {
    "model": model_name,
    "messages": messages,
}

# Don't set temperature on reasoning models
if "gpt-5" not in model_name:
    params["temperature"] = 0.0

# Get the response
response = client.chat.completions.create(**params)
choice = response.choices[0]
content = choice.message.content.strip()

# Print the response
print(f"Prompt 1: {prompt}")
print(f"Response 1: {content}")
print()