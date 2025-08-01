import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set manual parameters
model_name = "gpt-4.1-mini"
eval_name = "gaia-test-10"

# Load the summaries CSV file
results_file_path = "../data/summaries.csv"
results = pd.read_csv(results_file_path)

# Filter rows
results = results[results["model_name"] == model_name]
results = results[results["eval_name"] == eval_name]

# Plot the accuracy by agent
plt.figure(figsize=(10, 6))
sns.barplot(
    x="agent_name",
    y="accuracy",
    data=results)
plt.title(f"Accuracy by agent for {model_name} model on {eval_name} eval")
plt.xlabel("Agent")
plt.ylabel("Accuracy")
plt.ylim(0.0, 1.0)
plt.savefig(f"../data/plots/accuracy-by-agent-for-{model_name}-on-{eval_name}.png")
plt.show()