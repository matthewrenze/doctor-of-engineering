import sys
import time
import yaml
import numpy as np
from alfworld.agents.environment import get_environment

# Load the config
config_file = "base_config.yaml"
with open(config_file) as reader:
    config = yaml.safe_load(reader)

# Set the environment type
env_type = "AlfredTWEnv"
# env_type = "AlfredThorEnv"
# env_type = "AlfredHybrid"

# Setup the environment
env = get_environment(env_type)(config, train_eval='train')
env = env.init_env(batch_size=1)

# Reset the environment
obs, info = env.reset()
for i in range(50):

    print(f"# Step {i + 1}")

    # Get Random action
    admissible_commands = list(info['admissible_commands']) # note: BUTLER generates commands word-by-word without using admissible_commands
    random_actions = [np.random.choice(admissible_commands[0])]
    action = random_actions[0]
    print(f"Action: {action}")

    # Execute the action
    obs, scores, dones, infos = env.step([action])
    print(f"State: {obs[0]}")
    print()

    time.sleep(1)