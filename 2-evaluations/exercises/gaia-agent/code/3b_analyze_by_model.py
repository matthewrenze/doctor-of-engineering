import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set manual parameters
agent_name = "react"
eval_name = "gaia-test-10"

# Load the summaries CSV file
results_file_path = "../data/summaries.csv"
results = pd.read_csv(results_file_path)

# Filter rows
results = results[results["agent_name"] == agent_name]
results = results[results["eval_name"] == eval_name]

# Plot the accuracy by agent
plt.figure(figsize=(10, 6))
sns.barplot(
    x="model_name",
    y="accuracy",
    data=results)
plt.title(f"Accuracy by model for {agent_name} agent on {eval_name} eval")
plt.xlabel("Agent")
plt.ylabel("Accuracy")
plt.ylim(0.0, 1.0)
plt.savefig(f"../data/plots/accuracy-by-model-for-{agent_name}-on-{eval_name}.png")
plt.show()