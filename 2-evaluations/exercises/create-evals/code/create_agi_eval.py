# Import libraries
import os
import json
from problem_row import ProblemRow

# Set the file paths
input_folder_path = "../data/raw/agi-eval"
output_folder_path = "../data/clean"

# Specify the file names to process
# NOTE: Excluding all Chinese-language files
# NOTE: Removing math.jsonl because it isn't multiple choice
# NOTE: Split data in half for train and test sets
input_file_names_and_topics = {
    "aqua-rat.jsonl": "Math",
    # "logiqa-en.jsonl": "Logic",
    # "lsat-ar.jsonl": "Law",
    # "lsat-lr.jsonl": "Law",
    # "lsat-rc.jsonl": "Law",
    # "sat-en.jsonl": "English",
    # "sat-math.jsonl": "Math"
}

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through each input file
for input_file_name in input_file_names_and_topics:

    # Display status update
    print(f"Creating {input_file_name[:-5]} ...")

    # Get the input file path
    input_file_path = input_folder_path + "/" + input_file_name

    # Read the file
    with open(input_file_path, "r", encoding="utf8") as input_file:
        problem_lines = input_file.readlines()

    # Create a list of problem sets
    problem_sets = [
        ("train", problem_lines[:len(problem_lines) // 2]),
        ("test", problem_lines[len(problem_lines) // 2:])]

    # Loop through each problem set
    source_id = 0
    for problem_set in problem_sets:

        # Loop through each line
        problems = []
        for line in problem_set[1]:

            # Create the problem
            problem = ProblemRow()

            # Get the row of JSON data
            row = json.loads(line.strip())

            # Get the source file (exclude the ".jsonl")
            problem.source = f"agi-eval/{input_file_name[:-6]}"

            # Get the source ID
            problem.source_id = source_id + 1

            # Get the topic
            problem.topic = input_file_names_and_topics[input_file_name]

            # Get the passage (i.e. part before the question)
            if row.get("passage") is not None and row["passage"] != "":
                problem.context = row["passage"]

            # Get the question
            if row.get("question") is not None:
                problem.question = row["question"]

            # Get the choices
            choices = {}
            if row.get("options") is not None:
                options = row["options"]
                choices = {}
                for option in options:
                    letter = option[1:2]
                    answer = option[3:]
                    choices[letter] = answer

            # Get the label (i.e. multiple-choice answer)
            if row.get("label") is not None:
                label = row["label"]
                problem.answer = choices[label]

            # Get the answer (i.e. exact text answer)
            if row.get("answer") is not None:
                problem.answer = row["answer"]

            # Get the solution
            if row.get("other") is not None:
                problem.solution = row["other"]["solution"]

            # Add the problem to the list
            problems.append(problem)

            source_id += 1

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        # Create the output file path
        output_file_name = input_file_name
        output_file_path = f"{output_folder_path}/{problem_set[0]}/{output_file_name}"

        # Write the questions to the output file
        with open(output_file_path, "w", encoding="utf8") as f:
            for problem in problems:
                json.dump(problem.__dict__, f)
                f.write("\n")

# Display status update
print("Done.")







