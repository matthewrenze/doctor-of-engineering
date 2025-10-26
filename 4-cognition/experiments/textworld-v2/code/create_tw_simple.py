import os
import json
import textworld.challenges.tw_simple.simple

# Set parameters
num_tasks = 100
goal_verbosity = ["detailed", "brief", "none"]
reward_densities = ["dense", "balanced", "sparse"]
num_sublevels = len(goal_verbosity) * len(reward_densities)
eval_folder_path = "../data/evals/tw-simple"
game_folder_path = "../data/evals/tw-simple/files"

# Create the target files folders
os.makedirs(eval_folder_path, exist_ok=True)
os.makedirs(game_folder_path, exist_ok=True)

tasks = []
for task_id in range(1, num_tasks + 1):

    # Set level and sublevel
    level_id = 1
    sublevel_id = min((task_id - 1) * num_sublevels // num_tasks + 1, num_sublevels)

    print(f"Creating tw-simple-{level_id} task-{task_id} ...")

    # Set random seed
    random_seed = task_id

    # Set path for the game
    game_file_name = f"tw-simple-{level_id}-{task_id}.ulx"
    game_file_path = game_folder_path + "/" + game_file_name

    # Delete the old game
    if os.path.exists(game_file_path):
        os.remove(game_file_path)

    # Get the reward density and goal verbosity
    goal_verbosity_text = goal_verbosity[((sublevel_id - 1) // len(reward_densities)) % len(goal_verbosity)]
    reward_density_text = reward_densities[(sublevel_id - 1) % len(reward_densities)]


    # Set the settings
    settings = {
        "goal": goal_verbosity_text,
        "rewards": reward_density_text,
        "test": False}
    print(f"  Sublevel: {sublevel_id}")
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
    game = textworld.challenges.simple.make(settings, options)

    # Compile the game
    game_path = textworld.generator.compile_game(game, options)

    # Add the eval metadata
    eval_row = {
        "id": task_id,
        "level": level_id,
        "sublevel": sublevel_id,
        "task": game.objective,
        "solution": ", ".join(game.walkthrough),
        "solution_steps": len(game.walkthrough),
        "file_path": game_path}
    tasks.append(eval_row)

# Save the evals
eval_file_name = f"tw-simple-{level_id}.jsonl"
eval_file_path = eval_folder_path + "/" + eval_file_name
print(f"Saving {eval_file_name} eval...")
with open(eval_file_path, 'w') as f:
    for task in tasks:
        f.write(json.dumps(task) + '\n')
print("\n---\n")
