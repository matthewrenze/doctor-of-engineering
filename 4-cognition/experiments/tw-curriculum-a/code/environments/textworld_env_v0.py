import re
import textworld.gym

class TextWorldEnvV0:
    def __init__(self, params, evals):
        self.params = params
        self.evals = evals
        self.env = None
        self.episode = None
        self.episode_id = 0
        self.task = ""
        self.step_index = 0
        self.max_reward = 0.0

    def reset(self, episode_id):
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
        state, infos = self.env.reset()

        # Remove the banner
        state = "\n".join(state.split("\n")[23:])

        self.task = infos.get("objective", "").strip()
        self.step_index = 0
        self.max_reward = infos["max_score"]

        return self.task, state

    def render(self):
        self.env.render()

    def step(self, action: str) -> (str, float, bool):
        # HACK: Fix the "take <object> from floor" issue
        if action.startswith("take "):
            action = action.replace(" from floor", "")

        # Step the environment
        state, reward, is_done, infos = self.env.step(action)

        # Clean up the state
        state = re.sub(r'\n+', '\n', state.strip())
        state = state.rstrip('>')

        # Increment step index
        self.step_index += 1

        # Normalize the reward
        reward = reward / self.max_reward

        # Handle the quit action
        if action == "quit":
            is_done = True

        return state, reward, is_done
