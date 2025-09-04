import ast
import pandas as pd

data = pd.read_csv("simple_qa_test_set.csv")

data.head()

for index, row in data.iterrows():
    metadata_json = row["metadata"]
    metadata = ast.literal_eval(metadata_json)
    topic = metadata["topic"]
    question = row["problem"]
    answer = row["answer"]
    answer_type = metadata["answer_type"]
    urls = metadata["urls"]

    print(f"ID: {index}")
    print(f"Topic: {topic}")
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    print(f"Answer Type: {answer_type}")
    print(f"URLs:\n  " + "\n  ".join(urls))
    print()