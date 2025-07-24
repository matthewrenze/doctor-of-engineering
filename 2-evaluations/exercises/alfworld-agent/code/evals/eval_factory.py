import json

class EvalFactory:

    def create(self, eval_name):
        file_path = f"../data/evals/{eval_name}.jsonl"
        with open(file_path, 'r') as file:
            evals = [json.loads(line) for line in file]
        return evals

if __name__ == '__main__':
    eval_factory = EvalFactory()
    evals = eval_factory.create("textworld-1")
    print(f"Evals: {len(evals)}")
    for eval in evals:
        print(eval)

