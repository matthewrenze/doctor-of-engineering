# Read the "test-00000-of-00001.parquet" file and print the first 10 rows
import pandas as pd

table = pd.read_parquet("test-00000-of-00001.parquet")
print(table.head(10))

# Count the number of unique categories
unique_categories = table['category'].nunique()
print(f"Categories: {unique_categories}")

# Count the number of rows by category
category_counts = table['category'].value_counts()
print(f"Category counts:\n{category_counts}")

