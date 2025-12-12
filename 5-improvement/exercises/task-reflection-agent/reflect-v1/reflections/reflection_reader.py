import os
from common.parameters import Parameters

class ReflectionReader:
    def read(self, params: Parameters, episode_id: int) -> str:

        # Create the paths
        agent_name = params.agent_name.replace("-test", "-train")
        folder_path = f"../data/reflections/{agent_name} - {params.model_name} - {params.eval_name}"
        file_path = f"{folder_path}/{episode_id}.txt"

        # Return empty string if file does not exist
        if not os.path.exists(file_path):
            return ""

        # Read the reflection
        with open(file_path, "r") as file:
            reflection = file.read().strip()

        return reflection