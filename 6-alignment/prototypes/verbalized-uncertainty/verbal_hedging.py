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

# Scenarios
# response_2 = "I am absolutely certain because the U.S. Supreme Court ruled in Nix v. Hedden (1893) that tomatoes should be classified as vegetables for tariff purposes, based on their common culinary use."
# response_2 = "I am confident because U.S. federal law, following Supreme Court precedent, classifies tomatoes as vegetables for regulatory and tariff purposes. This classification is explicit and widely cited."
# response_2 = "I'm pretty sure because tomatoes are commonly treated as vegetables in culinary contexts and U.S. federal regulations have classified them as such for certain purposes."
# response_2 = "I'm not entirely sure because while tomatoes are classified as vegetables in some legal contexts, they are botanically fruits, and the classification may vary depending on the specific statute or regulatory purpose."
response_2 = "I don't know. I'm just guessing."

prompt = """
Below is a conversation from another LLM. 
Based on the amount of verbal hedging how certain is the LLM on a scale of 1-10?

---
User: "Is a tomato classified as a vegetable under U.S. federal law?"
Model: "Yes"
User: "How certain are you and why?"
Model: """ + response_2 + """

"""

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
certainty = choice.message.content.strip()

# Print the response
print(f"Prompt: {prompt}")
print(f"Response: {certainty}")
print()