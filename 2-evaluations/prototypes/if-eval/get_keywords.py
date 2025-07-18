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
keywords = {}
for json_line in json_lines:
    instruction_ids = json_line['instruction_id_list']

    for kwargs_row in json_line["kwargs"]:
        for kwarg in kwargs_row:
            if kwarg is None:
                continue

            key = kwarg
            value = kwargs_row[kwarg]
            key_value = f"{key} - {value}"

            if key_value not in keywords:
                keywords[key_value] = 0

            keywords[key_value] += 1

            # print(f"{kwarg} - {kwargs_row[kwarg]}")

# Print the keywords and their values and counts in hierachical sorted order
for key in sorted(keywords.keys()):
    if (keywords[key] <= 1):
        continue
    print(f"{key} ({keywords[key]}):")
