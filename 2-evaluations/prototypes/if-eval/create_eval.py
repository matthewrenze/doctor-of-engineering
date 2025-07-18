# Import libraries
import os
import json

# Set the file paths
input_file_path = "input_data.jsonl"
output_file_path = "output_data.jsonl"

instructions_to_keep = [

]

# Load the JSON data
input_lines = []
with open(input_file_path, "r") as file:
    for line in file:
        json_line = json.loads(line.strip())
        input_lines.append(json_line)

# Get the unique instruction IDs
output_lines = []
for json_line in input_lines:
    instruction_ids = json_line["instruction_id_list"]

    # Count the number of instructions
    num_instructions = len(instruction_ids)
    if num_instructions > 1:
        continue

    instruction_id = json_line["instruction_id_list"][0]

    # Add the task to the new eval
    output_lines.append(json_line)

# Save the new eval
with open(output_file_path, "w") as file:
    for json_line in output_lines:
        file.write(json.dumps(json_line) + "\n")


print(output_lines[0])
print(output_lines[1])
print(output_lines[2])
print(output_lines[3])
print(output_lines[4])

# ---

# Get the unique instruction IDs
num_of_instructions = {}
unique_instruction_ids = {}
for json_line in output_lines:
    instruction_ids = json_line['instruction_id_list']
    instruction_id = instruction_ids[0]
    if instruction_id not in unique_instruction_ids:
        unique_instruction_ids[instruction_id] = 0
    unique_instruction_ids[instruction_id] += 1

# # Sort the unique instruction IDs
# unique_instruction_ids = sorted(unique_instruction_ids.keys())

# Print the unique instruction IDs
for instruction_id in unique_instruction_ids:
    print(f"{instruction_id} ({unique_instruction_ids[instruction_id]})")