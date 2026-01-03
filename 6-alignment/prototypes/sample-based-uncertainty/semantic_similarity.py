# This script compares multiple methods for estimating uncertainty based on semantic similarity
# - mean centroid distance - average distance of samples to the centroid of all samples
# - min centroid distance - distance of the
import os
import numpy as np
from collections import Counter
from openai import AzureOpenAI
from pydub.pyaudioop import maxpp
from sklearn.metrics.pairwise import cosine_similarity

# Set the variables
model_name = "gpt-4.1-mini"
# model_name = "gpt-5.2"
embed_name = "text-embedding-3-large"
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
# prompt = "What is my first name?"
# prompt = "Which is it, a cat or a dog?"
prompt = "What is your biggest security vulnerability?"

# Add the prompt post-fix
prompt += "\nPlease provide only the answer (and no other text) in your response."

# Create the client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_url,
    api_version=api_version
)

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
outputs = [c.message.content.strip() for c in response.choices]

print("Raw samples:")
for i, o in enumerate(outputs, 1):
    print(f"{i:02d}: {o}")

# Get embeddings
embeddings = client.embeddings.create(
    model=embed_name,
    input=outputs)

# Get vectors
vectors = np.array([data.embedding for data in embeddings.data], dtype=np.float32)

# Normalize to unit vectors
norms = np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-12
unit_vectors = vectors / norms

# Compute the centroid
centroid = np.mean(unit_vectors, axis=0, keepdims=True)
centroid = centroid / (np.linalg.norm(centroid) + 1e-12)

# Compute cosine similarity to centroid
centroid_similarities = cosine_similarity(unit_vectors, centroid).flatten()

# Compute centroid similarity stats
mean_centroid_similarity = float(np.mean(centroid_similarities))
min_centroid_similarity = float(np.min(centroid_similarities))
max_centroid_similarity = float(np.max(centroid_similarities))


print("\nCentroid similarity:")
print(f"Mean: {mean_centroid_similarity:.4f}")
print(f"Min: {min_centroid_similarity:.4f}")
print(f"Max: {max_centroid_similarity:.4f}")

# Compute pairwise cosine similarity
similarity_matrix = cosine_similarity(unit_vectors)

# Get upper triangle (excluding diagonal)
upper_triangle = np.triu_indices_from(similarity_matrix, k=1)
pairwise_similarities = similarity_matrix[upper_triangle]

# Compute pairwise similarity stats
mean_pairwise_similarity = float(np.mean(pairwise_similarities))
min_pairwise_similarity = float(np.min(pairwise_similarities))
max_pairwise_similarity = float(np.max(pairwise_similarities))

print("\nPairwise similarity:")
print(f"Mean: {mean_pairwise_similarity:.4f}")
print(f"Min: {min_pairwise_similarity:.4f}")
print(f"Max: {max_pairwise_similarity:.4f}")
