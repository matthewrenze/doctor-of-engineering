import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
model_name = "gpt-4.1-mini"
eval_size = 100
summaries_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/accuracy-by-agent"
output_file_name = f"accuracy-by-agent-for-{model_name}-on-{eval_size}-task-evals.png"

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
num_tasks_per_agent = groups["tasks"].sum()
if len(num_tasks_per_agent.unique()) != 1:
    raise ValueError("Not all agents have the same number of tasks")

# Summarize by agent
groups = groups["accuracy"].mean().reset_index()

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(
    x="agent_name",
    y="accuracy",
    data=groups)
plt.title(f"Accuracy by agent for {model_name} model on {eval_size} task evals")
plt.xlabel("Agent")
plt.ylabel("Accuracy")
plt.xticks(rotation=10, ha='right')
plt.subplots_adjust(bottom=0.15)
plt.ylim(0.0, 1.0)
plt.savefig(f"{output_folder_path}/{output_file_name}")
plt.show()
