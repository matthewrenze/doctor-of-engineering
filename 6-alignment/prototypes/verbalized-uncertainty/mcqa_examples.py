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

# MCQA Prompts
# High prob; low entropy (high certainty)
# prompt = "What is 2 + 2? A: 3, B: 4, C: 5."

# High prob; high entropy (not really possible)
# prompt = "A fair die is rolled, what is the number? A: 1, B: 2, C: 3, D: 4, E: 5, F: 6"

# Low prob; high entropy (no right answer)
# prompt = "What is the capital of France? A: Berlin, B: Madrid, C: Rome, D: Canberra"

# Low prob; low entropy (some knowledge of right answer)
# prompt = "What is the capital of Germany? A: Berlin, B: Madrid, C: Rome, D: Canberra"

# Low prob; high entropy (no knowledge of right answer)
prompt = "What is the temperature (in °C) in New York City now? A:21, B: 22, C: 23, D: 24"

# Append the MCQA post-fix
prompt += "\nRespond with only the letter of the best answer."

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

# Create lists to hold token-level data
tokens = []
log_probs = []
probabilities = []
entropies = []
norm_entropies = []
margins = []

# Process each token in the completion
for token_info in choice.logprobs.content:

    # Get the token
    token = token_info.token
    tokens.append(token)

    # Get the log-probability
    lp = token_info.logprob
    log_probs.append(lp)

    # Get the propability
    probability = math.exp(lp)
    probabilities.append(probability)

    # Get the entropy over top alternatives
    entropy = 0.0
    top = token_info.top_logprobs
    for alt in top:
        p = math.exp(alt.logprob)
        entropy -= p * math.log(p)
    entropies.append(entropy)

    # Get normalized entropy
    norm_entropy = entropy / math.log(len(top))
    norm_entropies.append(norm_entropy)

    # Get the margin between top two alternatives
    if len(top) >= 2:
        p1 = math.exp(top[0].logprob)
        p2 = math.exp(top[1].logprob)
        margin = p1 - p2
    else:
        margin = 0.0
    margins.append(margin)

print(f"Prompt: {prompt}")
print(f"Completion: {''.join(tokens)}")
print(f"Min probability: {min(probabilities):.4f}")
print(f"Norm. entropy: {sum(norm_entropies) / len(norm_entropies):.4f}")
print(f"Min margin: {min(margins):.4f}")

# Print the top alternatives for all tokens
print("\nTop alternatives per token:")
for token_info in choice.logprobs.content:
    token = token_info.token
    print(f"Token: {repr(token)}")
    top = token_info.top_logprobs
    for alt in top:
        alt_token = alt.token
        alt_lp = alt.logprob
        alt_p = math.exp(alt_lp)
        print(f"   {repr(alt_token):>12} | p={alt_p:.4f}")
