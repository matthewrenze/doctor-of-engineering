import os
import requests
from urllib.parse import unquote

num_results = 5

class SearchWebTool:

    def execute(self, query: str) -> str:

        try:

            # Create the request
            api_key = os.getenv("GOOGLE_SEARCH_KEY")
            cx = os.getenv("GOOGLE_SEARCH_CX")
            url = f"https://www.googleapis.com/customsearch/v1"
            params = {
                "q": query,
                "key": api_key,
                "cx": cx,
                "num": num_results}

            # Get the results
            response = requests.get(url, params=params)
            response_json = response.json()
            results = response_json.get("items", [])            

            # Create the output
            output = ""

            # Check if there are results
            for index, result in enumerate(results):

                # Only return top n results
                if index >= num_results:
                    break

                # Add to the output
                output += f"Title: {result["title"]}\n"
                output += f"URL: {result["link"]}\n"
                output += f"Snippet: {result["snippet"]}\n\n"

            return output

        except Exception as e:
            return f"Error: {e}"


# Test the search engine
if __name__ == "__main__":

    search_query = "Python programming"
    search_engine = SearchWebTool()
    search_results = search_engine.execute(search_query)
    print(search_results)
