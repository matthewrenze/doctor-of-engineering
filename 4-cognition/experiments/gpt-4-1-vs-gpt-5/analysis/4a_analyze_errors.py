import os
import pandas as pd

# Set parameters
model_name = "gpt-4.1-mini"
input_folder_path = "../data/results"

# Load results
all_results = pd.DataFrame()
file_names = os.listdir(input_folder_path)
for file_name in file_names:
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder_path, file_name)
        result = pd.read_csv(file_path)
        all_results = pd.concat([all_results, result], ignore_index=True)

# Filter by parameters
results = all_results[all_results["model_name"] == model_name]
results = results[results["eval_name"].str.startswith("tw-")]

# Filter by errors (not NaN)
results = results[results["error"].notnull()]



