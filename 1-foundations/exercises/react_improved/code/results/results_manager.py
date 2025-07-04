import pandas as pd
from results.result_row import ResultRow

class ResultsManager:
    def __init__(self):
        self.results = pd.DataFrame()

    def create(self):
        return ResultRow()

    def add(self, row):
        self.results = self.results._append(row.__dict__, ignore_index=True)

    def get_table(self):
        return self.results

    def save(self):
        agent_name = self.results["agent_name"].iloc[0]
        model_name = self.results["model_name"].iloc[0]
        eval_name = self.results["eval_name"].iloc[0]
        file_path = f"../data/results/{agent_name} - {model_name} - {eval_name}.csv"
        self.results.to_csv(file_path, index=False)



