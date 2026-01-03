import os
import numpy as np
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
# prompt = "What is the capital of France?"
# prompt = "Give me a random number between 1 and 100."
# prompt = "Which is it, a cat or a dog?"
prompt = "Is the number of letters in the alphabet even or odd?"

# Add the prompt post-fix
prompt += "\nPlease provide only the answer (and no other text) in your response."

# Create the client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version)

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

# Collect outputs and per-sample action distributions (from first generated token)
outputs = []
samples = []
samples_top_tokens = []
samples_top_probs = []

for choice in response.choices:
    text = choice.message.content.strip()
    outputs.append(text)

    # Extract logprobs for the first token
    all_log_probs = choice.logprobs
    first_token = all_log_probs.content[0]
    top_log_probs = first_token.top_logprobs

    # Get the tokens for the vocabulary
    top_tokens = [t.token for t in top_log_probs]

    # Convert to probabilities
    top_log_probs = np.array([t.logprob for t in top_log_probs], dtype=np.float64)
    top_probs = np.exp(top_log_probs - np.max(top_log_probs))
    top_probs = top_probs / (np.sum(top_probs) + 1e-12)

    # Create a dictionary of tokens and probabilities
    token_dict = dict(zip(top_tokens, top_probs))
    token_dict["__OTHER__"] = float(max(0.0, 1.0 - float(np.sum(top_probs))))

    # Add to lists
    samples.append(token_dict)
    samples_top_tokens.append(top_tokens + ["__OTHER__"])
    samples_top_probs.append(top_probs.tolist() + [token_dict["__OTHER__"]])

# print("Raw samples:")
# for i, o in enumerate(outputs, 1):
#     print(f"{i:02d}: {o}")

# Build the top-k tokens and probabilities matrix (for display)
max_k = max(len(row) for row in samples_top_tokens)
top_tokens_matrix = np.array([
    row + [""] * (max_k - len(row))
    for row in samples_top_tokens
], dtype=object)
top_probs_matrix = np.array([
    row + [0.0] * (max_k - len(row))
    for row in samples_top_probs
], dtype=np.float64)


print("\nTop-k token matrix (rows = samples, cols = rank):")
for i, row in enumerate(top_tokens_matrix, 1):
    print(f"{i:02d}: {row}")
print()

print("\nTop-k probability matrix: (rows = samples, cols = rank):")
for i, row in enumerate(top_probs_matrix, 1):
    formatted = [f"{p:.4f}" for p in row]
    print(f"{i:02d}: {formatted}")
print()

# Build the full vocabulary from all samples
vocab = set()
for token_probs in samples:
    vocab.update(token_probs.keys())
vocab = sorted(vocab)

# Build the probability matrix
probs = np.zeros((len(samples), len(vocab)), dtype=np.float64)
for i, token_probs in enumerate(samples):
    for j, tok in enumerate(vocab):
        probs[i, j] = token_probs.get(tok, 0.0)

# Get length of vocabulary
length = probs.shape[1]


# Define entropy function
def entropy(p):
    p = np.asarray(p, dtype=np.float64)
    return float(-np.sum(p * np.log(p + 1e-12)))

# Compute entropies
predictive_entropy = entropy(np.mean(probs, axis=0))            # total uncertainty
expected_entropy = float(np.mean([entropy(p) for p in probs]))  # aleatoric uncertainty
mutual_information = predictive_entropy - expected_entropy      # epistemic uncertainty


print(f"Samples used: {len(probs)}/{n_samples}")
print(f"Top-k tokens used: {length}")

print("\nEntropies:")
print(f"Predictive entropy H[E[p]]:   {predictive_entropy:.4f}")
print(f"Expected entropy E[H[p]]:     {expected_entropy:.4f}")
print(f"Mutual information (MI):      {mutual_information:.4f}")

# Normalize entropies
max_entropy = float(np.log(length + 1e-12))
print("\nNormalized:")
print(f"Norm predictive entropy: {predictive_entropy / max_entropy:.4f}")
print(f"Norm expected entropy:   {expected_entropy / max_entropy:.4f}")
print(f"Norm mutual information: {mutual_information / max_entropy:.4f}")

# Compute certainty
print("\nCertainties:")
print(f"Total certainty: {1.0 - (predictive_entropy / max_entropy):.4f}")
print(f"Aleatoric certainty:   {1.0 - (expected_entropy / max_entropy):.4f}")
print(f"Epistemic certainty: {1.0 - (mutual_information / max_entropy):.4f}")
