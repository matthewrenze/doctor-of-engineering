import os
import pandas as pd
from summaries.summary_manager import SummaryManager

# Set paths
results_folder_path = "../data/results"
summary_file_path = "../data/summaries.csv"

# Create components
summary_manager = SummaryManager()

# Delete the summaries file if it exists
if os.path.exists(summary_file_path):
    os.remove(summary_file_path)

# Load results
all_results = pd.DataFrame()
results_files_names = os.listdir(results_folder_path)
for file_name in results_files_names:
    if not file_name.endswith(".csv"):
        continue
    file_path = results_folder_path + "/" + file_name
    results = pd.read_csv(file_path)
    summary = summary_manager.summarize(results)
    summary_manager.append(summary)

