# Create the HotpotQA evals
import random
import json

# Set random seed
random.seed(42)

# Set file paths
input_file_path = "../data/evals/raw/hotpot_train_v1.1_simplified.json"
output_folder_path = "../data/evals"

# Load the data
with open(input_file_path, "r") as infile:
    data = json.load(infile)

# Count the number of items
num_items = len(data)

# Shuffle the data
random.shuffle(data)

# Set the bach sizes
batch_sizes = [1, 10, 100, 1000]

# Create batches of data
for batch_size in batch_sizes:

    # Create the output file path
    output_file_name = f"hotpotqa-{batch_size}.jsonl"
    output_file_path = f"{output_folder_path}/{output_file_name}"

    # Select the batch
    batch_data = data[:batch_size]
    
    # Save the data
    with open(output_file_path, "w") as outfile:
        for item in batch_data:
            json.dump(item, outfile)
            outfile.write("\n")

    print(f"Created {output_file_name}")