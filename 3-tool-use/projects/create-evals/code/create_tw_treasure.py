import os
import json
import textworld.challenges.tw_coin_collector

# Set parameters
num_tasks = 100
task_sets = [1, 10, 100]
eval_folder_path = "../data/evals/tw-treasure"
game_folder_path = "../data/evals/tw-treasure/files"

tasks = []
for task_id in range(num_tasks):
    print(f"Creating tw-treasure-{task_id} game...")

    # Set random seed
    random_seed = task_id

    # Set the path
    game_file_name = f"tw-treasure-{task_id}.ulx"
    game_file_path = game_folder_path + "/" + game_file_name

    # Delete the old game
    if os.path.exists(game_file_path):
        os.remove(game_file_path)

    # Set the settings
    level = (task_id % 10) + 21
    settings = {"level": level}
    print(f"  Level: {level}")

    # Set the options
    options = textworld.GameOptions()
    options.seeds = random_seed
    options.path = game_file_path

    # Create the game
    game = textworld.challenges.treasure_hunter.make(settings, options)

    # Compile the game
    game_path = textworld.generator.compile_game(game, options)

    # Add the task
    task = {"id": task_id, "file_path": game_path}
    tasks.append(task)

# Save the eval
for i in task_sets:
    task_set = tasks[:i]
    eval_file_name = f"tw-treasure-{i}.jsonl"
    eval_file_path = eval_folder_path + "/" + eval_file_name
    print(f"Creating {eval_file_name}...")
    with open(eval_file_path, 'w') as f:
        for task in task_set:
            f.write(json.dumps(task) + '\n')