import os
import json
import textworld.challenges.tw_cooking.cooking
import textworld.render.render

tasks = []
for task_id in range(10):
    print(f"Creating cooking game {task_id}...")

    # Set random seed
    random_seed = task_id

    # Set path for the game
    game_path = f"../data/evals/textworld/cooking-game/cooking-game-{task_id}.z8"

    # Delete the old game
    if os.path.exists(game_path):
        os.remove(game_path)

    # Set the settings
    settings = {
        "recipe": 3,
        "take": 2,
        "go" : 6,
        "open": True,
        "cook": True,
        "cut": True,
        "drop": True,
        "recipe_seed": random_seed,
        "split": "train"
    }

    # Set the options
    options = textworld.GameOptions()
    # options.seeds = {"map": random_seed, "objects": random_seed, "quest": random_seed, "grammar": random_seed}
    options.seeds = random_seed
    options.path = game_path

    # Create the game
    game = textworld.challenges.cooking.make(settings, options)

    # Compile the game
    game_path = textworld.generator.compile_game(game, options)

    # Add the task
    task = {"id": task_id, "file_path": game_path}
    tasks.append(task)

# Save the eval
num_tasks = [1, 10]
for i in num_tasks:
    task_set = tasks[:i]
    file_path = f"../data/evals/cooking-game-{i}.jsonl"
    with open(file_path, 'w') as f:
        for task in task_set:
            f.write(json.dumps(task) + '\n')