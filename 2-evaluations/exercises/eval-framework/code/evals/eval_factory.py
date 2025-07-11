import json

class EvalFactory:

    def create(self, eval_name):
        file_path = f"../data/evals/{eval_name}.jsonl"
        with open(file_path, 'r') as file:
            evals = [json.loads(line) for line in file]
        return evals

# # DEBUG: Load the eval
# factor = EvalFactory()
# evals = factor.create("hotpotqa", 10)
# print(f"Tasks: {len(evals)}")
# print(f"Question 1: {evals[0]["question"]}")

