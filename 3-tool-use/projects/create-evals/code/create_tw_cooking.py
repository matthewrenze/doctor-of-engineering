import os
import json
import textworld.challenges.tw_cooking.cooking
import textworld.render.render

# Set parameters
num_tasks = 100
task_sets = [1, 10, 100]
eval_folder_path = "../data/evals/textworld"
game_folder_path = "../data/evals/textworld/tw-cooking"
curriculum = [
    {"go": 1, "recipe": 1, "take": 1, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 1, "recipe": 2, "take": 2, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 1, "recipe": 3, "take": 3, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 1, "recipe": 4, "take": 4, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 6, "recipe": 5, "take": 5, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 6, "recipe": 5, "take": 5, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 9, "recipe": 5, "take": 5, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 9, "recipe": 5, "take": 5, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 12, "recipe": 5, "take": 5, "open": True, "cut": True, "cook": True, "drop": True},
    {"go": 12, "recipe": 5, "take": 5, "open": True, "cut": True, "cook": True, "drop": True},
]

# Create the target files folders
os.makedirs(eval_folder_path, exist_ok=True)
os.makedirs(game_folder_path, exist_ok=True)

tasks = []
for task_id in range(num_tasks):
    print(f"Creating tw-cooking-{task_id} game...")

    # Set random seed
    random_seed = task_id

    # Set path for the game
    game_file_name = f"tw-cooking-{task_id}.ulx"
    game_file_path = game_folder_path + "/" + game_file_name

    # Delete the old game
    if os.path.exists(game_file_path):
        os.remove(game_file_path)

    # Set the settings
    level = (task_id % 10)
    settings = curriculum[level]
    settings["split"] = "train"
    settings["recipe_seed"] = random_seed
    print(f"  Level: {level}")
    print(f"  Settings: {settings}")

    # # Set the settings
    # settings = {
    #     "recipe": 3,
    #     "take": 2,
    #     "go" : 6,
    #     "open": True,
    #     "cook": True,
    #     "cut": True,
    #     "drop": True,
    #     "recipe_seed": random_seed,
    #     "split": "train"
    # }

    # Set the options
    options = textworld.GameOptions()
    # options.seeds = {"map": random_seed, "objects": random_seed, "quest": random_seed, "grammar": random_seed}
    options.seeds = random_seed
    options.path = game_file_path

    # Create the game
    game = textworld.challenges.cooking.make(settings, options)

    # Compile the game
    game_path = textworld.generator.compile_game(game, options)

    # Add the task
    task = {"id": task_id, "file_path": game_path}
    tasks.append(task)

# Save the evals
num_tasks = task_sets
for i in num_tasks:
    task_set = tasks[:i]
    eval_file_name = f"tw-cooking-{i}.jsonl"
    eval_file_path = eval_folder_path + "/" + eval_file_name
    print(f"Creating {eval_file_name}...")
    with open(eval_file_path, 'w') as f:
        for task in task_set:
            f.write(json.dumps(task) + '\n')