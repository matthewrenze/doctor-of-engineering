import os
import json
import pandas as pd

# Set paths
input_folder_path = "../data/evals/tw-curriculum/files"
output_file_path = "../data/task-depths.csv"

# Get the JSON files
file_names = os.listdir(input_folder_path)

# Create dataframe
table = pd.DataFrame(columns=["file_name", "level", "sublevel", "game_depth", "walkthrough"])

for file_name in file_names:

    # Exclude non-JSON files
    if not file_name.endswith(".json"):
        continue

    # Get the file path
    file_path = input_folder_path + "/" + file_name

    # Read the JSON file
    with open(file_path, 'r') as f:
        game_data = json.load(f)

    # Get the level and sublevel from the file name
    parts = file_name.replace(".json", "").split("-")
    level = int(parts[2])
    sublevel = int(parts[3])

    # Get the game depth
    metadata = game_data.get("metadata")
    walkthrough = metadata.get("walkthrough")

    # Hack: Remove any consecutive drop actions after the "examine cookbook" step
    # to avoid counting unnecessary drops from distractors in inventory
    filtered_walkthrough = []
    filter_on = False

    for action in walkthrough:
        # Always include "examine cookbook" and activate filter
        if action == "examine cookbook":
            filtered_walkthrough.append(action)
            filter_on = True
            continue

        # Skip "drop" actions while the filter is active
        if filter_on and action.startswith("drop"):
            continue

        # Turn filter off once we hit a non-drop action
        if filter_on and not action.startswith("drop"):
            filter_on = False

        # Normal operation (add action)
        filtered_walkthrough.append(action)

    game_depth = len(filtered_walkthrough)

    # Append to the dataframe
    table = table._append({
        "file_name": file_name,
        "level": level,
        "sublevel": sublevel,
        "game_depth": game_depth,
        "walkthrough": walkthrough
    }, ignore_index=True)

    print(f"{file_name}: {game_depth}")
    print(f" - Depth: {game_depth}")
    print(f" - Walkthrough: {walkthrough}")
    print()

# Group by level and sublevel to get average depth
grouped_table = table.groupby(["level", "sublevel"]).agg(
    average_depth=pd.NamedAgg(column="game_depth", aggfunc="mean"),
    count=pd.NamedAgg(column="game_depth", aggfunc="count")
).reset_index()

# Plot the results
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_table, x="level", y="average_depth", hue="sublevel")
plt.title("Average Game Depth by Level and Sublevel")
plt.xlabel("Level")
plt.ylabel("Average Game Depth")
plt.legend(title="Sublevel")
plt.savefig("../data/task-depths.png")
plt.show()

# Save grouped table to CSV
grouped_table.to_csv(output_file_path, index=False)

