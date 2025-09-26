import os
import requests
from common.cache import Cache

num_results = 10
max_results = 10
file_ext = "md"

class SearchWebTool:

    def __init__(self):
        self.cache = Cache("search")

    def execute(self, query: str) -> str:

        # Check the cache
        if self.cache.exists(query, file_ext):
            cached_results = self.cache.get(query, file_ext)
            top_k_results = self.get_top_k_results(cached_results, num_results)
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

            # Create the output
            formatted_entries = []
            for result in results[:max_results]:
                entry_lines = [
                    f'Title: {result.get("title", "")}',
                    f'URL: {result.get("link", "")}',
                    f'Snippet: {result.get("snippet", "")}',
                ]
                formatted_entries.append("\n".join(entry_lines))

            # Format the entries
            cached_output = "\n\n".join(formatted_entries)
            if cached_output:
                cached_output += "\n\n"

            # Cache the results
            self.cache.set(query, file_ext, cached_output)

            # Get the top k results
            top_k_results = self.get_top_k_results(cached_output, num_results)

            return top_k_results

        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_top_k_results(raw_output: str, limit: int) -> str:
        if not raw_output or limit <= 0:
            return ""
        entries = [entry for entry in raw_output.strip().split("\n\n") if entry.strip()]
        limited_entries = entries[:limit]
        if not limited_entries:
            return ""
        return "\n\n".join(limited_entries) + "\n\n"


# Test the search engine
if __name__ == "__main__":
    search_query = "Python programming"
    search_engine = SearchWebTool()
    search_results = search_engine.execute(search_query)
    print(search_results)
