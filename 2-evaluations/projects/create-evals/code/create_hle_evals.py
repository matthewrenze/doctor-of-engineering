# NOTE: We're replacing the bio/chem questions with the HLE gold bio/chem questions.

# Import libraries
import os
import base64
import pandas as pd

# Set the parameters
random_seed = 42
source_file_path = "../data/raw/hle/test-00000-of-00001.parquet"
bio_chem_path = "../data/raw/hle/hle-gold-bio-chem.parquet"
target_folder_path = "../data/evals/hle"
target_files_folder_path = "../data/evals/hle/files"
sizes = [1, 10, 100]

# Create the target folders
os.makedirs(target_folder_path, exist_ok=True)
os.makedirs(target_files_folder_path, exist_ok=True)

# Load the parquet file
raw_eval = pd.read_parquet(source_file_path)
bio_chem = pd.read_parquet(bio_chem_path)

# Copy the eval
eval = raw_eval.copy()

# Delete all questions in eval with a matching bio/chem id
eval = eval[~eval["id"].isin(bio_chem["id"])]

# Append the gold bio/chem questions to eval
eval = pd.concat([eval, bio_chem], ignore_index=True)

# Add the new columns
eval["source"] = "hle"
eval["source_id"] = eval["id"]
eval["subtopic"] = ""
eval["files"] = ""

# Convert answer type
eval["answer_type"] = eval["answer_type"].replace({
    "exactMatch": "exact match",
    "multipleChoice": "multiple choice"})

# Rename the columns
eval = eval.rename(columns={
    "rationale": "solution",
    "raw_subject": "topic"})

# Loop through the rows
for index, row in eval.iterrows():

    # Get the image data
    id = row["id"]
    image_data = row["image"]

    # Skip if the image data is empty
    if pd.isna(image_data) or image_data == "":
        continue

    # Save the image
    metadata_part = image_data.split(",")[0]
    base64_part = image_data.split(",")[1]
    image_data = base64.b64decode(base64_part)
    image_file_ext = metadata_part.split(";")[0].split("/")[1]
    image_filename = f"{id}.{image_file_ext}"
    image_filepath = f"{target_files_folder_path}/{image_filename}"
    with open(image_filepath, "wb") as image_file:
        image_file.write(image_data)

    # Update the files column
    eval.at[index, "files"] = image_filename

# Keep only the relevant columns
eval = eval[[
    "source",
    "source_id",
    "topic",
    "question",
    "answer",
    "answer_type",
    "solution",
    "files"]]

# Randomize the rows
eval = eval.sample(frac=1, random_state=random_seed)

# Reset the index
eval = eval.reset_index(drop=True)
eval.insert(0, "id", eval.index + 1)

# Add the max rows to the sizes
max_rows = eval.shape[0]
sizes.append(max_rows)

for size in sizes:

    target_file_name = f"hle-{size}.jsonl"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Select the first n rows
    eval_subset = eval.head(size)

    # Save the exam
    eval_subset.to_json(target_file_path, orient="records", lines=True, force_ascii=False)

    # Print status update
    print(f"Created {target_file_name} with {len(eval_subset)} entries.")




