import os
import json
import textworld.challenges.tw_coin_collector

tasks = []
for task_id in range(10):
    print(f"Creating coin game {task_id}...")

    # Set random seed for reproducibility
    random_seed = task_id

    # Set path for the game
    game_path = f"../data/evals/textworld/coin-game/coin-game-{task_id}.z8"

    # Delete the old game
    if os.path.exists(game_path):
        os.remove(game_path)

    # Set the settings
    level = task_id + 210
    settings = {"level": level}

    # Set the options
    options = textworld.GameOptions()
    options.seeds = random_seed
    options.path = game_path

    # Create the game
    game = textworld.challenges.coin_collector.make(settings, options)

    # Compile the game
    game_path = textworld.generator.compile_game(game, options)

    # Add the task
    task = {"id": task_id, "file_path": game_path}
    tasks.append(task)


# Save the eval
num_tasks = [1, 10]
for i in num_tasks:
    task_set = tasks[:i]
    file_path = f"../data/evals/coin-game-{i}.jsonl"
    with open(file_path, 'w') as f:
        for task in task_set:
            f.write(json.dumps(task) + '\n')