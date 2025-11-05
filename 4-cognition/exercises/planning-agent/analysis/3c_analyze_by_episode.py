import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Set parameters
agent_name = "v0-baseline"
model_name = "gpt-4.1-mini"
input_folder_path = "../data/results"
output_folder_path = "../data/plots/by-episode"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
all_results = pd.DataFrame()
input_file_names = os.listdir(input_folder_path)
for input_file_name in input_file_names:
    input_file_path = f"{input_folder_path}/{input_file_name}"
    input_results = pd.read_csv(input_file_path)
    all_results = pd.concat([all_results, input_results], ignore_index=True)

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

for eval_name in eval_order:

    # Copy the results
    results = all_results.copy()

    # Filter rows
    results = results[results["agent_name"] == agent_name]
    results = results[results["model_name"] == model_name]
    results = results[results["eval_name"] == eval_name]

    # Create plot for task completion accuracy
    accuracy_file_name = f"steps-by-episode-for-{agent_name}-with-{model_name}-on-{eval_name}.png"
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    palette = sns.color_palette(n_colors=2)[::-1]
    ax = sns.barplot(
        x="episode",
        y="steps",
        hue="success",
        palette=palette,
        data=results)
    plt.title(f"Steps by Episode for {agent_name} with {model_name} on {eval_name}")
    plt.xlabel("Episode")
    plt.ylabel("Steps")
    plt.ylim(0, 100)
    plt.xticks(rotation=45, ha='center', fontsize=6)
    plt.legend(title="Agent")
    plt.tight_layout()
    plt.savefig(f"{output_folder_path}/{accuracy_file_name}", bbox_inches='tight')
    plt.show()

# Create a scatter plot of steps vs solution steps
scatter_file_name = f"steps-vs-solution-steps-for-{agent_name}-with-{model_name}.png"
sns.set_style("whitegrid")
plt.figure(figsize=(8, 8))
palette = sns.color_palette(n_colors=2)[::-1]
ax = sns.scatterplot(
    x="solution_steps",
    y="steps",
    hue="success",
    palette=palette,
    data=all_results)
plt.title(f"Steps vs Solution Steps for {agent_name} with {model_name}")
plt.xlabel("Solution Steps")
plt.ylabel("Agent Steps")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.legend(title="Success")
plt.tight_layout()
plt.savefig(f"{output_folder_path}/{scatter_file_name}", bbox_inches='tight')
plt.show()
