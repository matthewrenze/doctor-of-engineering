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
details_folder_path = "../data/errors/details"
summaries_folder_path = "../data/errors/summaries"


# Set prompt
prompt_template = """
You are an expert AI researcher analyzing the performance of different AI agents on various evaluation tasks. 
Your goal is to identify patterns in the errors made by these agents to provide insights into their strengths and weaknesses.
I will provide you with a list of reasons for why you thought an agent made an error on a specific task.
You will provide me with a much smaller set of categories for each of these errors.
These categories will be used to categorize future errors made by the agents.
Each error begins with the ID of the task within this specific eval set.
Be concise in your response.

# Errors
{errors}
"""


# Create errors folder
os.makedirs(summaries_folder_path, exist_ok=True)

for eval_name in eval_names:

    print(f"Analyzing {agent_name} - {model_name} - {eval_name}")

    # Load details
    file_name = f"{agent_name} - {model_name} - {eval_name}.txt"
    details_file_path = f"{details_folder_path}/{file_name}"
    with open(details_file_path, "r") as f:
        errors = f.read()

    # Create the model
    model = GptModel(model_name)

    # Create the prompt
    prompt = prompt_template.format(errors=errors)

    # Create the messages
    messages = [{"role": "user", "content": prompt}]

    # Get the response
    response = model.get_response(messages)

    print(response)

    # Write the summary
    summary_file_path = f"{summaries_folder_path}/{file_name}"
    with open(summary_file_path, "w") as f:
        f.write(response)