import os
import time
import pandas as pd
from models.gpt_model import GptModel

# Set parameters
agent_name = "react"
model_name = "gpt-4.1-mini"

eval_names = [
    "gaia-100",
    "gpqa-diamond-100",
    "hle-100",
    "mmlu-pro-100",
    "tw-simple-100",
    "tw-coin-100",
    "tw-treasure-100",
    "tw-cooking-100"]

# Set paths
results_folder_path = "../data/results"
logs_base_path = "../data/logs"
messages_base_path = "../data/messages"
errors_folder_path = "../data/errors/details"

# Set prompt
prompt_template = """
You are an expert AI researcher analyzing the performance of different AI agents on various evaluation tasks. 
Your goal is to identify patterns in the errors made by these agents to provide insights into their strengths and weaknesses.
I will provide you with the results, logs, and messages for the agent's attempt at the task.
You will provide me with a single sentence summary of why the agent failed to complete the task.
This summary will be used to categorize the errors made by the agents.
The Results section (below) contains data about the agent's performance on the task.
The Logs section (below) contains detailed logs of the agent's steps during the task.
The Messages (below) section contains the full conversation between the agent and the model.
Be concise in your response.

# Results
{results}

# Logs
{logs}

# Messages
{messages}
"""

# Create errors folder
os.makedirs(errors_folder_path, exist_ok=True)

for eval_name in eval_names:

    # Load results
    results_file_name = f"{agent_name} - {model_name} - {eval_name}.csv"
    results_file_path = f"{results_folder_path}/{results_file_name}"
    results = pd.read_csv(results_file_path)

    errors = []
    for index, row in results.iterrows():

        print(f"Analyzing {agent_name} - {model_name} - {eval_name} - {index} / {len(results)}")

        if row["reward"] == 1.0:
            continue

        # Get results
        row_data = row.to_dict()
        row_text = "\n".join([f"{key}: {value}" for key, value in row_data.items()])

        # Load logs
        logs_file_name = f"{index}.txt"
        logs_folder_name = f"{agent_name} - {model_name} - {eval_name}"
        logs_file_path = f"{logs_base_path}/{logs_folder_name}/{logs_file_name}"
        with open(logs_file_path, 'r') as file:
            logs = file.read()

        # Load messages
        messages_file_name = f"{index}.txt"
        messages_folder_name = f"{agent_name} - {model_name} - {eval_name}"
        messages_file_path = f"{messages_base_path}/{messages_folder_name}/{messages_file_name}"
        with open(messages_file_path, 'r') as file:
            messages = file.read()

        # Format prompt
        prompt = prompt_template.format(
            results=row_text,
            logs=logs,
            messages=messages)
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
    errors_file_path = f"{errors_folder_path}/{agent_name} - {model_name} - {eval_name}.txt"
    with open(errors_file_path, 'w') as errors_file:
        for error in errors:
            errors_file.write(f"{error}\n")




