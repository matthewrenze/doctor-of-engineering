import os
import math
from openai import AzureOpenAI


api_key = os.environ.get("AZURE_OPENAI_KEY")
api_base = os.environ.get("AZURE_OPENAI_URL")
api_version = "2024-05-01-preview"
model_name = "gpt-4o-mini"

question_easy = """
What is the capital of France?
A: London
B: Paris
C: Berlin
D: Madrid
Answer with the letter only.
"""

question_hard = """
Topic: Law
Context: A software company employs exactly seven sales representatives — Kim, Mahr, Parra, Quinn, Stuckey, Tiao, and Udall — to work in its three sales zones — Zone 1, Zone 2, and Zone 3. 
Each sales representative works in exactly one of the sales zones, in accordance with the following conditions: Either Parra or Tiao (but not both) works in Zone 1. 
Either Tiao or Udall (but not both) works in Zone 2. 
Parra and Quinn work in the same sales zone as each other. 
Stuckey and Udall work in the same sales zone as each other. 
There are more of the sales representatives working in Zone 3 than in Zone 2.
Question: Which one of the following could be a complete and accurate list of the sales representatives working in Zone 3?
Choices:
  A: Kim, Mahr
  B: Kim, Tiao
  C: Parra, Quinn
  D: Stuckey, Tiao, Udall
  E: Parra, Quinn, Stuckey, Udall
Answer with the letter only.
"""

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_base,
    api_version=api_version)

response = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": question_hard}],
    temperature=0.0,
    logprobs=True,
    top_logprobs=5)

# # DEBUG
# print(f"Response: {response}")

choice = response.choices[0]
logprobs = choice.logprobs.content

# Print the top n logprobs for each token
print("Top log probabilities for each token:")
for token_info in logprobs:
    print(f"{token_info.token!r}: {token_info.logprob:.4f}")
    top_logprobs = token_info.top_logprobs
    for top_logprob in top_logprobs:
        token = top_logprob.token
        logprob = top_logprob.logprob
        print(f"  {token!r}: {logprob:.4f}")
print()

# Print the selected token logprobs
print("Selected tokens with log probabilities:")
for token_info in logprobs:
    token = token_info.token
    logprob = token_info.logprob
    print(f"{token!r}: {logprob:.4f}")
print()

# Compute the probability of the selected answer
answer_token =  choice.logprobs.content[0].token
answer_log_prob = choice.logprobs.content[0].logprob
answer_probability = math.exp(answer_log_prob)
print(f"Answer probability for '{answer_token}': {answer_probability:.4f}\n")

# Print the final answer
answer = response.choices[0].message.content.strip()
print(f"Final Tokens : {answer}\n")
