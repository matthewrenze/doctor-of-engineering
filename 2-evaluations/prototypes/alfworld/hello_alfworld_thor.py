import sys
import time
import yaml
from alfworld.agents.environment.alfred_thor_env import AlfredThorEnv
import matplotlib.pyplot as plt
from PIL import Image

def display_frame(frame):
    frame_rgb = frame[:, :, ::-1] # BGR -> RGB
    plt.imshow(frame_rgb)
    plt.axis("off")
    plt.show()

# HACK: to load config file
sys.argv = ["hello_alfworld.py", "base_config.yaml"]

# Load the config
config_file = "base_config.yaml"
with open(config_file) as reader:
    config = yaml.safe_load(reader)

# Set the task types
# Note: 1 - Pick & Place, 2 - Examine in Light, 3 - Clean & Place, 4 - Heat & Place, 5 - Cool & Place, 6 - Pick Two & Place
config["env"]["task_types"] = [1]

# Set the image size
# config["env"]["thor"]["screen_width"] = 600
# config["env"]["thor"]["screen_height"] = 600

# Setup the environment
env = AlfredThorEnv(config, train_eval="train")
env = env.init_env(batch_size=1)

# Reset the environment
state, infos = env.reset()
print(state[0])

# Display the first frame
frames = env.get_frames()
frame = frames[0]
display_frame(frame)

# Save the frame using PIL
frame_rgb = frame[:, :, ::-1] # BGR -> RGB
Image.fromarray(frame_rgb).save("frame.png")

for step_id in range(50):

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

    # Display the exploration frames
    frames = env.get_frames()
    frame = frames[0]
    display_frame(frame)

    # Exit if game is done
    if is_done[0]:
        score = 1 if infos["won"] else 0
        print(f"Score: {score}")
        break

    print()
    time.sleep(1)
