import os
import requests

API_KEY = os.getenv("GOOGLE_API_KEY")
CX = os.getenv("GOOGLE_SEARCH_CX")
query = "Python Programming"
num_results = 5
url = f"https://www.googleapis.com/customsearch/v1"
params = {
    "q": query,
    "key": API_KEY,
    "cx": CX,
    "num": num_results}

response = requests.get(url, params=params)
data = response.json()

for item in data.get("items", []):
    print(f"Title: {item["title"]}")
    print(f"URL: {item["link"]}")
    print(f"Snippet: {item["snippet"]}\n")
