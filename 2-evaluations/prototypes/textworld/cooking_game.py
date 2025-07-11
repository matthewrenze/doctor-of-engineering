import os
import numpy as np
import textworld.challenges.tw_cooking.cooking
import textworld.gym
import textworld.render.render

# Set random seed for reproducibility
random_seed = 42
np.random.seed(random_seed)

# Path for the game
game_path = "tw_games/cooking_world.z8"
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
options.seeds = {"map": random_seed, "objects": random_seed, "quest": random_seed, "grammar": random_seed}
options.path = game_path

# Create the game
game = textworld.challenges.cooking.make(settings, options)

# Compile the game
game_file = textworld.generator.compile_game(game, options)

# Set the env info (what info the player has access to)
env_infos = textworld.EnvInfos(
    admissible_commands=True,
    description=True,
    inventory=True,
    feedback=True)

# Register the game
env_id = textworld.gym.register_game(
    gamefile=game_file,
    request_infos=env_infos,
    max_episode_steps=50)

# Create the environment
env = textworld.gym.make(env_id)

# Set the game variables
done = False
score = 0
moves = 0

# Start the game
state, infos = env.reset()

# Play the game
while not done:
    env.render()
    command = input("> ")
    state, score, done, infos = env.step(command)
    moves += 1
    print(infos)

# End the game
env.render()
env.close()

# Print the results
print(f"Moves: {moves}")
print(f"Score: {score}")
