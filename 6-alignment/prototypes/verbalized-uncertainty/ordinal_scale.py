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

# # Scenario 1 - certain answer
# prompt_1 = "What is the capital of France?"
# response_1 = "The capital of France is Paris."

# # Scenario 2 - incorrect answer
# prompt_1 = "What is the capital of France?"
# response_1 = "The capital of France is Berlin."

# # Scenario 3 - uncertain answer
# prompt_1 = "What is your best guess as to the temperature in Las Vegas today in Fahrenheit?"
# response_1 = "The temperature in Las Vegas today is 60 degrees Fahrenheit."

# # Scenario 4 - ambiguous answer
# prompt_1 = "Is a tomato a vegetable or a fruit?"
# response_1 = "Vegetable."

# Scenario 5 - statistical answer
prompt_1 = "99 out of 100 people prefer option A over option B. Will the next person prefer option A?"
response_1 = "Yes"

# Create the certainty prompt
prompt_2 = "How certain are you about your answer? Classify your confidence as: high, medium, low. Why?"

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
messages = [
    {"role": "user", "content": prompt_1},
    {"role": "assistant", "content": response_1},
    {"role": "user", "content": prompt_2}]

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
certainty = choice.message.content.strip()

# Print the response
print(f"Prompt 1: {prompt_1}")
print(f"Response 1: {response_1}")
print(f"Prompt 2: {prompt_2}")
print(f"Response 2: {certainty}")
print()