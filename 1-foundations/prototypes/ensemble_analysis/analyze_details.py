import pandas as pd

# Load the dataset
file_path = "all-details.csv"
details = pd.read_csv(file_path)


print(details.head())

# Filter the data
details = details[details["Model Name"] == "gpt-4"]
details = details[details["Exam Name"] == "comprehensive-100"]
details = details[details["Temperature"] == 0.7]

# Count the rows
print(details.shape[0])

# Create six new columns "A", "B", "C", "D", "E", and "NA" initialized to 0
details["A"] = 0
details["B"] = 0
details["C"] = 0
details["D"] = 0
details["E"] = 0
details["NA"] = 0

# For each row, count the number of values contained in columns "Answer 1" to "Answer 10" and store them in the new columns
for index, row in details.iterrows():
    answers = row[["Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5", "Answer 6", "Answer 7", "Answer 8", "Answer 9", "Answer 10"]]

    for answer in answers:
        if answer == "A":
            details.at[index, "A"] += 1
        elif answer == "B":
            details.at[index, "B"] += 1
        elif answer == "C":
            details.at[index, "C"] += 1
        elif answer == "D":
            details.at[index, "D"] += 1
        elif answer == "E":
            details.at[index, "E"] += 1
        else:
            details.at[index, "NA"] += 1

# Convert counts to proportions
details["A"] = details["A"] / 10
details["B"] = details["B"] / 10
details["C"] = details["C"] / 10
details["D"] = details["D"] / 10
details["E"] = details["E"] / 10
details["NA"] = details["NA"] / 10