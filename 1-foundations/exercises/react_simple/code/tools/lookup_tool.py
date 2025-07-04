import re
import requests
from bs4 import BeautifulSoup

class LookupTool:

    def execute(self, entity: str, keyword: str) -> str:

        # Get the wikipedia page for the entity
        entity = entity.replace(" ", "+")
        search_url = f"https://en.wikipedia.org/w/index.php?search={entity}"
        response_text = requests.get(search_url).text
        soup = BeautifulSoup(response_text, "html.parser")
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
            paragraphs.append(paragraph)

        # Parse the paragraphs into sentences
        sentences = []
        for paragraph in paragraphs:
            sentences += paragraph.split(". ")
        sentences = [s.strip() + "." for s in sentences if s.strip()]

        # Filter sentences that contain the keyword
        keyword_sentences = []
        for sentence in sentences:
            if keyword.lower() in sentence.lower():
                keyword_sentences.append(sentence.strip())

        # Concatenate the sentences
        result = "\n".join(keyword_sentences)

        return result

def clean_text(text):
    text = text.encode()
    text = text.decode("unicode-escape")
    text = text.encode("latin1")
    text = text.decode("utf-8")
    return text


# # DEBUG:
# tool = LookupTool()
# result1 = tool.execute("Johns Hopkins University", "Whiting school Of engineering")
# print(result1)
# print("\n---\n")
# result2 = tool.execute("Colorado orogeny", "eastern sector")
# print(result2)

