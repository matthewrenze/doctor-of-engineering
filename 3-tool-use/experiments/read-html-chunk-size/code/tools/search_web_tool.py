import os
import re
import hashlib
import requests
from common.console import debug

# num_results = 10
max_results = 10
cache_folder = "../data/cache/search"


class SearchWebTool:
    def __init__(self):
        self.num_results = 5

    def execute(self, query: str) -> str:

        # Check the cache
        base_name = re.sub(r"[^a-zA-Z0-9]+", "-", query)
        base_name = base_name.lower()
        file_hash = hashlib.md5(query.encode()).hexdigest()
        file_name = f"{base_name[:64]}-{file_hash[:16]}.md"
        file_path = f"{cache_folder}/{file_name}"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                cached_results = file.read()
            top_k_results = self.get_top_k_results(cached_results, self.num_results)
            return top_k_results

        try:

            debug("Search cache miss")

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
                ]
                formatted_entries.append("\n".join(entry_lines))

            cached_output = "\n\n".join(formatted_entries)
            if cached_output:
                cached_output += "\n\n"

            # Cache the results
            os.makedirs(cache_folder, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(cached_output)

            top_k_results = self.get_top_k_results(cached_output, self.num_results)
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
