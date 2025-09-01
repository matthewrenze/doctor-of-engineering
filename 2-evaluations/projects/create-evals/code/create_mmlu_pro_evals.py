import os
import pandas as pd

# Set the parameters
random_seed = 42
source_file_path = "../data/raw/mmlu-pro/test-00000-of-00001.parquet"
target_folder_path = "../data/evals/mmlu-pro"
sizes = [1, 10, 100]

# Create the target folders
os.makedirs(target_folder_path, exist_ok=True)

# Load the parquet file
raw_eval = pd.read_parquet(source_file_path)

# Copy the eval
eval = raw_eval.copy()

# Add the new columns
eval["source"] = "mmlu-pro"
eval["source_id"] = "id"
eval["topic"] = eval["category"]
eval["choices"] = dict()
eval["solution"] = ""
eval["files"] = ""

# Convert options to a dictionary (A-J)
for index, row in eval.iterrows():
    options = row["options"]
    options_dict = {chr(65 + i): option for i, option in enumerate(options)}
    eval.at[index, "choices"] = options_dict

# Keep only the relevant columns
eval = eval[[
    "source",
    "source_id",
    "topic",
    "question",
    "choices",
    "answer",
    "solution",
    "files"
]]

# Randomize the rows
eval = eval.sample(frac=1, random_state=random_seed)

# Reset the index
eval = eval.reset_index(drop=True)
eval.insert(0, "id", eval.index + 1)

# Add the max rows to the sizes
max_rows = eval.shape[0]
sizes.append(max_rows)

for size in sizes:

    target_file_name = f"mmlu-pro-{size}.jsonl"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Select the first n rows
    target_eval_subset = eval.head(size)

    # Save the exam
    target_eval_subset.to_json(target_file_path, orient="records", lines=True, force_ascii=False)

    # Print status update
    print(f"Created {target_file_name} with {len(target_eval_subset)} entries.")