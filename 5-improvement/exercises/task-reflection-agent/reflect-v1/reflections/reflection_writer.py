import os
from common.parameters import Parameters

class ReflectionWriter:
    def write(self, params: Parameters, episode_id: int, reflection: str):

        # Create the folder
        folder_path = f"../data/reflections/{params.agent_name} - {params.model_name} - {params.eval_name}"
        os.makedirs(folder_path, exist_ok=True)

        # Write the reflection
        file_path = f"{folder_path}/{episode_id}.txt"
        with open(file_path, "w") as file:
            file.write(reflection + '\n')