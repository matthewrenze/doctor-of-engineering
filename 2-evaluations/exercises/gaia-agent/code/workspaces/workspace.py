import os
import shutil
from common.parameters import Parameters

class Workspace:
    def __init__(self, params: Parameters, episode_id: int):
        self.params = params
        self.folder_name = f"{params.agent_name} - {params.model_name} - {params.eval_name} - {episode_id}"
        self.folder_path = f"../data/workspaces/{self.folder_name}"

    def create(self):
        # Delete the folder if it already exists
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)

        # Create the new folder
        os.makedirs(self.folder_path, exist_ok=True)

    def setup(self, file_names):
        # NOTE: This is a hack to get the root name of the eval
        # TODO: Refactor this to use a more robust method
        eval_root_name = self.params.eval_name.split("-")[0]
        eval_folder_path = f"../data/evals/{eval_root_name}"

        for file_name in file_names:
            eval_file_path = f"{eval_folder_path}/{file_name}"
            if not os.path.exists(eval_file_path):
                raise FileNotFoundError(f"{eval_file_path} does not exist")

            # Copy the file from the eval folder to the workspace
            shutil.copy(eval_file_path, self.folder_path)








