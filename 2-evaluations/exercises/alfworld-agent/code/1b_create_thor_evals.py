import os
import sys
import json

# Set the task types
task_types = {
    1: "pick_and_place_simple",
    2: "look_at_obj_in_light",
    3: "pick_clean_then_place_in_recep",
    4: "pick_heat_then_place_in_recep",
    5: "pick_cool_then_place_in_recep",
    6: "pick_two_obj_and_place"
}

# Set folder path
input_folder_path = "/home/matthew/.cache/alfworld/json_2.1.1/train"
output_folder_path = "/mnt/c/Users/Matthew/Dropbox/School/JHU/DEng/Repository/2-evaluations/exercises/alfworld-agent/data/evals"

for task_type_key in task_types:
    task_type_value = task_types[task_type_key]
    tasks = []
    task_folder_names = os.listdir(input_folder_path)
    for task_id, task_folder_name in enumerate(task_folder_names):
        if task_type_value not in task_folder_name:
            continue

        # Get the trail folder path
        task_folder_path = os.path.join(input_folder_path, task_folder_name)
        trial_folder_names = os.listdir(task_folder_path)
        trial_folder_name = trial_folder_names[0]
        trial_folder_path = os.path.join(task_folder_path, trial_folder_name)
        print(trial_folder_path)

        # Get the task file path
        task_file_path = os.path.join(trial_folder_path, "game.tw-pddl")

        # Add the task to the eval list
        eval_row = {"id": task_id, "file_path": task_file_path}
        tasks.append(eval_row)


    # Save the eval
    num_tasks = [1, 10]
    for i in num_tasks:
        task_set = tasks[:i]
        file_name = f"alfworld-thor-level-{task_type_key}-{i}.jsonl"
        file_path = os.path.join(output_folder_path, file_name)
        with open(file_path, 'w') as f:
            for task in task_set:
                f.write(json.dumps(task) + '\n')
