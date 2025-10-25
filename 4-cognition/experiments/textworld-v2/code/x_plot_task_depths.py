import os
import json
import pandas as pd

# Set paths
# eval_name = "tw-simple"
# eval_name = "tw_coin"
# eval_name = "tw-treasure"
eval_name = "tw-cooking"
input_folder_path = f"../data/evals/{eval_name}"
plot_folder_path = f"../data/plots/task-depths"
plot_file_path = f"{plot_folder_path}/{eval_name}-task-depths.png"
output_file_path = f"../data/{eval_name}-task-depths.csv"

# Create the folders
os.makedirs(plot_folder_path, exist_ok=True)

# Get the JSON files
file_names = os.listdir(input_folder_path)

# Create dataframe
table = pd.DataFrame(columns=["file_name", "level", "sublevel", "game_depth", "walkthrough"])

for file_name in file_names:

    # Exclude non-JSON files
    if not file_name.endswith(".jsonl"):
        continue

    # Get the file path
    file_path = input_folder_path + "/" + file_name

    # Read the JSONL file (one JSON object per line)
    with open(file_path, "r", encoding="utf-8") as f:
        tasks = [json.loads(line) for line in f if line.strip()]

    for task in tasks:

        # Get the metadata
        task_id = task["id"]
        level = task["level"]
        sublevel = task["sublevel"]
        solution = task["solution"]
        task_depth = task["solution_steps"]

        # Append to the dataframe
        table = table._append({
            "file_name": file_name,
            "level": level,
            "sublevel": sublevel,
            "task_depth": task_depth,
            "solution": solution
        }, ignore_index=True)

        print(f"{file_name}-{task_id}: {task_depth}")
        print(f" - Depth: {task_depth}")
        print(f" - Solution: {solution}")
        print()

# Group by level and sublevel to get average depth
grouped_table = table.groupby(["level", "sublevel"]).agg(
    average_depth=pd.NamedAgg(column="task_depth", aggfunc="mean"),
    count=pd.NamedAgg(column="task_depth", aggfunc="count")
).reset_index()

# Plot the results
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_table, x="level", y="average_depth", hue="sublevel")
plt.title(f"Average Task Depth by Level and Sublevel for {eval_name}")
plt.xlabel("Level")
plt.ylabel("Average task depth")
plt.legend(title="Sublevel")
plt.savefig(plot_file_path)
plt.show()

# Save grouped table to CSV
grouped_table.to_csv(output_file_path, index=False)

