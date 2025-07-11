# Import libraries
import os
import json
import random

# Set a random seed
random.seed(42)

# Set the parameters
problem_sizes = [1, 10, 100, 1000, 10000]
problem_sets = ["train", "test"]

# Loop through each problem set
for problem_set in problem_sets:

    # Set the paths
    input_folder_path = f"../data/clean/{problem_set}"
    output_folder_path = f"../data/evals/{problem_set}"

    file_names = os.listdir(input_folder_path)
    file_paths = [f"{input_folder_path}/{file_name}" for file_name in file_names]
    for file_path in file_paths:

        # Loop through each problem set size
        for num_problems in problem_sizes:

            # Get the input file names
            input_file_names = os.listdir(input_folder_path)

            # DEBUG: Load only a single file
            # input_file_names = ["arc-challenge-test.jsonl"]

            # Loop through each input file
            for input_file_name in input_file_names:

                # If file is not a jsonl file, skip it
                if not input_file_name.endswith(".jsonl"):
                    continue

                # Display a status update
                print(f"Processing {problem_set}/{input_file_name} - {num_problems}")

                # Create a list of problems for the exam
                problems = []

                # Get the input file name
                input_file_path = f"{input_folder_path}/{input_file_name}"

                # Read the input file
                with open(input_file_path, "r", encoding="utf8") as input_file:

                    # Loop through each line
                    for line in input_file:

                        # Add the problem
                        problems.append(line)

                # Get the current number of problems
                current_num_problems = num_problems

                # If there are more problems than the size of the problem set
                if len(problems) > current_num_problems:

                    # Then, randomly sample n problems
                    problems = random.sample(problems, num_problems)
                else:
                    # Else, set the current number of problems to the max
                    current_num_problems = len(problems)

                # Create a list of output lines
                output_lines = []

                # Loop through each problem
                for i, line in enumerate(problems):

                    # Convert to problem to json
                    row = json.loads(line.strip())

                    # Add the id to the beginning of the json
                    line = json.dumps({"id": i + 1, **row}) + "\n"

                    # Add the problem to the output lines
                    output_lines.append(line)

                # Create output folder if it doesn't exist
                if not os.path.exists(output_folder_path):
                    os.makedirs(output_folder_path)

                # Create the output file path
                output_file_path = f"{output_folder_path}/{input_file_name[:-6]}-{current_num_problems}.jsonl"

                # Open the output file
                with open(output_file_path, "w", encoding="utf8") as output_file:

                    # Write the problems to the output file
                    for line in output_lines:
                        output_file.write(line)



