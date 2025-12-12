import os
from models.gpt_model import GptModel

# Set the parameters
base_folder_path = "../data/reflections"
file_name = "all.txt"
source_agent_name = "reflect-v3a-train"
target_agent_name = "reflect-v3b-train"
model_name = "gpt-4.1-mini"
eval_names = [
    "tw-simple-1",
    "tw-treasure-1",
    "tw-treasure-2",
    "tw-treasure-3",
    "tw-coin-1",
    "tw-coin-2",
    "tw-coin-3",
    "tw-cooking-1",
    "tw-cooking-2",
    "tw-cooking-3",
]

system_prompt = """
# Role
You are an intelligent agent that refines lists of self-reflections for LLM agents.
Your task it to ensure that the self-reflections are concise, non-redundant, and generally applicable.

# Definitions
A self-reflection is a previously encountered situation and advice for how to handle it better in the future.

# Instructions
Read through the list of self-reflections.
Merge similar self-reflections into a single, more general self-reflection.
Generalize overly specific self-reflections to make them more broadly applicable.
Order the self-reflections from most general and broadly applicable to most specific.

# Format
There should be one self-reflection per line.
Do not include any numbering or bullet points.
Each reflection must be formated as "When [situation], then [advice]."

# Examples
Input: 
 - When encountering blocked paths, then I should reassess available exits and choose alternative directions rather than repeatedly attempting blocked moves. 
 - When encountering blocked or unavailable exits, then I should reassess available paths and choose valid directions to continue progress rather than repeatedly attempting invalid moves. 
 - When encountering blocked exits or invalid moves, then I should reassess available exits and choose alternative valid directions to avoid getting stuck in loops.
Output:
 - When encountering blocked or invalid paths, then I should reassess the available exits and choose a valid alternative direction instead of repeating unsuccessful moves or getting stuck in loops.

"""

for eval_name in eval_names:

    # Set the paths
    source_folder_path = f"{base_folder_path}/{source_agent_name} - {model_name} - {eval_name}"
    source_file_path = f"{source_folder_path}/{file_name}"

    target_folder_path = f"{base_folder_path}/{target_agent_name} - {model_name} - {eval_name}"
    target_file_path = f"{target_folder_path}/{file_name}"

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder_path, exist_ok=True)

    # Read the content from the source file
    with open(source_file_path, 'r') as source_file:
        source_content = source_file.read()

    # Create the messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": source_content}
    ]

    # Get the response
    model = GptModel(model_name)
    target_content = model.get_response(messages)

    # Append the content to the target file
    with open(target_file_path, 'a') as target_file:
        target_file.write(target_content)