import os
import json
import textworld.challenges.tw_coin_collector

# Set parameters
num_levels = 3
num_tasks = 100
eval_folder_path = "../data/evals/tw-treasure"
game_folder_path = "../data/evals/tw-treasure/files"

for level_id in range(1, num_levels + 1):

    tasks = []
    for task_id in range(1, num_tasks + 1):
        print(f"Creating tw-treasure-{level_id} task-{task_id}...")

        # Set random seed
        random_seed = task_id

        # Set the path
        game_file_name = f"tw-treasure-{level_id}-{task_id}.ulx"
        game_file_path = game_folder_path + "/" + game_file_name

        # Delete the old game
        if os.path.exists(game_file_path):
            os.remove(game_file_path)

        # Set the settings
        sublevel = (task_id - 1) // 10 + 1
        game_level = ((level_id - 1) * 10) + ((task_id - 1) // 10 + 1)
        settings = {"level": game_level}
        print(f"  Settings: {settings}")
        print(f"  Sublevel: {sublevel}")

        # HACK: to fix "Current map configuration doesn't permit quest of length: {n}"
        retry = True
        while retry:

            # Create the game
            try:

                # Set the options
                options = textworld.GameOptions()
                options.path = game_file_path
                options.seeds = {
                    "map": random_seed,
                    "objects": random_seed,
                    "quest": random_seed,
                    "grammar": random_seed}

                game = textworld.challenges.treasure_hunter.make(settings, options)
                retry = False

            except Exception as e:
                retry = True
                random_seed += 100
                print(f"  *** Retry due to error: {e} ***")

        # Compile the game
        game_path = textworld.generator.compile_game(game, options)

        # Add the task
        task = {
            "id": task_id,
            "level": level_id,
            "sublevel": sublevel,
            "task": game.objective,
            "solution": ", ".join(game.walkthrough),
            "solution_steps": len(game.walkthrough),
            "file_path": game_file_path
        }
        tasks.append(task)

    # Save the eval
    eval_file_name = f"tw-treasure-{level_id}.jsonl"
    eval_file_path = eval_folder_path + "/" + eval_file_name
    print(f"Saving {eval_file_name}...")
    with open(eval_file_path, 'w') as f:
        for task in tasks:
            f.write(json.dumps(task) + '\n')
    print("\n---\n")