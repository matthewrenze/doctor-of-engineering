import sys
from alfworld.agents.environment.alfred_tw_env import AlfredTWEnv
import alfworld.agents.modules.generic as generic


class CustomAlfredTWEnv(AlfredTWEnv):
    def __init__(self, config, train_eval="train"):
        super().__init__(config, train_eval)

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


# HACK: to load config file
sys.argv = ["hello_alfworld.py", "base_config.yaml"]

# Load the config
config = generic.load_config()

# Set the task types
# Note: 1 - Pick & Place, 2 - Examine in Light, 3 - Clean & Place, 4 - Heat & Place, 5 - Cool & Place, 6 - Pick Two & Place
config["env"]["task_types"] = [1]

# Setup the environment
env = AlfredTWEnv(config, train_eval="train")
env = env.init_env(batch_size=1)

# Reset the environment
task_file = "/home/matthew/.cache/alfworld/json_2.1.1/train/pick_and_place_simple-Candle-None-Toilet-409/trial_T20190908_014219_052080/traj_data.json"
state, infos = env.reset(task_file)
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
