import os
from models.gpt_model import GptModel

# Set parameters
summaries_folder_path = "../data/errors/summaries"
target_file_name = "_meta-summary.txt"

# Set prompt
prompt_template = """
You are an expert AI researcher analyzing the performance of different AI agents on various evaluation tasks.
Your goal is to identify patterns in the errors made by these agents to provide insights into their strengths and weaknesses.
I will provide you with a set of summaries for why an agent failed to complete specific tasks.
You will provide me with a meta-analysis of these summaries.
 - Identify common themes and patterns.
 - Suggest potential improvements for the agents based on these patterns.
 - Highlight any surprising or unexpected findings.
This meta-analysis will be used to guide future development and refinement of the agents.
Each summary begins with the agent-name, model-name, and eval-name.
Be concise in your response.

# Summaries
{summaries}

"""

summaries = []
input_file_names = os.listdir(summaries_folder_path)
for file_name in input_file_names:
    if not file_name.endswith(".txt"):
        continue

    if file_name == target_file_name:
        continue

    print(f"Summarizing {file_name}")

    # Load summary
    summary_file_path = f"{summaries_folder_path}/{file_name}"
    with open(summary_file_path, "r") as f:
        summary = f.read()

    summaries.append(f"## {file_name}\n\n{summary}\n\n --- \n\n")

# Combine summaries
summaries = "\n".join(summaries)

# Set prompt
prompt = prompt_template \
    .format(summaries=summaries) \
    .strip()

# Create the model
model = GptModel("gpt-4.1-mini")

# Create the messages
messages = [{"role": "user", "content": prompt}]

# Get the response
response = model.get_response(messages)

# Save the response
output_file_path = f"{summaries_folder_path}/{target_file_name}"
with open(output_file_path, "w") as f:
    f.write(response)
