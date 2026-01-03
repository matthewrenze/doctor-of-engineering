import os
import math
from openai import AzureOpenAI

# Set variables
model_name = "gpt-4.1-mini"
# model_name = "gpt-5.2"
api_version = "2025-01-01-preview"

# MCQA Prompts
# High prob; low entropy (high certainty)
# prompt = "What is 2 + 2? A: 3, B: 4, C: 5."

# High prob; high entropy (not really possible)
# prompt = "A fair die is rolled, what is the number? A: 1, B: 2, C: 3, D: 4, E: 5, F: 6."

# Low prob; high entropy (no right answer)
# prompt = "What is the capital of France? A: Berlin, B: Madrid, C: Rome, D: Canberra."

# Low prob; high entropy (no knowledge of right answer)
prompt = "What is the temperature (in °C) in New York City now? A:21, B: 22, C: 23, D: 24."

# Append the MCQA post-fix
prompt += " Respond with only the letter of the best answer."

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

# Get the first token's info
token_info = choice.logprobs.content[0]

# Get the token
token = token_info.token

# Get the log-probability
lp = token_info.logprob

# Get the probability
probability = math.exp(lp)

# Get the entropy over top alternatives
entropy = 0.0
top = token_info.top_logprobs
for alt in top:
    p = math.exp(alt.logprob)
    entropy -= p * math.log(p)

# Normalize the entropy
norm_entropy = entropy / math.log(len(top))

# Get the margin between top two alternatives
if len(top) >= 2:
    p1 = math.exp(top[0].logprob)
    p2 = math.exp(top[1].logprob)
    margin = p1 - p2
else:
    margin = 0.0

# Print the results
print(f"Prompt: {prompt}")
print(f"Response: {'|'.join(tokens)}")
print(f"Num tokens: {len(tokens)}")
print()
print(f"Probability:   {probability:.4f}")
print(f"Norm. Entropy: {norm_entropy:.4f}")
print(f"Margin:        {margin:.4f}")


# Print the top alternatives for all tokens
print("\nTop alternatives for the first token:")
token = token_info.token
print(f"Token: {repr(token)}")
top = token_info.top_logprobs
for alt in top:
    alt_token = alt.token
    alt_lp = alt.logprob
    alt_p = math.exp(alt_lp)
    print(f"   {repr(alt_token):>12} | p={alt_p:.4f}")