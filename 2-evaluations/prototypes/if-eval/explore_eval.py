# Import libraries
import os
import json

# Set the file paths
input_file_path = 'input_data.jsonl'

# Load the JSON data
json_lines = []
with open(input_file_path, 'r') as file:
    for line in file:
        json_line = json.loads(line.strip())
        json_lines.append(json_line)

# Inspect the eval tasks
print(json_lines[0])
print(json_lines[1])
print(json_lines[2])
print(json_lines[3])
print(json_lines[4])

# Get the unique instruction IDs
num_of_instructions = {}
unique_instruction_ids = []
for json_line in json_lines:
    instruction_ids = json_line['instruction_id_list']

    # Count the number of instructions
    num_instructions = len(instruction_ids)
    if num_instructions in num_of_instructions:
        num_of_instructions[num_instructions] += 1
    else:
        num_of_instructions[num_instructions] = 1

    # Collect unique instruction IDs
    for instruction_id in instruction_ids:
        if instruction_id not in unique_instruction_ids:
            unique_instruction_ids.append(instruction_id)

# Print the number of instructions
print("Number of instructions per task:")
for num, count in num_of_instructions.items():
    print(f"{num} instructions: {count} tasks")

# Sort the unique instruction IDs
unique_instruction_ids.sort()

# Print the unique instruction IDs
for instruction_id in unique_instruction_ids:
    print(instruction_id)