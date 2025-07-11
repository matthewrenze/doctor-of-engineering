# Import libraries
import os
import json
import re
from problem_row import *

# Set the file paths
input_root_path = "../data/raw/gsm-8k"
output_root_path = "../data/clean"

# Specify the dataset mappings
dataset_mappings = {
    "train.jsonl": "train/gsm-8k.jsonl",
    # "train_socratic.jsonl": "train/gsm-8k-socratic.jsonl",
    "test.jsonl": "test/gsm-8k.jsonl",
    # "test_socratic.jsonl": "test/gsm-8k-socratic.jsonl"
}

# Loop through each input file
for dataset_mapping in dataset_mappings:

    # Display status update
    print(f'Creating {dataset_mapping[:-5]} ...')

    # Get the input file path
    input_file_path = input_root_path + "/" + dataset_mapping

    # Read the input file
    with open(input_file_path, 'r', encoding='utf8') as input_file:

        # Create a list of questions
        questions = []

        # Loop through each line of JSON
        for i, line in enumerate(input_file):

            # Get the row of JSON data
            row = json.loads(line.strip())

            # Create the question
            problem = ProblemRow()

            # Get the row of JSON data
            row = json.loads(line.strip())

            # Get the source file (exclude the ".jsonl")
            problem.source = f"gsm-8k/{dataset_mapping[:-6]}"

            # Get the source ID
            problem.source_id = i + 1

            # Get the topic
            problem.topic = "Math"

            # Get the question
            problem.question = row['question']

            # Get the answer
            # Note: Sometimes contains thousands separator but not always
            match = re.search(r'#### (.*)', row['answer'])
            correct_answer = match.group(1)
            correct_answer = correct_answer.replace(',', '')
            problem.answer = correct_answer

            # Get the solution
            solution = row['answer']
            solution = re.sub(r'<<[^>]*>>', '', solution)
            solution = re.sub(r'#### \d+', '', solution)
            problem.solution = solution

            # Add the question to the list
            questions.append(problem)

    # Create the output file path
    output_file_path = output_root_path + '/' + dataset_mappings[dataset_mapping]

    # Write the questions to the output file
    with open(output_file_path, 'w', encoding='utf8') as f:
        for problem in questions:
            json.dump(problem.__dict__, f)
            f.write('\n')

# Display status update
print('Done.')







