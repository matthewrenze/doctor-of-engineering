import os
import pandas as pd
from common.parameters import Parameters
from summaries.summary_row import SummaryRow

class SummaryManager:

    def __init__(self):
        self.file_path = "../data/summaries.csv"
        self.summaries = None

    def load(self):
        if not os.path.exists(self.file_path):
            self.summaries = pd.DataFrame()
        else:
            self.summaries = pd.read_csv(self.file_path)

    def exists(self, params: Parameters):
        if self.summaries is None or self.summaries.empty:
            return False

        agent_matches = self.summaries["agent_name"] == params.agent_name
        model_matches = self.summaries["model_name"] == params.model_name
        eval_matches = self.summaries["eval_name"] == params.eval_name
        all_matches = self.summaries[agent_matches & model_matches & eval_matches]

        return not all_matches.empty

    def summarize(self, results):
        summary = SummaryRow()
        summary.agent_name = results["agent_name"].iloc[0]
        summary.model_name = results["model_name"].iloc[0]
        summary.eval_name = results["eval_name"].iloc[0]
        summary.tasks = len(results)
        summary.successes = results["reward"].sum()
        summary.failures = len(results[results["reward"] == 0])
        summary.errors = len(results[results["error"] != ""])
        summary.accuracy = summary.successes / summary.tasks if summary.tasks > 0 else 0
        summary.total_reward = results["reward"].sum()
        summary.total_steps = results["steps"].sum()
        summary.input_tokens = results["input_tokens"].sum()
        summary.output_tokens = results["output_tokens"].sum()
        summary.total_tokens = results["total_tokens"].sum()
        summary.avg_reward_per_task = summary.total_reward / summary.tasks if summary.tasks > 0 else 0
        summary.avg_reward_per_step = summary.total_reward / summary.total_steps if summary.total_steps > 0 else 0
        summary.avg_reward_per_token = (summary.total_reward / summary.total_tokens) if summary.total_tokens > 0 else 0
        return summary

    def add(self, summary):
        self.summaries = self.summaries._append(summary.__dict__, ignore_index=True)

    def save(self):
        try:
            self.summaries.sort_values(by=["agent_name", "model_name", "eval_name"], inplace=True)
            self.summaries.to_csv(self.file_path, index=False)
        except Exception as e:
            print(f"ERROR: Summary file is locked. Saving to temporary file.")
            date_time = pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")
            temp_file_path = f"../data/summaries-{date_time}.csv"
            self.summaries.to_csv(temp_file_path, index=False)
