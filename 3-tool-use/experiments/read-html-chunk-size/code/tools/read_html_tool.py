import os
import re
import math
import hashlib
import requests
import html2text
from bs4 import BeautifulSoup
from common.console import debug

# page_size = 10000
timeout = 30
cache_folder_path = "../data/cache/html"

class ReadHtmlTool:
    def __init__(self, chunk_size):
        self.chunk_size = chunk_size * 1000

    def execute(self, url: str, chunk: int = 1) -> str:

        try:

            # Handle optional chunk parameter
            if chunk is None:
                chunk = 1

            # Create the cache file path
            base_name = re.sub(r"https?://", "", url)
            base_name = re.sub(r"[^a-zA-Z0-9]+", "-", base_name)
            base_name = base_name.lower()
            url_hash = hashlib.md5(url.encode()).hexdigest()
            file_name = f"{base_name[:64]}-{url_hash[:16]}.md"
            file_path = f"{cache_folder_path}/{file_name}"

            # Check the cache
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    markdown = file.read()
            else:

                debug("HTML cache miss")

                # Handle pdf files
                if url.lower().endswith(".pdf"):
                    return "Error: PDF files are not supported by the read_html tool."

                # Get the HTML
                response = requests.get(
                    url,
                    headers={"User-Agent": "Mozilla/5.0"},
                    timeout=timeout)
                response.raise_for_status()

                # Handle non-HTML content
                content_type = response.headers.get("Content-Type", "").lower()
                if "text/html" not in content_type and "application/xhtml+xml" not in content_type:
                    return f"Error: URL does not contain HTML. Content-Type: {content_type}"

                # Get the page title
                html_content = response.text
                soup = BeautifulSoup(html_content, "html.parser")
                title = soup.title.get_text(strip=True) if soup.title else "<untitled>"

                # Convert HTML to Markdown
                converter = html2text.HTML2Text()
                converter.body_width = 0
                converter.ignore_links = False
                converter.ignore_images = False
                markdown = converter.handle(html_content)

                # Add metadata header
                header = f"Title: {title}\n" \
                    + f"URL: {url}\n\n"
                markdown = header + markdown

                # Save page to cache
                file_name = f"{base_name[:64]}-{url_hash[:16]}.md"
                with open(f"{cache_folder_path}/{file_name}", "w", encoding="utf-8") as file:
                    file.write(markdown)

            # Calculate total pages
            total_chunks = math.ceil(len(markdown) / self.chunk_size)

            # Handle zero-based page index
            if chunk < 1:
                return "Error: Chunk number must be 1 or greater."

            # Handle out-of-range error
            if chunk > total_chunks:
                return f"Error: Chunk {chunk} is out of range. Total chunks: {total_chunks}."

            start = (chunk - 1) * self.chunk_size
            end = min(chunk * self.chunk_size, len(markdown))
            chunk_text = markdown[start:end]
            footer = f"\n\n[End of chunk {chunk} of {total_chunks}]"
            return chunk_text + footer

        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    tool = ReadHtmlTool()
    url = "https://matthewrenze.com/"
    chunk = 1
    content = tool.execute(url, chunk)
    print(content)

