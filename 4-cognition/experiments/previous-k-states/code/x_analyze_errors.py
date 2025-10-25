import os
import time
import pandas as pd
from models.gpt_model import GptModel

# Set parameters
agent_name_a = "react-v0"
agent_name_b = "react-v1"
model_name = "gpt-4.1-mini"

eval_size = 100
eval_names = [
    # "gaia",
    # "gpqa-diamond",
    # "hle",
    # "mmlu-pro",
    # "simple-qa",
    # "tw-simple",
    "tw-coin",
    "tw-treasure",
    "tw-cooking"
]

# Set paths
results_folder_path = "../data/results"
logs_base_path = "../data/logs"
messages_base_path = "../data/messages"
errors_folder_path = "../data/errors/details"

# Set prompt
prompt_template = """
You are an expert AI researcher analyzing the performance of different AI agents on various evaluation tasks. 
Your goal is to identify patterns in the errors made by these agents to provide insights into their strengths and weaknesses.
There are two agents (A and B) that attempted to complete a specific evaluation task, but agent B failed to do so successfully.
I will provide you with the results, logs, and messages for the two agent's attempt at the task.
You will provide me with a single sentence summary of why agent B failed to complete the task.
This summary will be used to categorize the errors made by the agents.
The Results section (below) contains data about the agent's performance on the task.
The Logs section (below) contains detailed logs of the agent's steps during the task.
The Messages (below) section contains the full conversation between the agent and the model.
Be concise in your response.

# Agent A Results
{results_a}

# Agent B Results
{results_b}

# Agent A Logs
{logs_a}

# Agent B Logs
{logs_b}

# Agent A Messages
{messages_a}

# Agent B Messages
{messages_b}
"""

# Create errors folder
os.makedirs(errors_folder_path, exist_ok=True)

for eval_name in eval_names:

    # Load results
    results_file_name_a = f"{agent_name_a} - {model_name} - {eval_name}-{eval_size}.csv"
    results_file_name_b = f"{agent_name_b} - {model_name} - {eval_name}-{eval_size}.csv"
    results_file_path_a = f"{results_folder_path}/{results_file_name_a}"
    results_file_path_b = f"{results_folder_path}/{results_file_name_b}"
    results_a = pd.read_csv(results_file_path_a)
    results_b = pd.read_csv(results_file_path_b)

    # Verify both results have the same number of rows
    if len(results_a) != len(results_b):
        raise ValueError(f"Results files have different number of rows: {len(results_a)} vs {len(results_b)}")

    errors = []
    for index, row_a in results_a.iterrows():

        print(f"Analyzing {agent_name_a} & {agent_name_b} - {model_name} - {eval_name}-{eval_size} - {index} / {len(results_a)}")

        row_b = results_b.iloc[index]

        if row_a["reward"] != 1.0:
            continue

        if row_b["reward"] == 1.0:
            continue

        # Get results a
        row_data_a = row_a.to_dict()
        row_text_a = "\n".join([f"{key}: {value}" for key, value in row_data_a.items()])

        # Get results b
        row_data_b = row_b.to_dict()
        row_text_b = "\n".join([f"{key}: {value}" for key, value in row_data_b.items()])

        # Load logs a
        logs_file_name_a = f"{index}.txt"
        logs_folder_name_a = f"{agent_name_a} - {model_name} - {eval_name}-{eval_size}"
        logs_file_path_a = f"{logs_base_path}/{logs_folder_name_a}/{logs_file_name_a}"
        with open(logs_file_path_a, 'r') as file:
            logs_a = file.read()

        # Load logs b
        logs_file_name_b = f"{index}.txt"
        logs_folder_name_b = f"{agent_name_b} - {model_name} - {eval_name}-{eval_size}"
        logs_file_path_b = f"{logs_base_path}/{logs_folder_name_b}/{logs_file_name_b}"
        with open(logs_file_path_b, 'r') as file:
            logs_b = file.read()

        # Load messages a
        messages_file_name_a = f"{index}.txt"
        messages_folder_name_a = f"{agent_name_a} - {model_name} - {eval_name}-{eval_size}"
        messages_file_path = f"{messages_base_path}/{messages_folder_name_a}/{messages_file_name_a}"
        with open(messages_file_path, 'r') as file:
            messages_a = file.read()

        # Load messages b
        messages_file_name_b = f"{index}.txt"
        messages_folder_name_b = f"{agent_name_b} - {model_name} - {eval_name}-{eval_size}"
        messages_file_path = f"{messages_base_path}/{messages_folder_name_b}/{messages_file_name_b}"
        with open(messages_file_path, 'r') as file:
            messages_b = file.read()

        # Format prompt
        prompt = prompt_template.format(
            results_a=row_text_a,
            results_b=row_text_b,
            logs_a=logs_a,
            logs_b=logs_b,
            messages_a=messages_a,
            messages_b=messages_b)
        print(prompt)

        model = GptModel("gpt-4.1-mini")
        prompt_messages = [{"role": "user", "content": prompt}]
        response = model.get_response(prompt_messages)
        print(response)
        print("\n---\n")

        error_line = f"{index}: {response}"
        errors.append(error_line)

        time.sleep(1)

    # Create target file
    errors_file_path = f"{errors_folder_path}/{agent_name_a} and {agent_name_b} - {model_name} - {eval_name}-{eval_size}.txt"
    with open(errors_file_path, 'w') as errors_file:
        for error in errors:
            errors_file.write(f"{error}\n")




