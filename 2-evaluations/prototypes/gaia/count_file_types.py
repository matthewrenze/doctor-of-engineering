import pandas as pd

input_file_path = "raw/gaia_val.csv"
output_file_path = "file-type-counts.csv"

# Load the CSV file
eval = pd.read_csv(input_file_path)

# Count the number of file types (file extensions in the "file_name" column)
file_types = eval["file_name"].str.split(".", expand=True).iloc[:, -1].value_counts().reset_index()

# Name the columns
file_types.columns = ["File Type", "Count"]

# Sort by file types
file_types = file_types.sort_values(by="Count", ascending=False)

# Save the file types to a new CSV file
file_types.to_csv(output_file_path, index=False, encoding="utf-8")

# Print the file types
print("File types:")
print(file_types)



