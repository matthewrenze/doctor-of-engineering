import textworld

# Set the env info (what info the player has access to)
infos = textworld.EnvInfos(
    feedback=True,
    description=True,
    inventory=True)

# Start the game
env = textworld.start("tw_games/zork1.z5")

# Set the variables
done = False
score = 0
moves = 0

# Start the game
env.reset()

# Play the game
while not done:
    env.render()
    command = input("> ")
    game_state, score, done = env.step(command)
    moves += 1

# End the game
env.render()
env.close()
print(f"Moves: {moves}")
print(f"Score: {score}")