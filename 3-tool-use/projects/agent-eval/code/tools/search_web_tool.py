# Based on https://github.com/Nv7-GitHub/googlesearch
import hashlib
import os
import re
import random
from bs4 import BeautifulSoup
from requests import get
from urllib.parse import unquote

max_results = 5
cache_folder = "../data/cache/search"

class SearchWebTool:

    def execute(self, query: str) -> str:

        # Check the cache
        file_name = re.sub(r"[^a-zA-Z0-9]+", "-", query)
        file_name = file_name.lower()
        file_hash = hashlib.md5(query.encode()).hexdigest()
        file_name = f"{file_name[:64]}-{file_hash[:16]}-{max_results}.md"
        file_path = f"{cache_folder}/{file_name}"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                search_results = file.read()
            return search_results

        # Send search request
        try:
            response = get(
                url="https://www.google.com/search",
                headers={
                    "User-Agent": f"Lynx/{random.randint(2,3)}.{random.randint(8,9)}.{random.randint(0,2)}",
                    "Accept": "*/*"
                },
                params={
                    "q": query,
                    "num": max_results,
                    "hl": "en"
                },
                proxies=None,
                timeout=5,
                verify=None,
                cookies={
                    "CONSENT": "PENDING+987",  # Bypasses the consent page
                    "SOCS": "CAESHAgBEhIaAB",
                }
            )
            response.raise_for_status()

            # Parse response
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("div", class_="ezO2md")

            # Create the output
            output = ""

            # Check if there are results
            for index, result in enumerate(results):

                # Only return top n results
                if index >= max_results:
                    break

                # Find the tags
                link_tag = result.find("a", href=True)
                title_tag = link_tag.find("span", class_="CVA68e") if link_tag else None
                description_tag = result.find("span", class_="FrIlee")

                # Extract the data
                link = unquote(link_tag["href"].split("&")[0].replace("/url?q=", ""))
                title = title_tag.text if title_tag else ""
                snippet = description_tag.text.strip() if description_tag else ""

                # Add to the output
                output += f"Title: {title}\n"
                output += f"URL: {link}\n"
                output += f"Snippet: {snippet}\n\n"

            # Cache the results
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output)

            return output

        except Exception as e:
            return f"Error: {e}"


# Test the search engine
if __name__ == "__main__":

    search_query = "Python programming"
    search_engine = SearchWebTool()
    search_results = search_engine.execute(search_query)
    print(search_results)
