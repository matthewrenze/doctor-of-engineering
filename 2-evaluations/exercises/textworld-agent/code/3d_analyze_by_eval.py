import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set manual parameters
agent_name = "react"
model_name = "gpt-4.1-mini"
num_tasks = 10

# Load the summaries CSV file
results_file_path = "../data/summaries.csv"
results = pd.read_csv(results_file_path)

# Filter rows
results = results[results["agent_name"] == agent_name]
results = results[results["model_name"] == model_name]
results = results[results["tasks"] == num_tasks]

# Plot the accuracy by agent
plt.figure(figsize=(10, 6))
sns.barplot(
    x="eval_name",
    y="accuracy",
    data=results)
plt.title(f"Accuracy by eval for {agent_name} agent using {model_name} model")
plt.xlabel("Eval")
plt.ylabel("Accuracy")
plt.ylim(0.0, 1.0)
plt.savefig(f"../data/plots/accuracy-by-eval-for-{agent_name}-with-{model_name}.png")
plt.show()