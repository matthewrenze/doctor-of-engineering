# Import libraries
import os
import pandas as pd
import random

# Set the parameters
random_seed = 42
source_file_path = "../data/raw/gpqa/gpqa_diamond.csv"
target_folder_path = "../data/evals/gpqa"
sizes = [1, 10, 100]

# Set the random seed
random.seed(random_seed)

# Create the target folders
os.makedirs(target_folder_path, exist_ok=True)

# Load the csv file
raw_eval = pd.read_csv(source_file_path)

# Copy the eval
eval = raw_eval.copy()

# Add the new columns
eval["source"] = "gpqa"
eval["source_id"] = eval.index + 1
eval["files"] = ""

# Create the multiple choice answer options
choices_list = []
answer_list = []
letters = ["A", "B", "C", "D"]

for _, row in eval.iterrows():
    answers = [
        ("correct", row["Correct Answer"]),
        ("incorrect", row["Incorrect Answer 1"]),
        ("incorrect", row["Incorrect Answer 2"]),
        ("incorrect", row["Incorrect Answer 3"]),
    ]
    random.shuffle(answers)

    mapping = {letter: ans for letter, (_, ans) in zip(letters, answers)}
    correct_letter = [letter for letter, (kind, _) in zip(letters, answers) if kind == "correct"][0]

    choices_list.append(mapping)
    answer_list.append(correct_letter)

eval["choices"] = choices_list
eval["answer"] = answer_list

# Rename the columns
eval = eval.rename(columns={
    "High-level domain": "topic",
    "Subdomain": "subtopic",
    "Question": "question",
    "Explanation": "solution"
})

# Keep only the necessary columns
eval = eval[[
    "source",
    "source_id",
    "topic",
    "subtopic",
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

    target_file_name = f"gpqa-diamond-{size}.jsonl"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Select the first n rows
    eval_subset = eval.head(size)

    # Save the exam
    eval_subset.to_json(target_file_path, orient="records", lines=True, force_ascii=False)

    # Print status update
    print(f"Created {target_file_name} with {len(eval_subset)} entries.")
