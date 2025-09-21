import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
model_name = "gpt-4.1-mini"
eval_size = 1000
summaries_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/"
output_file_name = f"token-efficiency.png"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(summaries_file_path)

# Filter rows
summaries = summaries[summaries["model_name"] == model_name]
summaries = summaries[summaries["eval_name"] == f"simple-qa-{eval_size}"]

# Group by agent
groups = summaries.groupby("agent_name")

# Verify that all agents have the same number of tasks
num_episodes_per_agent = groups["tasks"].sum()
if len(num_episodes_per_agent.unique()) != 1:
    raise ValueError("Not all agents have the same number of tasks")
episodes = num_episodes_per_agent.unique()[0]

# Summarize by agent (mean accuracy and mean tokens)
groups = groups[["accuracy", "total_tokens"]].mean().reset_index()

# Compute efficiency: accuracy per token
groups["token_efficiency"] = groups["accuracy"] / groups["total_tokens"]

# Extract numeric k for sorting
groups["agent_num"] = groups["agent_name"].str.extract(r"(\d+)").astype(int)
groups = groups.sort_values("agent_num")

# Plot efficiency
plt.figure(figsize=(10, 6))
sns.barplot(
    x="agent_name",
    y="token_efficiency",
    data=groups,
    order=groups["agent_name"]
)
plt.title(f"Token Efficiency by Agent for {model_name} model on simple-qa-{episodes}")
plt.xlabel("Agent")
plt.ylabel("Accuracy per Token")
plt.xticks(rotation=10, ha="right")
plt.subplots_adjust(bottom=0.15)
plt.savefig(f"{output_folder_path}/{output_file_name}")
plt.show()

# Print the table for inspection
print(groups[["agent_name", "accuracy", "total_tokens", "token_efficiency"]])
