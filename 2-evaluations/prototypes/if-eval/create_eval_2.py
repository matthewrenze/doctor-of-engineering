# Import libraries
import os
import json
import pandas as pd

# Set the file paths
input_file_path = "input_data.jsonl"
output_file_path = "output_data.csv"

instructions_to_keep = [

]

# Load the JSON data
input_lines = []
with open(input_file_path, "r") as file:
    for line in file:
        json_line = json.loads(line.strip())
        input_lines.append(json_line)

output_table = pd.DataFrame(columns=["key", "prompt"])
for json_line in input_lines:

    # Keep only single-instruction tasks
    instruction_ids = json_line["instruction_id_list"]
    num_instructions = len(instruction_ids)
    if num_instructions > 1:
        continue

    # Get the fields
    key = json_line["key"]
    prompt = json_line["prompt"]

    # Add the task to the new eval
    output_table = output_table._append(
        {"key": key,
         "prompt": prompt},
        ignore_index=True)

# Save the new eval
output_table.to_csv(output_file_path, index=False)



