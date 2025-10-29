import re
import textworld.gym
from environments.state import State


class TextWorldEnvV1:
    def __init__(self, params, evals):
        self.params = params
        self.evals = evals
        self.env = None
        self.episode = None
        self.episode_id = 0
        self.step_index = 0

    def reset(self, episode_id: int) -> State:
        self.episode_id = episode_id
        self.episode = self.evals.iloc[episode_id].to_dict()
        game_file_path = self.episode["file_path"]

        # Set the env info (what info the player has access to)
        env_infos = textworld.EnvInfos(
            objective=True,
            admissible_commands=True,
            description=True,
            inventory=True,
            feedback=True,
            max_score=True,)

        # Register the game
        env_id = textworld.gym.register_game(
            gamefile=game_file_path,
            request_infos=env_infos,
            max_episode_steps=self.params.max_steps)

        # Create the environment
        self.env = textworld.gym.make(env_id)

        # Reset the environment
        _, infos = self.env.reset()

        # Reset the properties
        self.step_index = 0

        # Get the state info
        task = infos["objective"].strip()
        description = infos["description"].strip()
        location = self.get_location(description)
        inventory = infos["inventory"].strip()
        score = 0
        max_score = infos["max_score"]
        score_text = f"{score} of {max_score}"

        # Clean up the description
        description = self.remove_location(description)

        # Create the state
        state = State(
            task=task,
            feedback="",
            location=location,
            description=description,
            inventory=inventory,
            score=score_text)

        return state

    def render(self):
        self.env.render()

    def step(self, action: str) -> tuple[State, float, bool]:
        # HACK: Fix the "take <object> from floor" issue
        if action.startswith("take "):
            action = action.replace(" from floor", "")

        # Step the environment
        _, score, is_done, infos = self.env.step(action)

        # Get the state info
        feedback = infos["feedback"].strip()
        description = infos["description"].strip()
        location = self.get_location(description)
        inventory = infos["inventory"].strip()
        max_score = infos["max_score"]
        score_text = f"{score} of {max_score}"

        # Clean up the description
        description = self.remove_location(description)

        # Create the state
        state = State(
            task="",
            feedback=feedback,
            location=location,
            description=description,
            inventory=inventory,
            score=score_text)

        # Increment step index
        self.step_index += 1

        # Compute the reward
        reward = score / max_score

        # Handle the quit action
        if action == "quit":
            is_done = True

        return state, reward, is_done

    @staticmethod
    def get_location(description: str) -> str:
        match = re.search(r'-= (.*?) =-', description)
        return match.group(1).strip()

    @staticmethod
    def remove_location(description: str) -> str:
        return re.sub(r'-= (.*?) =-', '', description).strip()
