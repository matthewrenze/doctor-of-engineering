from io import StringIO
import pandas as pd

# Load the results CSV file
results_file_path = "../data/results/results-100.csv"
summary_file_path = "../data/results/summary-100.txt"
results = pd.read_csv(results_file_path)

# Compute summary statistics
task_count = len(results)
correct_tasks = results['reward'].sum()
total_score = results['reward'].sum()
accuracy = total_score / task_count
reward_per_task = total_score / task_count
reward_per_step = results['reward_per_step'].mean()
reward_per_token = results['reward_per_token'].mean()

# Create the report
output = StringIO()
output.write(f"Total Tasks: {task_count}\n")
output.write(f"Correct Tasks: {correct_tasks}\n")
output.write(f"Accuracy: {accuracy:.0%}\n")
output.write(f"Avg Reward per Task: {reward_per_task:.2f}\n")
output.write(f"Avg Reward per Step: {reward_per_step:.4f}\n")
output.write(f"Avg Reward per Token: {reward_per_token:.6f}\n")

# Save the results to file
with open(summary_file_path, "w") as f:
    f.write(output.getvalue())

# Print the results
print(output.getvalue())