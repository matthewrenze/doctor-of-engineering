# Import libraries
import os
import ast
import pandas as pd

# Set the parameters
random_seed = 42
source_file_path = "../data/raw/simple-qa/simple_qa_test_set.csv"
target_folder_path = "../data/evals/simple-qa"
target_file_path = "../data/evals/simple-qa/simple-qa.jsonl"
sizes = [1, 10, 100]

# Create the target folder
os.makedirs(target_folder_path, exist_ok=True)

# Load the csv file
source_eval = pd.read_csv(source_file_path)

# Create target eval
target_eval = pd.DataFrame()

# Randomize the rows
source_eval = source_eval.sample(frac=1, random_state=random_seed)
# source_eval = source_eval.reset_index(drop=True)

# Loop through rows
for index, row in source_eval.iterrows():

    # Get the fields
    metadata_json = row["metadata"]
    metadata = ast.literal_eval(metadata_json)
    topic = metadata["topic"]
    question = row["problem"]
    answer = row["answer"]
    answer_type = metadata["answer_type"]
    urls = metadata["urls"]
    solution = "The answer is found by combining information from the following URLs: " + ", ".join(urls)

    # Create a new row for the target eval
    new_row = {
        "source": "simple-qa",
        "source_id": int(index),
        "topic": topic,
        "question": question,
        "answer": answer,
        "solution": solution,
        "files": ""
    }

    # Append the new row to the target eval
    target_eval = target_eval._append(new_row, ignore_index=True)

# Add the max rows to the sizes
max_rows = source_eval.shape[0]
sizes.append(max_rows)

# Create the eval sets
for size in sizes:

    target_file_name = f"simple-qa-{size}.jsonl"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Select the first n rows
    target_eval_subset = target_eval.head(size)

    # Save the exam
    target_eval_subset.to_json(target_file_path, orient="records", lines=True, force_ascii=False)

    # Print status update
    print(f"Created {target_file_name} with {len(target_eval_subset)} entries.")


