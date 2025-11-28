import os
import pandas as pd
from details.details_row import DetailsRow
from common.parameters import Parameters

class DetailsManager:
    def __init__(self, params: Parameters, episode_id: int):
        self.folder_path = "../data/details"
        self.details = pd.DataFrame()
        self.params = params
        self.episode_id = episode_id

    def create(self):
        row = DetailsRow()
        return row

    def add(self, row):
        self.details = self.details._append(row.__dict__, ignore_index=True)

    def get_table(self):
        return self.details

    def save(self):
        # Create the folder path
        agent_name = self.params.agent_name
        model_name = self.params.model_name
        eval_name = self.params.eval_name
        episode_id = self.episode_id
        subfolder_name = f"{agent_name} - {model_name} - {eval_name}"
        subfolder_path = f"{self.folder_path}/{subfolder_name}"

        # Create the folder if it doesn't exist
        os.makedirs(subfolder_path, exist_ok=True)

        # Create the file path
        file_name = f"{episode_id + 1}.csv"
        file_path = f"{subfolder_path}/{file_name}"

        # Save the details
        self.details.to_csv(file_path, index=False)
