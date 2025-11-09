import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Set parameters
model_name = "gpt-4.1-mini"
input_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/by-agent"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(input_file_path)

# Filter rows
# summaries = summaries[summaries["model_name"] == model_name]
summaries = summaries[summaries["eval_name"].str.startswith("tw-")]

# Merge curriculum sublevels by level
summaries = summaries.groupby(["agent_name", "model_name"], as_index=False).agg({
    "tasks": "sum",
    "total_steps": "sum",
    "total_tokens": "sum",
    "total_reward": "sum",
    "accuracy": "mean"
})

# Compute averages
summaries["avg_steps_per_task"] = summaries["total_steps"] / summaries["tasks"]
summaries["avg_tokens_per_task"] = summaries["total_tokens"] / summaries["tasks"]
summaries["avg_reward_per_task"] = summaries["total_reward"] / summaries["tasks"]
summaries["avg_reward_per_step"] = summaries["total_reward"] / summaries["total_steps"]
summaries["avg_reward_per_token"] = summaries["total_reward"] / summaries["total_tokens"]

# Order agents
# [FINISH]

# Create plot for task completion accuracy
accuracy_file_name = f"accuracy-by-agent-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="agent_name",
    y="accuracy",
    data=summaries)
plt.title(f"Accuracy by Agent with {model_name}")
plt.xlabel("Agent")
plt.ylabel("Accuracy (task completion rate)")
plt.ylim(0.0, 1.0)
for p in ax.patches:
    ax.annotate(f"{p.get_height():.1%}",(p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=9)
plt.savefig(f"{output_folder_path}/{accuracy_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average steps per task
steps_file_name = f"avg-steps-per-task-by-agent-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(14, 6))
ax = sns.barplot(
    x="agent_name",
    y="avg_steps_per_task",
    data=summaries)
plt.title(f"Average Steps per Task by Agent with {model_name}")
plt.xlabel("Agent")
plt.ylabel("Average steps per task")
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
for p in ax.patches:
    ax.annotate(f"{int(p.get_height()):,}",(p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=9)
plt.savefig(f"{output_folder_path}/{steps_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average tokens per task
tokens_file_name = f"avg-tokens-per-task-by-agent-with-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(14, 6))
ax = sns.barplot(
    x="agent_name",
    y="avg_tokens_per_task",
    data=summaries)
plt.title(f"Average Tokens by Agent with {model_name}")
plt.xlabel("Agent")
plt.ylabel("Average tokens per task")
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
for p in ax.patches:
    ax.annotate(f"{int(p.get_height()):,}",(p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=9)
plt.savefig(f"{output_folder_path}/{tokens_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average reward per task
reward_file_name = f"avg-reward-per-task-by-agent-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="agent_name",
    y="avg_reward_per_task",
    data=summaries)
plt.title(f"Average Reward per Task by Agent with {model_name}")
plt.xlabel("Agent")
plt.ylabel("Average reward per task")
plt.ylim(0.0, 1.0)
for p in ax.patches:
    ax.annotate(f"{p.get_height():.2f}",(p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=9)
plt.savefig(f"{output_folder_path}/{reward_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average reward per step
reward_per_step_file_name = f"avg-reward-per-step-by-agent-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="agent_name",
    y="avg_reward_per_step",
    data=summaries)
plt.title(f"Average Reward per Step by Agent with {model_name}")
plt.xlabel("Agent")
plt.ylabel("Reward per step")
#plt.ylim(0.0, 1.0)
for p in ax.patches:
    ax.annotate(f"{p.get_height():.4f}",(p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=9)
plt.savefig(f"{output_folder_path}/{reward_per_step_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average reward per token
reward_per_token_file_name = f"reward-per-token-by-agent-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="agent_name",
    y="avg_reward_per_token",
    data=summaries)
plt.title(f"Average Reward per Token by Agent with {model_name}")
plt.xlabel("Agent")
plt.ylabel("Average reward per token")
#plt.ylim(0.0, 1.0)
for p in ax.patches:
    ax.annotate(f"{p.get_height():.6f}",(p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=9)
plt.savefig(f"{output_folder_path}/{reward_per_token_file_name}", bbox_inches='tight')
plt.show()


