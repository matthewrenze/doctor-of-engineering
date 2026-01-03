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

# Collect outputs and per-sample token distributions (for ALL generated tokens)
outputs = []
samples = []                 # list of lists; samples[s][t] = dict(token->prob) for token position t
samples_lengths = []

for choice in response.choices:
    text = choice.message.content.strip()
    outputs.append(text)

    all_log_probs = choice.logprobs
    token_logprobs = all_log_probs.content
    samples_lengths.append(len(token_logprobs))

    sample_tokens = []

    for token_pos in token_logprobs:
        top_log_probs = token_pos.top_logprobs

        # Get tokens (top-k) for this position
        top_tokens = []
        for t in top_log_probs:
            top_tokens.append(t.token)

        # Convert to probabilities (top-k only, renormalized)
        top_log_probs_values = []
        for t in top_log_probs:
            top_log_probs_values.append(t.logprob)
        top_log_probs_values = np.array(top_log_probs_values, dtype=np.float64)

        top_probs = np.exp(top_log_probs_values - np.max(top_log_probs_values))
        top_probs = top_probs / (np.sum(top_probs) + 1e-12)

        token_dict = dict(zip(top_tokens, top_probs))
        token_dict["__OTHER__"] = float(max(0.0, 1.0 - float(np.sum(top_probs))))

        sample_tokens.append(token_dict)

    samples.append(sample_tokens)

# Define entropy function
def entropy(p):
    p = np.asarray(p, dtype=np.float64)
    return float(-np.sum(p * np.log(p + 1e-12)))

# Option A: token-wise uncertainty over time
T = min(samples_lengths)  # truncate to min generated length across samples

predictive_entropies = []
expected_entropies = []
mutual_informations = []
lengths = []

for t in range(T):
    # Build vocabulary at this token position across samples
    vocab = set()
    for s in range(len(samples)):
        vocab.update(samples[s][t].keys())
    vocab = sorted(vocab)

    # Build probability matrix for this position: shape (S, K_t)
    probs = np.zeros((len(samples), len(vocab)), dtype=np.float64)
    for s in range(len(samples)):
        token_probs = samples[s][t]
        for j, tok in enumerate(vocab):
            probs[s, j] = token_probs.get(tok, 0.0)

    lengths.append(probs.shape[1])

    pe = entropy(np.mean(probs, axis=0))
    ee = float(np.mean([entropy(p) for p in probs]))
    mi = pe - ee

    predictive_entropies.append(pe)
    expected_entropies.append(ee)
    mutual_informations.append(mi)

# Aggregate across time (mean)
mean_predictive_entropy = float(np.mean(predictive_entropies)) if len(predictive_entropies) > 0 else 0.0
mean_expected_entropy = float(np.mean(expected_entropies)) if len(expected_entropies) > 0 else 0.0
mean_mutual_information = float(np.mean(mutual_informations)) if len(mutual_informations) > 0 else 0.0

# Normalize using mean log(K_t) across time (consistent with varying vocab sizes)
max_entropies = []
for k in lengths:
    max_entropies.append(float(np.log(k + 1e-12)))
mean_max_entropy = float(np.mean(max_entropies)) if len(max_entropies) > 0 else 1.0

# Print results
print(f"Prompt: {prompt}\n")
print("Responses:")
for i, o in enumerate(outputs, 1):
    print(f"{i:02d}: {o}")
print()

print(f"Samples used: {len(samples)}/{n_samples}")
print(f"Token positions used (T): {T}")

print("\nPer-token (mean over positions) entropies:")
print(f"Mean predictive entropy H[E[p_t]]:   {mean_predictive_entropy:.4f}")
print(f"Mean expected entropy E[H[p_t]]:     {mean_expected_entropy:.4f}")
print(f"Mean mutual information (MI_t):      {mean_mutual_information:.4f}")

print("\nPer-token (mean over positions) normalized:")
print(f"Norm mean predictive entropy: {mean_predictive_entropy / mean_max_entropy:.4f}")
print(f"Norm mean expected entropy:   {mean_expected_entropy / mean_max_entropy:.4f}")
print(f"Norm mean mutual information: {mean_mutual_information / mean_max_entropy:.4f}")

print("\nPer-token (mean over positions) certainties:")
print(f"Total certainty:     {1.0 - (mean_predictive_entropy / mean_max_entropy):.4f}")
print(f"Aleatoric certainty: {1.0 - (mean_expected_entropy / mean_max_entropy):.4f}")
print(f"Epistemic certainty: {1.0 - (mean_mutual_information / mean_max_entropy):.4f}")
