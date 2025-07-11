import os
import textworld
import textworld.gym
import textworld.challenges.tw_simple.simple

game_path = "tw_games/simple_game.z8"

# Delete the old game
if os.path.exists(game_path):
    os.remove(game_path)

# Set the settings
settings = {
    "rewards": "balanced",
    "goal": "detailed",
    "test": True}

# Set the options
options = textworld.GameOptions()
options.seeds = 42
options.path = game_path

# Create the game
game = textworld.challenges.simple.make(settings, options)

# Compile the game
game_path = textworld.generator.compile_game(game, options)

# Set the env info (what info the player has access to)
env_infos = textworld.EnvInfos(
    admissible_commands=True,
    description=True,
    inventory=True,
    feedback=True)

# Register the game
env_id = textworld.gym.register_game(
    game_path,
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

# Finish the game
env.render()
env.close()

# Print the results
print(f"Moves: {moves}")
print(f"Score: {score}")








