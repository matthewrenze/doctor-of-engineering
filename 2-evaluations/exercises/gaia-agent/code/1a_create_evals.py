# Import libraries
import ast
import pandas as pd

# Set the parameters
source_file_name = "../data/raw/gaia_val.csv"
target_folder_name = "../data/evals"
sizes = [1, 10, 100]

# Load the csv file
source_eval = pd.read_csv(source_file_name)

# Create target eval
target_eval = pd.DataFrame()

# TODO: Need to randomize the rows

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
        "id": int(index),
        "task": "Answer the following question:\n" + row["Question"],
        "answer": row["Final answer"],
        "solution": solution,
        "files": row["file_name"]
    }

    # Append the new row to the target eval
    target_eval = target_eval._append(new_row, ignore_index=True)

# Clean up the files column
target_eval["files"] = target_eval["files"].fillna("")

for size in sizes:
    target_file_name = f"gaia-{size}.csv"
    target_file_path = f"{target_folder_name}/{target_file_name}"

    # Select the first n rows
    target_eval_subset = target_eval.head(size)

    # Save the exam
    target_eval_subset.to_csv(target_file_path, index=False, encoding="utf-8")

    # Print status update
    print(f"Created {target_file_name} with {len(target_eval_subset)} entries.")




