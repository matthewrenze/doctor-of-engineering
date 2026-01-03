import re
import textworld.gym
from states.env_state import EnvState

class TextWorldEnv:
    def __init__(self, params, evals):
        self.params = params
        self.evals = evals
        self.env = None
        self.episode = None
        self.episode_id = 0
        self.step_index = 0

    def reset(self, episode_id: int) -> tuple[str, EnvState]:
        self.episode_id = episode_id
        self.episode = self.evals.iloc[episode_id - 1].to_dict()
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

        # Clean up the description
        description = self.remove_location(description)
        description = self.clean_text(description)

        # Create the state
        state = EnvState(
            feedback="",
            location=location,
            description=description,
            inventory=inventory,
            score=score,
            max_score=max_score,
            reward=0,
            max_reward=1.0,
            is_done=False)

        return task, state

    def render(self):
        self.env.render()

    def step(self, action: str) -> EnvState:
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
        reward = score / max_score

        # Clean up the descriptions
        feedback = self.remove_location(feedback)
        feedback = self.clean_text(feedback)
        description = self.remove_location(description)
        description = self.clean_text(description)

        # Handle the quit action
        if action == "quit":
            is_done = True

        # Create the state
        state = EnvState(
            feedback=feedback,
            location=location,
            description=description,
            inventory=inventory,
            score=score,
            max_score=max_score,
            reward=reward,
            max_reward=1.0,
            is_done=is_done)

        # Increment step index
        self.step_index += 1

        return state

    @staticmethod
    def get_location(description: str) -> str:
        match = re.search(r'-= (.*?) =-', description)
        return match.group(1).strip()

    @staticmethod
    def remove_location(description: str) -> str:
        return re.sub(r'-= (.*?) =-', '', description).strip()

    @staticmethod
    def clean_text(text):
        text = re.sub(r'\n+', '\n', text)
        text = re.sub('\n', ' ', text)
        text = re.sub(r'(?<!^)\s+', ' ', text)
        return text
