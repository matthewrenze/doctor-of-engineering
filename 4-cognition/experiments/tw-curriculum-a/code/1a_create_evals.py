import os
import json
import textworld.challenges.tw_cooking.cooking
import textworld.render.render

# Set parameters
num_tasks = 10
eval_folder_path = "../data/evals/tw-curriculum"
game_folder_path = "../data/evals/tw-curriculum/files"
curriculum = [
    # Level 1 - Basics
    {"level": 1, "sublevel": 1, "go": 1, "recipe": 1, "take": 0, "open": False, "cook": False, "cut": False, "drop": False},
    {"level": 1, "sublevel": 2, "go": 1, "recipe": 1, "take": 1, "open": False, "cook": False, "cut": False, "drop": False}, # take

    # Level 2 - Single Skills
    {"level": 2, "sublevel": 1, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": False, "cut": False, "drop": False}, # open (requires take)
    {"level": 2, "sublevel": 2, "go": 1, "recipe": 1, "take": 1, "open": False, "cook": True, "cut": False, "drop": False}, # cook
    {"level": 2, "sublevel": 3, "go": 1, "recipe": 1, "take": 1, "open": False, "cook": False, "cut": True, "drop": False}, # cut

    # Level 3 - Multiple Skills
    {"level": 3, "sublevel": 1, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": True, "cut": False, "drop": False}, # take + open + cook
    {"level": 3, "sublevel": 2, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": True, "cut": True, "drop": False}, # take + open + cook + cut
    {"level": 3, "sublevel": 3, "go": 1, "recipe": 1, "take": 1, "open": True, "cook": True, "cut": True, "drop": True}, # take + open + cook + cut + drop

    # Level 4 - Two Items
    {"level": 4, "sublevel": 1, "go": 1, "recipe": 2, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 4, "sublevel": 2, "go": 1, "recipe": 2, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 4, "sublevel": 3, "go": 1, "recipe": 2, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 5 - Three Items
    {"level": 5, "sublevel": 1, "go": 1, "recipe": 3, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 5, "sublevel": 2, "go": 1, "recipe": 3, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 5, "sublevel": 3, "go": 1, "recipe": 3, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 5, "sublevel": 4, "go": 1, "recipe": 3, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 6 - Four Items
    {"level": 6, "sublevel": 1, "go": 1, "recipe": 4, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 6, "sublevel": 2, "go": 1, "recipe": 4, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 6, "sublevel": 3, "go": 1, "recipe": 4, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 6, "sublevel": 4, "go": 1, "recipe": 4, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 6, "sublevel": 5, "go": 1, "recipe": 4, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 7 - Five Items
    {"level": 7, "sublevel": 1, "go": 1, "recipe": 5, "take": 0, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 7, "sublevel": 2, "go": 1, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 7, "sublevel": 3, "go": 1, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 7, "sublevel": 4, "go": 1, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 7, "sublevel": 5, "go": 1, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 7, "sublevel": 6, "go": 1, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 8 - Six Rooms
    {"level": 8, "sublevel": 1, "go": 6, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 8, "sublevel": 2, "go": 6, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 8, "sublevel": 3, "go": 6, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 8, "sublevel": 4, "go": 6, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 8, "sublevel": 5, "go": 6, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 9 - Nine Rooms
    {"level": 9, "sublevel": 1, "go": 9, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 9, "sublevel": 2, "go": 9, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 9, "sublevel": 3, "go": 9, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 9, "sublevel": 4, "go": 9, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 9, "sublevel": 5, "go": 9, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},

    # Level 10 - Twelve Rooms
    {"level": 10, "sublevel": 1, "go": 12, "recipe": 5, "take": 1, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 10, "sublevel": 2, "go": 12, "recipe": 5, "take": 2, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 10, "sublevel": 3, "go": 12, "recipe": 5, "take": 3, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 10, "sublevel": 4, "go": 12, "recipe": 5, "take": 4, "open": True, "cook": True, "cut": True, "drop": True},
    {"level": 10, "sublevel": 5, "go": 12, "recipe": 5, "take": 5, "open": True, "cook": True, "cut": True, "drop": True},
]

# Create the target files folders
os.makedirs(eval_folder_path, exist_ok=True)
os.makedirs(game_folder_path, exist_ok=True)

# HACK: Temporary level/sublevel numbers
for lesson in curriculum:
    level_id = lesson["level"]
    sublevel_id = lesson["sublevel"]
    tasks = []

    for task_id in range(1, num_tasks + 1):
        print(f"Creating tw-curriculum-{level_id}.{sublevel_id} task-{task_id} ...")

        # Set random seed
        random_seed = task_id

        # Set path for the game
        game_file_name = f"tw-curriculum-{level_id}-{sublevel_id}-{task_id}.ulx"
        game_file_path = game_folder_path + "/" + game_file_name

        # Delete the old game
        if os.path.exists(game_file_path):
            os.remove(game_file_path)

        # Set the settings
        settings = lesson
        settings["split"] = "train"

        # Hack: to workaround "Shuffle recipe requires the 'take' skill" issue
        settings["recipe_seed"] = 0 if lesson["take"] == 0 else random_seed

        print(f"  Settings: {settings}")

        # # Set the settings
        # settings = {
        #     "go" : 6,
        #     "recipe": 3,
        #     "take": 2,
        #     "open": True,
        #     "cut": True,
        #     "cook": True,
        #     "drop": True,
        #     "recipe_seed": random_seed,
        #     "split": "train"
        # }

        # Set the options
        options = textworld.GameOptions()
        options.seeds = {
            "map": random_seed,
            "objects": random_seed,
            "quest": random_seed,
            "grammar": random_seed}
        options.path = game_file_path

        # Create the game
        game = textworld.challenges.cooking.make(settings, options)

        # Compile the game
        game_path = textworld.generator.compile_game(game, options)

        # Add the task
        task = {"id": task_id, "file_path": game_path}
        tasks.append(task)

    # Save the evals
    eval_file_name = f"tw-curriculum-{level_id}-{sublevel_id}.jsonl"
    eval_file_path = eval_folder_path + "/" + eval_file_name
    print(f"Creating {eval_file_name}...")
    with open(eval_file_path, 'w') as f:
        for task in tasks:
            f.write(json.dumps(task) + '\n')