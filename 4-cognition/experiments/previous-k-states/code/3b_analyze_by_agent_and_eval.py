import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Set parameters
model_name = "gpt-4.1-mini"
input_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/by-agent-and-eval"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(input_file_path)

# Filter rows
summaries = summaries[summaries["model_name"] == model_name]
summaries = summaries[summaries["eval_name"].str.startswith("tw-")]

# Create groups
summaries = summaries.groupby(["agent_name", "model_name", "eval_name"], as_index=False).agg({
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
agent_order = sorted(
    summaries["agent_name"].unique(),
    key=lambda name: (name.rsplit('-v', 1)[0], int(name.rsplit('-v', 1)[1]))
)
summaries["agent_name"] = pd.Categorical(summaries["agent_name"], categories=agent_order, ordered=True)
summaries = summaries.sort_values("agent_name")

# Order the eval names
eval_order = [
    "tw-simple-1",
    "tw-coin-1",
    "tw-coin-2",
    "tw-coin-3",
    "tw-treasure-1",
    "tw-treasure-2",
    "tw-treasure-3",
    "tw-cooking-1",
    "tw-cooking-2",
    "tw-cooking-3"
]
summaries["eval_name"] = pd.Categorical(
    summaries["eval_name"],
    categories=eval_order,
    ordered=True)

# Create plot for task completion accuracy
accuracy_file_name = f"accuracy-by-agent-and-eval-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="eval_name",
    y="accuracy",
    hue="agent_name",
    data=summaries)
plt.title(f"Accuracy by Agent and Eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Accuracy (task completion rate)")
plt.ylim(0.0, 1.0)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.legend(title="Agent")
plt.savefig(f"{output_folder_path}/{accuracy_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average steps per task
steps_file_name = f"avg-steps-per-task-by-agent-and-eval-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(14, 6))
ax = sns.barplot(
    x="eval_name",
    y="avg_steps_per_task",
    hue="agent_name",
    data=summaries)
plt.title(f"Average Steps per Task by Agent and Eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Average steps per task")
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.25)
plt.legend(title="Agent")
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
plt.savefig(f"{output_folder_path}/{steps_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average tokens per task
tokens_file_name = f"avg-tokens-per-task-by-agent-and-eval-with-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(14, 6))
ax = sns.barplot(
    x="eval_name",
    y="avg_tokens_per_task",
    hue="agent_name",
    data=summaries)
plt.title(f"Average Tokens by Agent and Eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Average tokens per task")
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.25)
plt.legend(title="Agent")
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
plt.savefig(f"{output_folder_path}/{tokens_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average reward per task
reward_file_name = f"avg-reward-per-task-by-agent-and-eval-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="eval_name",
    y="avg_reward_per_task",
    hue="agent_name",
    data=summaries)
plt.title(f"Average Reward per Task by Agent and Eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Average reward per task")
plt.ylim(0.0, 1.0)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.legend(title="Agent")
plt.savefig(f"{output_folder_path}/{reward_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average reward per step
reward_per_step_file_name = f"avg-reward-per-step-by-agent-and-eval-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="eval_name",
    y="avg_reward_per_step",
    hue="agent_name",
    data=summaries)
plt.title(f"Average Reward per Step by Agent and Eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Reward per step")
#plt.ylim(0.0, 1.0)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.legend(title="Agent")
plt.savefig(f"{output_folder_path}/{reward_per_step_file_name}", bbox_inches='tight')
plt.show()

# Create plot for average reward per token
reward_per_token_file_name = f"reward-per-token-by-agent-and-eval-for-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.barplot(
    x="eval_name",
    y="avg_reward_per_token",
    hue="agent_name",
    data=summaries)
plt.title(f"Average Reward per Token by Agent and Eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Average reward per token")
#plt.ylim(0.0, 1.0)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.legend(title="Agent")
plt.savefig(f"{output_folder_path}/{reward_per_token_file_name}", bbox_inches='tight')
plt.show()


