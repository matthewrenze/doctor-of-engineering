import os
import math
import openai
from azure.core.credentials import AzureKeyCredential

api_type = "azure"
api_key = os.environ.get("AZURE_OPENAI_KEY")
api_base = os.environ.get("AZURE_OPENAI_URL")
api_version = "2025-01-01-preview"
model_name = "gpt-4o-mini"
# model_name = "o3-mini"

system_prompt = """
Answer the following questions by providing your confidence in each possible answer.
Your response should include three parts: Thought, Confidence, and Answer.
Thought: A step-by-step thought process working your way from the question to the answer.
Confidence: A list of answer letters, each with a confidence score between 0.00 and 1.00.
The confidence scores must sum to 1.00, indicating your confidence in each answer.
Answer: The letter of the answer you believe is correct.
"""

example_prompt = """
What is 2 + 2?
A: 2
B: 3
C: 4
D: 5
"""
example_response = """
Thought: 2 + 2 equals 4.
Confidence:
A: 0.00
B: 0.00
C: 1.00
D: 0.00
Answer: C
"""

user_prompt_easy = """
What is the capital of France?
A: London
B: Paris
C: Berlin
D: Madrid
"""

user_prompt_hard = """
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
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": example_prompt},
    {"role": "assistant", "content": example_response},
    {"role": "user", "content": user_prompt_hard}
]

client = openai.AzureOpenAI(
    api_version=api_version,
    api_key=api_key,
    azure_endpoint=api_base,
    azure_deployment=model_name)

response = client.chat.completions.create(
    messages=messages,
    model=model_name,
    temperature=0.0)

# # DEBUG
# print(f"Response: {response}")

# Print response
answer = response.choices[0].message.content.strip()
print(f"Response:\n{answer}\n")
