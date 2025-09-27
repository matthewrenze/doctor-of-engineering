import re
import requests
import html2text
from bs4 import BeautifulSoup
from common.cache import Cache

window_size = 1000
file_ext = "md"

class FindInHtmlTool:
    def __init__(self):
        self.cache = Cache("html")

    def execute(self, url: str, text: str, match: int):
        try:
            # Handle missing text
            if not text:
                return "Text must be non-empty."

            # Handle optional match
            if match is None:
                match = 1

            # Handle out-of-bounds match
            if match < 1:
                return "Match index must be a 1-based integer."

            # Get markdown from the cache
            if self.cache.exists(url, file_ext):
                markdown = self.cache.get(url, file_ext)

            else:
                # Get the HTML
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
                response.raise_for_status()
                html_content = response.text

                # Handle non-HTML content
                content_type = response.headers.get("Content-Type", "").lower()
                if "text/html" not in content_type and "application/xhtml+xml" not in content_type:
                    return f"Error: URL does not contain HTML. Content-Type: {content_type}"

                # Get the page title
                soup = BeautifulSoup(html_content, "html.parser")
                title = soup.title.get_text(strip=True) if soup.title else "<untitled>"

                # Convert HTML to Markdown
                converter = html2text.HTML2Text()
                converter.body_width = 0
                converter.ignore_links = False
                converter.ignore_images = False
                markdown = converter.handle(html_content)

                # Remove all blank lines
                markdown = re.sub(r"(?m)^\s*\n", "", markdown)

                # Add metadata header
                header = f"Title: {title}\n" + f"URL: {url}\n"
                markdown = header + markdown

                # Save page to cache
                self.cache.set(url, file_ext, markdown)

            # Case-insensitive search
            text_lower = text.lower()
            markdown_lower = markdown.lower()

            # Find all matches
            matches = []
            pos = -1
            while True:
                pos = markdown_lower.find(text_lower, pos + 1)
                if pos == -1:
                    break
                matches.append(pos)

            # Handle no matches
            total_matches = len(matches)
            if total_matches == 0:
                return f"No matches found for '{text}'."

            # Handle out-of-bounds match
            if match > total_matches:
                return f"Match index {match} is out of range. Total matches: {total_matches}."

            # Get the match snippet
            idx = matches[match - 1]
            half = window_size // 2
            start = max(0, idx - half)
            end = min(len(markdown), start + window_size)
            snippet = markdown[start:end]
            footer = f"\n[Match {match} of {total_matches} at location {idx:,}]"
            return snippet + footer

        except Exception as e:
            return f"Error: {str(e)}"
