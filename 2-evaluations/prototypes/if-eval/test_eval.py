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

print(json_lines[0])
print(json_lines[1])
print(json_lines[2])
print(json_lines[3])
print(json_lines[4])