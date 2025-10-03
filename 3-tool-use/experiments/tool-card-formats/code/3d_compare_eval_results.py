import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters
model_name = "gpt-4.1-mini"
eval_size = 100
results_folder_path = "../data/results/"
results_a_file_name = "react-v1 - gpt-4.1-mini - simple-qa-100.csv"
results_b_file_name = "react-v1c - gpt-4.1-mini - simple-qa-100.csv"
results_a_file_path = f"{results_folder_path}/{results_a_file_name}"
results_b_file_path = f"{results_folder_path}/{results_b_file_name}"

# Load the data into a single dataframe joined on episode_id
results_a = pd.read_csv(results_a_file_path)
results_b = pd.read_csv(results_b_file_path)
results = results_a.merge(
    results_b,
    on="episode_id",
    suffixes=("_a", "_b"))

# Keep only rows where either reward_a or reward_b are zero
results = results[(results["reward_a"] == 0) | (results["reward_b"] == 0)]

# Keep only rows where the reward_a is different from reward_b
results = results[results["reward_a"] != results["reward_b"]]

# Keep only relevant columns
results = results[[
    "episode_id",
    "question_a",
    "correct_answer_a",
    "agent_answer_a",
    "agent_answer_b",
    "reward_a",
    "reward_b"]]