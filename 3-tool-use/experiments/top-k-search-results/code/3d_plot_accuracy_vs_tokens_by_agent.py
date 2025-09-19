import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
model_name = "gpt-4.1-mini"
eval_size = 10
summaries_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/"
output_file_name = f"accuracy-vs-tokens.png"

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

# Sort by k
summaries["agent_num"] = summaries["agent_name"].str.extract(r"(\d+)").astype(int)
summaries = summaries.sort_values("agent_num")

# Create the palette
num_agents = summaries["agent_num"].nunique()
palette = sns.color_palette("RdYlBu_r", num_agents)

# Create a scatterplot of accuracy vs total tokens by agent
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="total_tokens",
    y="accuracy",
    hue="agent_num",
    palette=palette,
    s=100,
    data=summaries)
plt.title(f"Accuracy vs Total Tokens by agent for {model_name} model on simple-qa-{episodes}")
plt.xlabel("Total Tokens")
plt.ylabel("Accuracy")
plt.xlim(0)
plt.ylim(0.0, 1.0)
plt.legend(title="Agent (k=)", bbox_to_anchor=(1.05, 1), loc='upper left', ncol=1)
plt.subplots_adjust(right=0.75)
plt.savefig(f"{output_folder_path}/{output_file_name}")
plt.show()
