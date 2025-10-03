import os
import shutil

# Set paths
source_folder_path = "../../create-evals/data/evals"
target_folder_path = "../data/evals"

# Create the target folder
os.makedirs(target_folder_path, exist_ok=True)

# Copy the contents of the source folder to the target folder
for item_name in os.listdir(source_folder_path):
    source_item_path = source_folder_path + "/" + item_name
    target_item_path = target_folder_path + "/" + item_name

    if os.path.isdir(source_item_path):
        shutil.copytree(source_item_path, target_item_path, dirs_exist_ok=True)
        print(f"Copied folder: {item_name}")
    else:
        shutil.copy2(source_item_path, target_item_path)
        print(f"Copied file: {item_name}")