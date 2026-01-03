import os
import math
from openai import AzureOpenAI

# Set variables
model_name = "gpt-4.1-mini"
# model_name = "gpt-5.1"
api_version = "2025-01-01-preview"

# prompt = """
# # Role
# Your task is to cut a carrot, cook it, and then serve it.
#
# # State
# You are in a kitchen with a stove and a counter.
# Your inventory contains a knife and a carrot.
#
# # Actions:
# - go <direction> - move in a direction (north, south, east, west)
# - take <object> - pick up an object
# - cut <object> with <tool> - cut an object with a tool
# - cook <object> with <tool> - cook an object with a tool (e.g. stove, oven, grill)
# - serve <object> - serve the cooked object
#
# # Format
# Write your response in the form: "<selected-action>"
#
# # Examples
# go north
# take apple from counter
# cook potato with stove
# serve soup
# """

# prompt="""
# # Role
# Your task is to find the kitchen.
#
# # State
# You are in a living room with an open door to the east and an open door to the west.
# Your inventory is empty.
#
# # Actions:
# - go <direction> - move in a direction (north, south, east, west)
# - take <object> from <container> - pick up an object from a container
# - open <object> - open an object (e.g. door, container)
#
# # Format
# Write your response in the form: "<selected-action>"
#
# # Examples
# go east
# take key from table
# open door
# """

# # Prompts
# prompt ="""
# # Role
# Your task is to cut the fruit with a knife.
#
# # State
# You are in a kitchen with a counter.
# Your inventory contains a knife, an orange, and an apple.
#
# # Actions:
# - go <direction> - move in a direction (north, south, east, west)
# - take <object> from <container> - pick up an object from a container
# - cut <object> with <tool> - cut an object with a tool
#
# # Format
# Write your response in the form: "<selected-action>"
#
# # Examples
# go north
# take carrot from counter
# cook potato with stove
# """

# Prompts
prompt ="""
# Role
Your task is to put the carrot in the smaller box.

# State
You are in a kitchen with two boxes: box A and box B.
Your inventory contains a carrot.

# Actions:
- go <direction> - move in a direction (north, south, east, west)
- take <object> from <container> - pick up an object from a container
- cut <object> with <tool> - cut an object with a tool
- put <object> in <container> - put an object in a container

# Format
Write your response in the form: "<selected-action>"

# Examples
go north
take carrot from counter
cut potato with knife
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

print(f"Response: {'|'.join(tokens)}")
print(f"Token count: {len(tokens)}")
print(f"Min probability: {min(probabilities):.4f}")
print(f"Mean entropy: {sum(entropies) / len(entropies):.4f}")
print(f"Min margin: {min(margins):.4f}")


print("\nPer-token:")
for t, p, nH, m in zip(tokens, probabilities, norm_entropies, margins):
    print(f"{repr(t):>12} | p={p:.4f} | nH={nH:.4f} | M={m:.4f}")
