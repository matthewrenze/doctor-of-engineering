import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
agent_name = "react"
eval_size = 100
summaries_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/accuracy-by-model"
output_file_name = f"accuracy-by-model-for-{agent_name}-on-{eval_size}-task-evals.png"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(summaries_file_path)

# Filter rows
summaries = summaries[summaries["agent_name"] == agent_name]
summaries = summaries[summaries["eval_name"].str.contains(f"-{eval_size}$")]

# Group by model
groups = summaries.groupby("model_name")

# Verify that all groups have the same number of tasks
num_tasks_per_group = groups["tasks"].sum()
if len(num_tasks_per_group.unique()) != 1:
    raise ValueError("Not all agents have the same number of tasks")

# Summarize by model
groups = groups["accuracy"].mean().reset_index()

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(
    x="model_name",
    y="accuracy",
    data=groups)
plt.title(f"Accuracy by model for {agent_name} agent on {eval_size} task evals")
plt.xlabel("Model")
plt.ylabel("Accuracy")
# Rotate the x labels for better readability
plt.xticks(rotation=10, ha='right')
plt.subplots_adjust(bottom=0.15)
plt.ylim(0.0, 1.0)
plt.savefig(f"{output_folder_path}/{output_file_name}")
plt.show()