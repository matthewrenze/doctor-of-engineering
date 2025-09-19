import os
import requests

api_key = os.getenv("BRAVE_SEARCH_API_KEY")
query = "Python programming"
num_results = 5

url = "https://api.search.brave.com/res/v1/web/search"
headers = {
    "Accept": "application/json",
    "X-Subscription-Token": api_key,
}
params = {"q": query, "count": num_results}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for item in data.get("web", {}).get("results", []):
    print(f"Title: {item["title"]}")
    print(f"URL: {item["url"]}")
    print(f"Snippet: {item["description"]}")
    print()
