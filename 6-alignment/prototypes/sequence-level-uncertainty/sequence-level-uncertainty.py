# This script demonstrates several measures of sequence-level uncertainty
# - min token probability - the lowest token probability in the sequence  (0.0 to 1.0)
# - mean norm entropy - average normalized entropy over all tokens (0.0 to 1.0)
# - min margin - smallest margin between top two alternatives over all tokens (0.0 to 1.0)

import os
import math
from openai import AzureOpenAI

# Set variables
# model_name = "gpt-4.1-mini"
model_name = "gpt-5.2"
api_version = "2025-01-01-preview"

# Prompts
prompt = "What is the capital of France?"
# prompt = "Give me a random number between 1 and 100."
# prompt = "What is my full name?"

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

    # Get the probability
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
print(f"Response: {'|'.join(tokens)}")
print(f"Mean token prob: {sum(probabilities) / len(probabilities):.4f}")
print(f"Min token prob: {min(probabilities):.4f}")
print(f"Mean entropy: {sum(entropies) / len(entropies):.4f}")
print(f"Mean norm. entropy: {sum(norm_entropies) / len(norm_entropies):.4f}")
print(f"Mean margin: {sum(margins) / len(margins):.4f}")
print(f"Min margin: {min(margins):.4f}")


print("\nPer-token:")
for t, lp, p, h, nh, m in zip(tokens, log_probs, probabilities, entropies, norm_entropies, margins):
    print(f"{repr(t):>12} | lp={lp:.4f} | p={p:.4f} | H={h:.4f} | nH={nh:.4f} | M={m:.4f}")

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
        print(f"   {repr(alt_token):>12} | lp={alt_lp:.4f} | p={alt_p:.4f}")
