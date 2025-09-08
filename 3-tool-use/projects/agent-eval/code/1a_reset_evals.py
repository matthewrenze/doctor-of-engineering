import os
import shutil

# Set paths
cache_folder_path = "../data/cache"
search_cache_folder_path = "../data/cache/search"
errors_folder_path = "../data/errors"
logs_folder_path = "../data/logs"
messages_folder_path = "../data/messages"
plots_folder_path = "../data/plots"
results_folder_path = "../data/results"
workspaces_folder_path = "../data/workspaces"
summaries_file_path = "../data/summaries.csv"

# Delete the files/folders
print("Deleting cache folder...")
shutil.rmtree(cache_folder_path)

print("Deleting errors folder...")
shutil.rmtree(errors_folder_path)

print("Deleting logs folder...")
shutil.rmtree(logs_folder_path)

print("Deleting messages folder...")
shutil.rmtree(messages_folder_path)

print("Deleting plots folder...")
shutil.rmtree(plots_folder_path)

print("Deleting results folder...")
shutil.rmtree(results_folder_path)

print("Deleting workspaces folder...")
shutil.rmtree(workspaces_folder_path)

print("Deleting summaries file...")
os.remove(summaries_file_path)

# Recreate the folders
print("Recreating folders...")
os.makedirs(cache_folder_path, exist_ok=True)
os.makedirs(search_cache_folder_path, exist_ok=True)
os.makedirs(errors_folder_path, exist_ok=True)
os.makedirs(logs_folder_path, exist_ok=True)
os.makedirs(messages_folder_path, exist_ok=True)
os.makedirs(plots_folder_path, exist_ok=True)
os.makedirs(results_folder_path, exist_ok=True)
os.makedirs(workspaces_folder_path, exist_ok=True)


