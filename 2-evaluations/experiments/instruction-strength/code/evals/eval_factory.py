class EvalFactory:

    def create(self, eval_name):
        file_path = f"../data/evals/{eval_name}.txt"
        eval = []
        with open(file_path, 'r') as file:
            for line in file:
                eval.append(line.strip())
        return eval

# # DEBUG: Load the eval
# factor = EvalFactory()
# evals = factor.create("if-eval-10")
# print(f"Tasks: {len(evals)}")
# print(f"Task 1: {evals[0]}")

