import pandas as pd

input_file_path = "raw/gaia_val.csv"
output_file_path = "difficulty-levels.csv"

# Load the CSV file
eval = pd.read_csv(input_file_path)

# Count the number of levels
levels = eval["Level"].value_counts().reset_index()
levels.columns = ["Level", "Count"]

# Save the levels to a new CSV file
levels.to_csv(output_file_path, index=False, encoding="utf-8")

# Sort by level
levels = levels.sort_values(by="Level")

# Print the levels
print("Levels:")
print(levels)



