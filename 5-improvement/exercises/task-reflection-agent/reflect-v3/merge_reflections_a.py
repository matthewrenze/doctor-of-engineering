import os

# Set the parameters
base_folder_path = "../data/reflections"
target_file_name = "all.txt"
source_agent_name = "reflect-v2-train"
target_agent_name = "reflect-v3a-train"
model_name = "gpt-5.2"
eval_names = [
    "tw-simple-1",
    "tw-treasure-1",
    "tw-treasure-2",
    "tw-treasure-3",
    "tw-coin-1",
    "tw-coin-2",
    "tw-coin-3",
    "tw-cooking-1",
    "tw-cooking-2",
    "tw-cooking-3",
]

for eval_name in eval_names:

    # Set the paths
    source_folder_path = f"{base_folder_path}/{source_agent_name} - {model_name} - {eval_name}"
    target_folder_path = f"{base_folder_path}/{target_agent_name} - {model_name} - {eval_name}"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder_path, exist_ok=True)

    # Delete the target file if it exists
    if os.path.exists(target_file_path):
        os.remove(target_file_path)

    # List the source files
    source_files = os.listdir(source_folder_path)

    # Merge the source files into the target file
    for source_file_name in source_files:

        # Get the source file path
        source_file_path = f"{source_folder_path}/{source_file_name}"

        # Read the content from the source file
        with open(source_file_path, 'r') as source_file:
            content = source_file.read()

        # Skip files with "N/A"
        if content.strip() == "N/A":
            continue

        # Append the content to the target file
        with open(target_file_path, 'a') as target_file:
            target_file.write(content)

    # If the target file does not exist, create an empty one
    if not os.path.exists(target_file_path):
        with open(target_file_path, 'w') as target_file:
            target_file.write("")


