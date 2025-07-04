import os
import re
import requests
from bs4 import BeautifulSoup

class LookupTool:

    def execute(self, entity: str, keyword: str) -> str:

        # Check wikipedia page cache first
        cache_folder = "../data/pages"
        cache_file_path = f"{cache_folder}/{entity}.html"
        if os.path.exists(cache_file_path):

            # Read the cached page text
            with open(cache_file_path, "r", encoding="utf-8") as file:
                page_text = file.read()
        else:

            # Get the wikipedia page for the entity
            entity = entity.replace(" ", "+")
            search_url = f"https://en.wikipedia.org/w/index.php?search={entity}"
            response = requests.get(search_url)
            page_text = response.text

        # Save the page text to cache
        with open(cache_file_path, "w", encoding="utf-8") as file:
            file.write(page_text)

        # Parse the page text
        soup = BeautifulSoup(page_text, "html.parser")
        result_divs = soup.find_all("div", {"class": "mw-search-result-heading"})

        # Handle mismatches
        if result_divs:
            result_titles = [clean_text(div.get_text().strip()) for div in result_divs]
            obs = f"Could not find {entity}. Similar: {result_titles[:5]}."
            return obs

        # Get the paragraphs and lists from the page
        page = []
        for tag in soup.find_all("p") + soup.find_all("ul"):
            page.append(tag.get_text().strip())

        # Handle disambiguation pages
        if any("may refer to:" in p for p in page):
            return self.execute("[" + entity + "]", keyword)

        # Clean and filter the paragraphs
        paragraphs = []
        for paragraph in page:
            if len(paragraph.split(" ")) <= 2:
                continue

            paragraph = clean_text(paragraph)
            paragraph = remove_blank_lines(paragraph)
            paragraphs.append(paragraph)

        # Filter paragraphs that contain the keyword
        keyword_paragraphs = []
        for paragraph in paragraphs:
            if keyword.lower() in paragraph.lower():
                keyword_paragraphs.append(paragraph.strip())

        # Handle no matches
        if len(keyword_paragraphs) == 0:
            return f"No matching paragraphs found with keyword '{keyword}' in {entity}."

        # Concatenate the paragraphs
        result = "\n".join(keyword_paragraphs)

        return result

def clean_text(text):
    text = text.encode()
    text = text.decode("unicode-escape")
    text = text.encode("latin1")
    text = text.decode("utf-8")
    return text

def remove_blank_lines(text):
    lines = text.splitlines()
    return "\n".join(line for line in lines if line.strip())


# # DEBUG:
# tool = LookupTool()
# result1 = tool.execute("Johns Hopkins University", "Whiting school Of engineering")
# print(result1)
# print("\n---\n")
# result2 = tool.execute("Colorado orogeny", "eastern sector")
# print(result2)

