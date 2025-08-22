# Import libraries
import base64
import pandas as pd

# Set the parameters
source_file_path = "../data/raw/test-00000-of-00001.parquet"
target_folder_path = "../data/evals"
image_folder_path = "../data/evals/hle"
sizes = [1, 10, 100]

# Load the parquet file
eval = pd.read_parquet(source_file_path)

# Add the new columns
eval["source"] = "HLE"
eval["source_id"] = eval.index + 1
eval["subtopic"] = ""
eval["task"] = "Answer the following question:\n" + eval["question"]
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
    image_filepath = f"{image_folder_path}/{image_filename}"
    with open(image_filepath, "wb") as image_file:
        image_file.write(image_data)

    # Update the files column
    eval.at[index, "files"] = image_filename

# Keep only the relevant columns
eval = eval[[
    "source",
    "source_id",
    "topic",
    "task",
    "answer",
    "answer_type",
    "solution",
    "files"]]

# TODO: Need to randomize the rows

# Add the max rows to the sizes
max_rows = eval.shape[0]
sizes.append(max_rows)

for size in sizes:
    target_file_name = f"hle-{size}.csv"
    target_file_path = f"{target_folder_path}/{target_file_name}"

    # Select the first n rows
    eval_subset = eval.head(size)

    # Save the exam
    eval_subset.to_csv(target_file_path, index=False, encoding="utf-8")

    # Print status update
    print(f"Created {target_file_name} with {len(eval_subset)} entries.")




