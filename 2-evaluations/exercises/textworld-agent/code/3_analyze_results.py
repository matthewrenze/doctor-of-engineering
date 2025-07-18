import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set default parameters
agent_name, model_name, eval_name = None, None, None

# Set manual parameters
# agent_name = "react"
model_name = "gpt-4.1-mini"
eval_name = "cooking-game-10"

# Load the summaries CSV file
results_file_path = "../data/summaries.csv"
results = pd.read_csv(results_file_path)

# Filter rows
if agent_name is not None:
    results = results[results["agent_name"] == agent_name]
if model_name is not None:
    results = results[results["model_name"] == model_name]
if eval_name is not None:
    results = results[results["eval_name"] == eval_name]

# Create filename
file_name = ""
file_name += f"{agent_name} - " if agent_name is not None else "all-agents - "
file_name += f"{model_name} - " if model_name is not None else "all-models - "
file_name += f"{eval_name} - " if eval_name is not None else "all-evals - "
file_name += "accuracy.png"

# Plot the accuracy by agent
if agent_name is None:
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="agent_name",
        y="accuracy",
        data=results)
    plt.title(f"Accuracy by Agent for {model_name} on {eval_name}")
    plt.xlabel("Agent")
    plt.ylabel("Accuracy")
    plt.ylim(0.0, 1.0)
    plt.savefig(f"../data/plots/{file_name}")
    plt.show()


# Plot the accuracy by model
if model_name is None:
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="model_name",
        y="accuracy",
        data=results)
    plt.title(f"Accuracy by Model for {agent_name} on {eval_name}")
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.ylim(0.0, 1.0)
    plt.savefig(f"../data/plots/{file_name}")
    plt.show()
