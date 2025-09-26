import re
import math
import requests
import html2text
from bs4 import BeautifulSoup
from common.cache import Cache

page_size = 10000
file_ext = "md"

class ReadHtmlTool:
    def __init__(self):
        self.cache = Cache("html")

    def execute(self, url: str, chunk: int = 1) -> str:

        try:

            # Handle optional chunk parameter
            if chunk is None:
                chunk = 1

            # Check the cache
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
                header = f"Title: {title}\n" \
                    + f"URL: {url}\n"
                markdown = header + markdown

                # Save page to cache
                self.cache.set(url, file_ext, markdown)

            # Calculate total pages
            total_chunks = math.ceil(len(markdown) / page_size)

            # Handle zero-based page index
            if chunk < 1:
                return "Error: Chunk number must be 1 or greater."

            # Handle out-of-range error
            if chunk > total_chunks:
                return f"Error: Chunk {chunk} is out of range. Total chunks: {total_chunks}."

            start = (chunk - 1) * page_size
            end = min(chunk * page_size, len(markdown))
            chunk_text = markdown[start:end]
            footer = f"\n[End of chunk {chunk} of {total_chunks}]"
            return chunk_text + footer

        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    tool = ReadHtmlTool()
    url = "https://matthewrenze.com/"
    chunk = 1
    content = tool.execute(url, chunk)
    print(content)

