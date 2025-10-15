import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
model_name = "gpt-4.1-mini"
eval_size = 100
summaries_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/tokens-by-agent"
output_file_name = f"tokens-by-agent-for-{model_name}-on-all-{eval_size}-episode-evals.png"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(summaries_file_path)

# Filter rows
summaries = summaries[summaries["model_name"] == model_name]
summaries = summaries[summaries["eval_name"].str.contains(f"-{eval_size}$")]

# Group by agent
groups = summaries.groupby("agent_name")

# Verify that all agents have the same number of tasks
num_episodes_per_agent = groups["tasks"].sum()
if len(num_episodes_per_agent.unique()) != 1:
    raise ValueError("Not all agents have the same number of tasks")
episodes = num_episodes_per_agent.unique()[0]

# Summarize by agent
groups = groups["total_tokens"].mean().reset_index()

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(
    x="agent_name",
    y="total_tokens",
    data=groups)
plt.title(f"Tokens by agent for {model_name} model on {episodes} episodes")
plt.xlabel("Agent")
plt.ylabel("Tokens")
plt.xticks(rotation=10, ha='right')
plt.subplots_adjust(bottom=0.15)
for index, row in groups.iterrows():
    plt.text(index, row.total_tokens + 40000, f"{row.total_tokens:,.0f}", color='black', ha="center")
plt.savefig(f"{output_folder_path}/{output_file_name}")
plt.show()
