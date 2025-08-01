import os
import shutil
from huggingface_hub import login
from datasets import load_dataset

# Authenticate with your Hugging Face token
token = os.getenv("HUGGINGFACE_TOKEN")
login(token=token)

# Set the output folder
# NOTE: Needs to be a short path due to path-length issue
output_folder = "C:/GAIA"

# Load the GAIA dataset
dataset = load_dataset(
    path="gaia-benchmark/GAIA",
    name="2023_all",
    trust_remote_code=True,
    cache_dir=output_folder)

# Set the output file paths
val_file_path = os.path.join(output_folder, "gaia_val.csv")
test_file_path = os.path.join(output_folder, "gaia_test.csv")

# Save the dataset to a local directory as a CSV file
dataset["validation"].to_csv(val_file_path, index=False, encoding="utf-8")
dataset["test"].to_csv(test_file_path, index=False, encoding="utf-8")

# Set the folder paths
val_folder_base = "C:/Users/Matthew/.cache/huggingface/hub/datasets--gaia-benchmark--GAIA/snapshots/897f2dfbb5c952b5c3c1509e648381f9c7b70316/2023/"
val_folder_in = os.path.join(val_folder_base, "validation")
test_folder_in = os.path.join(val_folder_base, "test")
val_folder_out = os.path.join(output_folder, "validation")
test_folder_out = os.path.join(output_folder, "test")

# Create the output folders
os.makedirs(val_folder_out, exist_ok=True)
os.makedirs(test_folder_out, exist_ok=True)

# Copy the files to the output folder
for filename in os.listdir(val_folder_in):
    source = os.path.join(val_folder_in, filename)
    target = os.path.join(val_folder_out, filename)
    shutil.copy2(source, target)

for filename in os.listdir(test_folder_in):
    source = os.path.join(test_folder_in, filename)
    target = os.path.join(test_folder_out, filename)
    shutil.copy2(source, target)

