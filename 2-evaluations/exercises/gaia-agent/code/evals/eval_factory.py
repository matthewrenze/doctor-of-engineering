import pandas as pd
from common.parameters import Parameters

class EvalFactory:

    def create(self, params: Parameters):
        file_path = f"../data/evals/{params.eval_name}.csv"
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            raise ValueError(f"Eval file not found: {file_path}")


# # DEBUG: Load the eval
# factor = EvalFactory()
# evals = factor.create("hotpotqa", 10)
# print(f"Tasks: {len(evals)}")
# print(f"Question 1: {evals[0]["question"]}")

