import os
import shutil

# Set file paths
file_paths = [
    "../data/summaries.csv",
]

# Set folder paths
folder_paths = [
    "../data/details",
    "../data/logs",
    "../data/messages",
    "../data/plots",
    "../data/results",
]

print("Resetting eval data ...")

print("Deleting files ...")
for file_path in file_paths:
    if os.path.exists(file_path):
        print(f"Deleting: {file_path}...")
        os.remove(file_path)

# Delete folders
print("Deleting folders ...")
for folder_path in folder_paths:
    if os.path.exists(folder_path):
        print(f" - Deleting: {folder_path}")
        shutil.rmtree(folder_path, ignore_errors=True)


# Recreate the directories
print("Creating folders ...")
for folder_path in folder_paths:
    print(f" - Creating: {folder_path}")
    os.makedirs(folder_path, exist_ok=True)

print("Reset complete.")
