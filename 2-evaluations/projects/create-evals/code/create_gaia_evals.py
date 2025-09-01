# Import libraries
import os
import shutil
import ast
import pandas as pd

# Set the parameters
random_seed = 42
source_file_path = "../data/raw/gaia/gaia_val.csv"
target_folder_path = "../data/evals/gaia"
source_files_folder_path = "../data/raw/gaia/files"
target_files_folder_path = "../data/evals/gaia/files"
sizes = [1, 10, 100]

# Create the target files folders
os.makedirs(target_folder_path, exist_ok=True)
os.makedirs(target_files_folder_path, exist_ok=True)

# Copy the source files to the target files folder
for filename in os.listdir(source_files_folder_path):
    source_file = os.path.join(source_files_folder_path, filename)
    target_file = os.path.join(target_files_folder_path, filename)
    shutil.copy2(source_file, target_file)

# Load the csv file
source_eval = pd.read_csv(source_file_path)

# Create target eval
target_eval = pd.DataFrame()

# Randomize the rows
source_eval = source_eval.sample(frac=1, random_state=random_seed)
# source_eval = source_eval.reset_index(drop=True)

# Add the max rows to the sizes
max_rows = source_eval.shape[0]
sizes.append(max_rows)

# Loop through rows
for index, row in source_eval.iterrows():

    # Get the solution
    metadata = row["Annotator Metadata"]
    metadata_dict = ast.literal_eval(metadata)
    solution = metadata_dict["Steps"]

    # Create a new row for the target eval
    new_row = {
        "source": "gaia",
        "source_id": int(index),
        "topic": "general",
        "question": row["Question"],
        "answer": row["Final answer"],
        "solution": solution,
        "files": row["file_name"]
    }

    # Append the new row to the target eval
    target_eval = target_eval._append(new_row, ignore_index=True)

# Clean up the files column
target_eval["files"] = target_eval["files"].fillna("")
target_eval = target_eval.reset_index(drop=True)
target_eval.insert(0, "id", target_eval.index + 1)

for size in sizes:

    target_file_name = f"gaia-{size}.jsonl"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Select the first n rows
    target_eval_subset = target_eval.head(size)

    # Save the exam
    target_eval_subset.to_json(target_file_path, orient="records", lines=True, force_ascii=False)

    # Print status update
    print(f"Created {target_file_name} with {len(target_eval_subset)} entries.")




