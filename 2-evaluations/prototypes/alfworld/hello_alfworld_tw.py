import yaml
from alfworld.agents.environment.alfred_tw_env import AlfredTWEnv

# Load the config
config_file = "base_config.yaml"
with open(config_file) as reader:
    config = yaml.safe_load(reader)

# Set the task types
# Note: 1 - Pick & Place, 2 - Examine in Light, 3 - Clean & Place, 4 - Heat & Place, 5 - Cool & Place, 6 - Pick Two & Place
config["env"]["task_types"] = [1]

# Setup the environment
env = AlfredTWEnv(config, train_eval="train")
env = env.init_env(batch_size=1)

# Reset the environment
state, infos = env.reset()
print(state[0])

for step_id in range(100):

    print(f"# Step {step_id + 1}")

    # Get action from user
    # action = input(">")

    # Get expert action
    action = infos["extra.expert_plan"][0][0]
    print(action)


    # Exit on "exit"
    if action == "exit":
        break

    # Get the next state from the environment
    state, score, is_done, infos = env.step([action])
    print(state[0])

    # Exit if game is done
    if is_done[0]:
        score = 1 if infos["won"] else 0
        print(f"Score: {score}")
        break

    print()
