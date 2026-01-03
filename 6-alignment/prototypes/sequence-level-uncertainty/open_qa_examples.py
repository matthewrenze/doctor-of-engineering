import os
import math
from openai import AzureOpenAI

# Set variables
model_name = "gpt-4.1-mini"
# model_name = "gpt-5.2"
api_version = "2025-01-01-preview"

# MCQA Prompts
# High prob; low entropy (high certainty)
# prompt = "What is the capital of France?"

# High prob; high entropy (not really possible)
# prompt = "Two fair dice are rolled, what are the numbers and the sum? Provide your answer in the form 'a + b = sum' with no other text."

# Low prob; low entropy (no knowledge of right answer)
# prompt = "What is the capital of Renzetopia? Provide your best guess."

# Low prob; high entropy (no knowledge of right answer)
prompt = "What is the temperature (in °C) in New York City now? A:21, B: 22, C: 23, D: 24"

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
print(f"Min probability: {min(probabilities):.4f}")
print(f"Norm. entropy: {sum(norm_entropies) / len(norm_entropies):.4f}")
print(f"Min margin: {min(margins):.4f}")

print("\nPer-token:")
for t, p, nh, m in zip(tokens, probabilities, norm_entropies, margins):
    print(f"{repr(t):>12} | p={p:.4f} | nH={nh:.4f} | M={m:.4f}")
