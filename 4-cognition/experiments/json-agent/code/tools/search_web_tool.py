import os
import json
import requests
from common.cache import Cache

num_results = 5
max_results = 10
file_ext = "json"

class SearchWebTool:

    def __init__(self):
        self.cache = Cache("search")

    def execute(self, query: str) -> dict:

        # Check the cache
        if self.cache.exists(query, file_ext):
            cached_results = self.cache.get(query, file_ext)
            cached_results = json.loads(cached_results)
            top_k_results = cached_results[0:num_results]
            top_k_results = { "results": top_k_results }
            return top_k_results

        try:

            # Create the request
            api_key = os.getenv("GOOGLE_API_KEY")
            cx = os.getenv("GOOGLE_SEARCH_CX")
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "q": query,
                "key": api_key,
                "cx": cx,
                "num": max_results}

            # Get the results
            response = requests.get(url, params=params)
            response_json = response.json()
            results = response_json.get("items", [])

            # Keep only title, url, and snippet
            for result in results:
                result["url"] = result.pop("link", "")
                keys_to_keep = ["title", "url", "snippet"]
                for key in list(result.keys()):
                    if key not in keys_to_keep:
                        result.pop(key)

            # Cache the results
            results_text = json.dumps(results, indent=2)
            self.cache.set(query, file_ext, results_text)

            # Get the top k results
            top_k_results = results[0:num_results]

            # Wrap in a dictionary entry
            top_k_results = { "results": top_k_results }

            return top_k_results

        except Exception as e:
            return { "error": str(e) }


# Test the search engine
if __name__ == "__main__":
    search_query = "Python programming"
    search_engine = SearchWebTool()
    search_results = search_engine.execute(search_query)
    print(search_results)
