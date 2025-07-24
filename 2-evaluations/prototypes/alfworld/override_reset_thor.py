import sys
import yaml
import numpy as np
from alfworld.agents.environment.alfred_thor_env import AlfredThorEnv
from alfworld.agents.environment import get_environment
import matplotlib.pyplot as plt
from PIL import Image

class CustomAlfredThorEnv(AlfredThorEnv):
    def __init__(self, config, train_eval="train"):
        super().__init__(config, train_eval)
        self.current_task_index = 0

    def reset(self, task_file):
        batch_size = self.batch_size

        if task_file is not None:
            tasks = [task_file] * batch_size
        else:
            tasks = []
            for _ in range(batch_size):
                task = self.json_file_list[self.current_task_index % len(self.json_file_list)]
                tasks.append(task)
                self.current_task_index += 1

        for n in range(batch_size):
            self.action_queues[n].put((None, True, tasks[n]))

        obs, dones, infos = self.wait_and_get_info()
        return obs, infos


# Load the config
config_file = "base_config.yaml"
with open(config_file) as reader:
    config = yaml.safe_load(reader)

# Manually set environment type
# env_type = "AlfredTWEnv"
env_type = "AlfredThorEnv"
# env_type = "AlfredHybrid"

# Set the task types
# Note: 1 - Pick & Place, 2 - Examine in Light, 3 - Clean & Place, 4 - Heat & Place, 5 - Cool & Place, 6 - Pick Two & Place
config["env"]["task_types"] = [1]

# Setup the environment
env = get_environment(env_type)(config, train_eval="train")
env = env.init_env(batch_size=1)

# Reset the environment
task_file = "/home/matthew/.cache/alfworld/json_2.1.1/train/pick_and_place_simple-Candle-None-Toilet-409/trial_T20190908_014219_052080/traj_data.json"
state, infos = env.reset(task_file)
print(state[0])

exploration_frames = env.get_exploration_frames()
frames = env.get_frames()
frame = frames[0]
print(frame.shape)
print("R:", frame[:, :, 0].min(), frame[:, :, 0].max())
print("G:", frame[:, :, 1].min(), frame[:, :, 1].max())
print("B:", frame[:, :, 2].min(), frame[:, :, 2].max())


# Display frame using matplotlib
frame_rgb = frame[:, :, ::-1]  # reverse last dimension (BGR → RGB)
plt.imshow(frame_rgb)
plt.axis("off")
plt.show()


# Display frame using PIL
Image.fromarray(frame).save("frame.png")
Image.fromarray(frame_rgb).save("frame_rgb.png")



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
    exploration_frames = env.get_exploration_frames()
    frames = env.get_frames()
    print(state[0])

    # Exit if game is done
    if is_done[0]:
        score = 1 if infos["won"] else 0
        print(f"Score: {score}")
        break

    print()
