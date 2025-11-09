import os
import json
import textworld.challenges.tw_cooking.cooking
import textworld.render.render

# Set parameters
num_tasks = 100
eval_folder_path = "../data/evals/tw-cooking"
game_folder_path = "../data/evals/tw-cooking/files"
curriculum = [
    # Level 1 - One item
    {"level": 1, "sublevel": 1, "go": 1, "recipe": 1, "take": 0, "open": False, "cook": False, "cut": False, "drop": False},
    {"level": 1, "sublevel": 2, "go": 1, "recipe": 1, "take": 1, "open": False, "cook": False, "cut": False, "drop": False}, # take
    {"level": 1, "sublevel": 3, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": False, "cut": False, "drop": False}, # take + open
    {"level": 1, "sublevel": 4, "go": 1, "recipe": 1, "take": 1, "open": False, "cook": True, "cut": False, "drop": False}, # take + cook
    {"level": 1, "sublevel": 5, "go": 1, "recipe": 1, "take": 1, "open": False, "cook": False, "cut": True, "drop": False}, # take + cut
    {"level": 1, "sublevel": 6, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": True, "cut": False, "drop": False}, # take + open + cook
    {"level": 1, "sublevel": 7, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": True, "cut": True, "drop": False}, # take + open + cook + cut
    {"level": 1, "sublevel": 8, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": True, "cut": True, "drop": True}, # take + open + cook + cut + drop

    # Level 2 - Multiple items
    {"level": 2, "sublevel": 1, "go": 1, "recipe": 2, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 2, "go": 1, "recipe": 2, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 3, "go": 1, "recipe": 2, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 4, "go": 1, "recipe": 3, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 5, "go": 1, "recipe": 3, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 6, "go": 1, "recipe": 3, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 7, "go": 1, "recipe": 3, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 8, "go": 1, "recipe": 4, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 9, "go": 1, "recipe": 4, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 10, "go": 1, "recipe": 4, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 11, "go": 1, "recipe": 4, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 12, "go": 1, "recipe": 4, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 13, "go": 1, "recipe": 5, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 14, "go": 1, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 15, "go": 1, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 16, "go": 1, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 17, "go": 1, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 2, "sublevel": 18, "go": 1, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 3 - Multiple locations
    {"level": 3, "sublevel": 1, "go": 6, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 2, "go": 6, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 3, "go": 6, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 4, "go": 6, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 5, "go": 6, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 6, "go": 9, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 7, "go": 9, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 8, "go": 9, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 9, "go": 9, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 10, "go": 9, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 11, "go": 12, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 12, "go": 12, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 13, "go": 12, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 14, "go": 12, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 3, "sublevel": 15, "go": 12, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},
]

# Create the target files folders
os.makedirs(eval_folder_path, exist_ok=True)
os.makedirs(game_folder_path, exist_ok=True)

# HACK: Temporary level/sublevel numbers
for level_id in range(1, 4):
    level_group = [lesson for lesson in curriculum if lesson["level"] == level_id]

    tasks = []
    for task_id in range(1, num_tasks + 1):
        print(f"Creating tw-cooking-{level_id} task-{task_id} ...")

        # Set random seed
        random_seed = task_id

        # Hack: fix the broken task 3-94
        if level_id == 3 and task_id == 94:
            random_seed += 100

        # Set path for the game
        game_file_name = f"tw-cooking-{level_id}-{task_id}.ulx"
        game_file_path = game_folder_path + "/" + game_file_name

        # Delete the old game
        if os.path.exists(game_file_path):
            os.remove(game_file_path)

        # Get the lesson settings
        lesson_index = (task_id - 1) * len(level_group) // num_tasks
        lesson = level_group[lesson_index]

        # Set the settings
        settings = lesson
        settings["split"] = "train"

        # Hack: to workaround "Shuffle recipe requires the 'take' skill" issue
        settings["recipe_seed"] = 0 if lesson["take"] == 0 else random_seed

        print(f"  Settings: {settings}")

        # Set the options
        options = textworld.GameOptions()
        options.path = game_file_path
        options.seeds = {
            "map": random_seed,
            "objects": random_seed,
            "quest": random_seed,
            "grammar": random_seed}

        # Create the game
        game = textworld.challenges.cooking.make(settings, options)

        # Compile the game
        game_path = textworld.generator.compile_game(game, options)

        # Add the task
        task = {
            "id": task_id,
            "level": level_id,
            "sublevel": lesson["sublevel"],
            "task": game.objective,
            "solution": ", ".join(game.walkthrough),
            "solution_steps": len(game.walkthrough),
            "file_path": game_file_path
        }
        tasks.append(task)

    # Save the evals
    eval_file_name = f"tw-cooking-{level_id}.jsonl"
    eval_file_path = eval_folder_path + "/" + eval_file_name
    print(f"Creating {eval_file_name}...")
    with open(eval_file_path, 'w') as f:
        for task in tasks:
            f.write(json.dumps(task) + '\n')