import pandas as pd
from common.parameters import Parameters

class EvalFactory:

    def create(self, params: Parameters):
        if params.eval_name.startswith("tw-curriculum-"):
            file_path = f"../data/evals/tw-curriculum/{params.eval_name}.jsonl"
            eval = pd.read_json(file_path, lines=True)
            return eval
        else:
            raise ValueError(f"Unknown eval name: {params.eval_name}")


# # DEBUG: Load the eval
# factor = EvalFactory()
# evals = factor.create("hotpotqa", 10)
# print(f"Tasks: {len(evals)}")
# print(f"Question 1: {evals[0]["question"]}")

