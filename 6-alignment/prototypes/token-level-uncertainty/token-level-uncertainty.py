# This script demonstrates several measures of (single) token-level uncertainty
# - negative log probability - direct measure of how likely the model thought the token was (-0.0 to -inf)
# - token probability - exponentiated log-probability, easier to interpret (0.0 to 1.0)
# - entropy - measure of uncertainty over top alternatives (0.0 to log(N))
# - norm entropy - entropy normalized by log(N) (0.0 to 1.0)
# - margin - difference in probability between top two alternatives (0.0 to 1.0)

import os
import math
from openai import AzureOpenAI

# Set variables
model_name = "gpt-4.1-mini"
# model_name = "gpt-5.2"
api_version = "2025-01-01-preview"

# Prompts
# prompt = "What is the capital of France? Provide the answer only."
# prompt = "Give me a random number between 1 and 100. Provide the number only."
prompt = "What is my first name? Provide the answer only. Do not provide any other text."

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
    "top_p": 1.0,
    "logprobs": True,
    "top_logprobs": 5
}

# Don't set temperature on reasoning models
if "gpt-5" not in model_name:
    params["temperature"] = 0.0

# Get the response
response = client.chat.completions.create(**params)
choice = response.choices[0]

# Get the tokens
tokens = []
for token_info in choice.logprobs.content:
    token = token_info.token
    tokens.append(token)

# Process each token in the completion
token_info = choice.logprobs.content[0]

# Get the token
token = token_info.token

# Get the log-probability
log_prob = token_info.logprob

# Get the probability
probability = math.exp(log_prob)

# Get the entropy over top alternatives
entropies = []
entropy = 0.0
top = token_info.top_logprobs
for alt in top:
    p = math.exp(alt.logprob)
    entropy -= p * math.log(p)
entropies.append(entropy)

# Normalize the entropy
norm_entropy = entropy / math.log(len(top))

# Get the margin between top two alternatives
if len(top) >= 2:
    p1 = math.exp(top[0].logprob)
    p2 = math.exp(top[1].logprob)
    margin = p1 - p2
else:
    margin = 0.0

# Print the statistics
print(f"Prompt: {prompt}")
print(f"Response: {'|'.join(tokens)}")
print(f"Num tokens: {len(tokens)}")
print()
print(f"Log-probability: {log_prob:.4f}")
print(f"Token probability: {probability:.4f}")
print(f"Entropy: {entropy:.4f}")
print(f"Norm. entropy: {norm_entropy:.4f}")
print(f"Margin: {margin:.4f}")

# Print the top alternatives for all tokens
print("\nTop alternatives for the first token:")
token = token_info.token
print(f"Token: {repr(token)}")
top = token_info.top_logprobs
for alt in top:
    alt_token = alt.token
    alt_lp = alt.logprob
    alt_p = math.exp(alt_lp)
    print(f"   {repr(alt_token):>12} | lp={alt_lp:.4f} | p={alt_p:.4f}")
