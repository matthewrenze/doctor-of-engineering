# Based on https://github.com/Nv7-GitHub/googlesearch

import random
from bs4 import BeautifulSoup
from requests import get
from urllib.parse import unquote

def search(query):

        # Send request
        response = get(
            url="https://www.google.com/search",
            headers={
                "User-Agent": f"Lynx/{random.randint(2,3)}.{random.randint(8,9)}.{random.randint(0,2)}",
                "Accept": "*/*"
            },
            params={
                "q": query,
                "num": 10,
                "hl": "en"
            },
            proxies=None,
            timeout=5,
            verify=None,
            cookies={
                'CONSENT': 'PENDING+987',  # Bypasses the consent page
                'SOCS': 'CAESHAgBEhIaAB',
            }
        )
        response.raise_for_status()

        # Parse
        soup = BeautifulSoup(response.text, "html.parser")
        result_block = soup.find_all("div", class_="ezO2md")

        for result in result_block:

            # Find the tags
            link_tag = result.find("a", href=True)
            title_tag = link_tag.find("span", class_="CVA68e") if link_tag else None
            description_tag = result.find("span", class_="FrIlee")

            # Extract the data
            link = unquote(link_tag["href"].split("&")[0].replace("/url?q=", ""))
            title = title_tag.text if title_tag else ""
            description = description_tag.text.strip() if description_tag else ""

            yield {"title": title, "description": description, "url": link}

results = search("Python programming")

for result in results:
    print(result["title"])
    print(result["description"])
    print(result["url"])
    print()
