import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Set parameters
agent_names = ["react-v0", "react-v1"]
model_name = "gpt-4.1-mini"
input_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/steps-by-eval"
output_file_name = f"steps-by-agent-and-eval-with-{model_name}.png"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(input_file_path)

# Filter rows: keep only the two agent variants and the chosen model and exams ending with -100
summaries = summaries[summaries["agent_name"].isin(agent_names)]
summaries = summaries[summaries["model_name"] == model_name]
summaries = summaries[summaries["eval_name"].str.endswith("-100")]

# Create a grouped bar plot
sns.set_style("whitegrid")
plt.figure(figsize=(14, 6))
ax = sns.barplot(
    x="eval_name",
    y="total_steps",
    hue="agent_name",
    data=summaries)
plt.title(f"Total steps by agent and eval with {model_name}")
plt.xlabel("Eval")
plt.ylabel("Total steps")
plt.xticks(rotation=10, ha='right')
plt.subplots_adjust(bottom=0.25)
plt.legend(title="Agent")
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
plt.savefig(f"{output_folder_path}/{output_file_name}", bbox_inches='tight')
plt.show()