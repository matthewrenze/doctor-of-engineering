# Import libraries
import textworld.gym

# Set path to the game file
file_name = "tw-curriculum-1-1-1.ulx"
folder_path = "../data/evals/tw-curriculum/files/"
file_path = folder_path + file_name

# Set the env info (what info the player has access to)
env_infos = textworld.EnvInfos(
    objective=True,
    max_score=True,
    location=True,
    description=True,
    inventory=True,
    feedback=True,
    admissible_commands=True)

# Register the game
env_id = textworld.gym.register_game(
    gamefile=file_path,
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
print("Infos:")
for key, value in infos.items():
    if isinstance(value, str):
        value = value.replace('\n', '')
    print(f" - {key}: {value}")
print(f"State: {state}")

# Play the game
while not done:
    # env.render()
    command = input("> ")
    state, score, done, infos = env.step(command)
    moves += 1
    print("Infos:")
    for key, value in infos.items():
        if isinstance(value, str):
            value = value.replace('\n', '')
        print(f" - {key}: {value}")
    print(f"State: {state}")
    print(f"Score: {score}")
    print(f"Done: {done}")


# End the game
env.render()
env.close()

# Print the results
print(f"Moves: {moves}")
print(f"Score: {score}")
