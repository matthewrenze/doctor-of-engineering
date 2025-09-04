# NOTE: This version uses pip install google

# Import the libraries
from googlesearch import search

# Define the search query
query = "Python programming"

# Get the search results
results = search(query)

# Print the search results
for result in results:
    print(result)
