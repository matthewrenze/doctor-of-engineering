import os
import sys
import re
import yaml
from alfworld.agents.environment.alfred_thor_env import AlfredThorEnv

class AlfWorldThorEnv:
    def __init__(self, evals):
        self.env = None
        self.evals = evals
        self.task = None
        self.step_index = 0
        self.max_reward = 0.0

        # Load the config
        config_file = "/mnt/c/Users/Matthew/Dropbox/School/JHU/DEng/Repository/2-evaluations/exercises/alfworld-agent/data/configs/base_config.yaml"
        with open(config_file) as reader:
            config = yaml.safe_load(reader)

        # Set the task types
        # Note: 1 - Pick & Place, 2 - Examine in Light, 3 - Clean & Place, 4 - Heat & Place, 5 - Cool & Place, 6 - Pick Two & Place
        config["env"]["task_types"] = [6]

        # Setup the environment
        env = AlfredThorEnv(config, train_eval="train")
        env = env.init_env(batch_size=1)
        self.env = env

    def reset(self, task_id):

        # # TODO: Implement task_id handling
        # task = self.evals[task_id]
        # game_file_path = task["file_path"]

        # Reset the environment
        states, infos = self.env.reset()
        state_text = states[0]
        frames = self.env.get_frames()
        frame = frames[0]
        state_image = frame[:, :, ::-1]  # BGR -> RGB
        state = {
            "text": state_text,
            "image": state_image
        }
        self.step_index = 0
        self.max_reward = 1.0

        return state

    def render(self):
        self.env.render()

    def step(self, action: str) -> (str, float, bool):
        actions = [action]
        states, rewards, is_dones, infos = self.env.step(actions)
        state_text = states[0]
        frames = self.env.get_frames()
        frame = frames[0]
        image = frame[:, :, ::-1]  # BGR -> RGB
        state = {
            "text": state_text,
            "image": image
        }
        is_done = is_dones[0]
        reward = 1 if infos["won"][0] else 0
        self.step_index += 1
        return state, reward, is_done
