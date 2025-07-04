import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the summaries CSV file
results_file_path = "../data/summaries.csv"
results = pd.read_csv(results_file_path)

# Filter rows
# results = results[results["agent_name"] == "baseline"]
results = results[results["model_name"] == "gpt-4.1-mini"]
results = results[results["eval_name"] == "hotpotqa-10"]

# Plot the accuracy by agent
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(
    x="agent_name",
    y="accuracy",
    data=results)
plt.title("Accuracy by Agent")
plt.xlabel("Agent")
plt.ylabel("Accuracy")
plt.show()

