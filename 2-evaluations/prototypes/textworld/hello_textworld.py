import os
import textworld
import textworld.gym

# Delete the old game
if os.path.exists("tw_games/hello_textworld.z8"):
    os.remove("tw_games/hello_textworld.z8")

# Create a game
options = textworld.GameOptions()
options.seed = 43
options.quest_length = 10
options.world_size = 5
options.nb_objects = 20
options.path = "tw_games/hello_textworld.z8"
game = textworld.make(options)
game_path = game[0]

# Load the game
env_id = textworld.gym.register_game(
    gamefile=game_path,
    request_infos=textworld.EnvInfos(admissible_commands=True),
    max_episode_steps=10)

# Create the environment
env = textworld.gym.make(env_id)

# Start the game
obs, infos = env.reset()
env.render()

# Set the variables
score = 0
moves = 0
done = False

# Play the game
while not done:
    command = input("> ")
    obs, score, done, infos = env.step(command)
    env.render()
    moves += 1

# Finish the game
env.close()
print(f"moves: {moves}; score: {score} ")