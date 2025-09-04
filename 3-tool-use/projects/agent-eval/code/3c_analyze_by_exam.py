import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
agent_name = "react"
model_name = "gpt-4.1-mini"
input_file_path = "../data/summaries.csv"
output_folder_path = "../data/plots/accuracy-by-exam"
output_file_name = f"accuracy-by-exam-for-{agent_name}-with-{model_name}.png"

# Create the output folder
os.makedirs(output_folder_path, exist_ok=True)

# Load the data
summaries = pd.read_csv(input_file_path)

# Filter rows
summaries = summaries[summaries["agent_name"] == agent_name]
summaries = summaries[summaries["model_name"] == model_name]
summaries = summaries[summaries["eval_name"].str.endswith("-100")]

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(
    x="eval_name",
    y="accuracy",
    data=summaries)
plt.title(f"Accuracy by eval for {agent_name} agent with {model_name} model")
plt.xlabel("Eval")
plt.ylabel("Accuracy")
plt.xticks(rotation=10, ha='right')
plt.subplots_adjust(bottom=0.15)
plt.ylim(0.0, 1.0)
plt.savefig(f"{output_folder_path}/{output_file_name}")
plt.show()