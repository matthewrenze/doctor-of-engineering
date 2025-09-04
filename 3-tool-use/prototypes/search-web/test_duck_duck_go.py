import requests

query = "Python programming"
url = "https://api.duckduckgo.com/"
params = {
    "q": query,
    "format": "json",
    "no_redirect": 1,
    "no_html": 1}
num_results = 5

results = []

response = requests.get(url, params=params)

if response.status_code == 200 or response.status_code == 202:
    data = response.json()
    results = data.get("Results", [])[:num_results]
else:
    print("Error:", response.status_code, response.text)

# Display results
for idx, result in enumerate(results):
    if "Text" in result and "FirstURL" in result:
        print(f"{idx+1}. {result['Text']}")
        print(f"   URL: {result['FirstURL']}\n")
