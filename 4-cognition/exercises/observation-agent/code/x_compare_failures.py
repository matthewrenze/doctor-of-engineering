import pandas as pd

# Set paths
agent_name_a = "react-v0"
agent_name_b = "react-v1"
model_name = "gpt-4.1-mini"
eval_name = "tw-cooking-100"
results_folder_path = "../data/results"
results_file_name_a = f"{agent_name_a} - {model_name} - {eval_name}.csv"
results_file_name_b = f"{agent_name_b} - {model_name} - {eval_name}.csv"
results_file_path_a = f"{results_folder_path}/{results_file_name_a}"
results_file_path_b = f"{results_folder_path}/{results_file_name_b}"

# Read files
results_a = pd.read_csv(results_file_path_a)
results_b = pd.read_csv(results_file_path_b)

# Join tables
results = results_a.merge(
    results_b,
    on=["model_name", "eval_name", "episode_id"],
    suffixes=("_v0", "_v1"))

# Keep relevant columns
results = results[[
    "episode_id",
    "reward_v0",
    "reward_v1",
    "steps_v0",
    "steps_v1"]]

# Keep rows where v0 performed better than v1
failures = results[(results["reward_v0"] > results["reward_v1"])]