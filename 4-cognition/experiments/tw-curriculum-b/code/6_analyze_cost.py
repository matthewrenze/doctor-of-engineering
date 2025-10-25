import pandas as pd

# Set parameters
input_file_path = "../data/summaries.csv"

# Load the data
summaries = pd.read_csv(input_file_path)

# Filter the rows
# summaries = summaries[summaries["eval_name"].str.endswith("-100")]

# Group by model and sum the cost
# Note: only two decimal places for cost
cost_by_model = summaries \
    .groupby("model_name")["total_cost"] \
    .sum() \
    .reset_index()
cost_by_model["total_cost"] = cost_by_model["total_cost"].round(2)
cost_by_model = cost_by_model.sort_values(by="total_cost", ascending=False)
print("Cost by model:")
print(cost_by_model.to_string(index=False))
print()

# Sum the cost
total_cost = summaries["total_cost"].sum()
print(f"Total cost: ${total_cost:.2f}")
print()