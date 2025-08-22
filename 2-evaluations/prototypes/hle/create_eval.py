import base64
import pandas as pd

# Load the parquet file
eval = pd.read_parquet("test-00000-of-00001.parquet")

# Add the new columns
eval["source"] = "HLE"
eval["source_id"] = eval.index + 1
eval["subtopic"] = ""
eval["files"] = ""

# Convert answer type
eval["answer_type"] = eval["answer_type"].replace({
    "exactMatch": "exact match",
    "multipleChoice": "multiple choice"})

# Rename the columns
eval = eval.rename(columns={
    "question": "problem",
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
    image_filepath = f"files/{image_filename}"
    with open(image_filepath, "wb") as image_file:
        image_file.write(image_data)

    # Update the files column
    eval.at[index, "files"] = image_filename

# Keep only the relevant columns
eval = eval[[
    "source",
    "source_id",
    "topic",
    "problem",
    "answer",
    "answer_type",
    "solution",
    "files"]]

# Save the exam to csv
eval.to_csv("hle.csv", index=False)