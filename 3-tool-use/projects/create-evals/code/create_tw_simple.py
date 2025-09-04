import os
import json
import textworld.challenges.tw_simple.simple

# Set parameters
num_tasks = 100
task_sets = [1, 10, 100]
eval_folder_path = "../data/evals/textworld"
game_folder_path = "../data/evals/textworld/tw-simple"

# Create the target files folders
os.makedirs(eval_folder_path, exist_ok=True)
os.makedirs(game_folder_path, exist_ok=True)

tasks = []
for task_id in range(num_tasks):
    print(f"Creating tw-simple-{task_id} game...")

    # Set random seed
    random_seed = task_id

    # Set path for the game
    game_file_name = f"tw-simple-{task_id}.ulx"
    game_file_path = game_folder_path + "/" + game_file_name

    # Delete the old game
    if os.path.exists(game_file_path):
        os.remove(game_file_path)

    # Set the settings
    settings = {
        "rewards": "dense",
        "goal": "detailed",
        "test": False}

    # Set the options
    options = textworld.GameOptions()
    options.seeds = random_seed
    options.path = game_file_path

    # Create the game
    game = textworld.challenges.simple.make(settings, options)

    # Compile the game
    game_path = textworld.generator.compile_game(game, options)

    # Add the game to the eval list
    eval_row = {"id": task_id, "file_path": game_path}
    tasks.append(eval_row)

# Save the evals
for i in task_sets:
    task_set = tasks[:i]
    eval_file_name = f"tw-simple-{i}.jsonl"
    eval_file_path = eval_folder_path + "/" + eval_file_name
    print(f"Creating {eval_file_name} eval...")
    with open(eval_file_path, 'w') as f:
        for task in task_set:
            f.write(json.dumps(task) + '\n')
