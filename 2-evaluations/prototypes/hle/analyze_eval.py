import pandas as pd

# Read the CSV file
eval = pd.read_csv("hle.csv")

# Count the file types
file_types = eval['files'].str.split('.', expand=True)[1].value_counts()
file_types.to_csv("file_types.csv", header=["count"])
print("File types:")
for file_type, count in file_types.items():
    print(f"{file_type}: {count}")
print()

# Count the topics
topic_counts = eval['topic'].value_counts().to_dict()
topic_counts_df = pd.DataFrame(list(topic_counts.items()), columns=['topic', 'count'])
topic_counts_df.to_csv("topics.csv", index=False)
print("Topic:")
for topic, count in topic_counts.items():
    print(f"{topic}: {count}")
print()

# Count the answer types
answer_type_counts = eval['answer_type'].value_counts().to_dict()
answer_type_counts_df = pd.DataFrame(list(answer_type_counts.items()), columns=['answer_type', 'count'])
answer_type_counts_df.to_csv("answer_types.csv", index=False)
print("Answer types:")
for answer_type, count in answer_type_counts.items():
    print(f"{answer_type}: {count}")
print()

