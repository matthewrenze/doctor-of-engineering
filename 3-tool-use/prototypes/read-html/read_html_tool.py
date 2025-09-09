import os
import re
import math
import hashlib
import requests
import html2text
from bs4 import BeautifulSoup

page_size = 10000
cache_folder_path = "data/cache"

class ReadHtmlTool:
    def execute(self, url: str, page: int = 1) -> str:

        # Create the file path
        base_name = re.sub(r"https?://", "", url)
        base_name = re.sub(r"[^a-zA-Z0-9]+", "-", base_name)
        base_name = base_name.lower()
        url_hash = hashlib.md5(url.encode()).hexdigest()
        file_name = f"{base_name[:64]}-{url_hash[:16]}-{page}.md"
        file_path = f"{cache_folder_path}/{file_name}"

        # Check the cache
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                cached_page = file.read()
            return cached_page

        try:
            # Get the HTML
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            html_content = response.text

            # Get the page title
            soup = BeautifulSoup(html_content, "html.parser")
            title = soup.title.get_text(strip=True) if soup.title else "<untitled>"

            # Convert HTML to Markdown
            converter = html2text.HTML2Text()
            converter.body_width = 0
            converter.ignore_links = False
            converter.ignore_images = False
            markdown = converter.handle(html_content)

            # Calculate total pages
            total_pages = math.ceil(len(markdown) / page_size)

            # Create the pages
            for i in range(1, total_pages + 1):
                start = (i - 1) * page_size
                end = min(i * page_size, len(markdown))
                chunk = markdown[start:end]
                header = f"Title: {title}\n" \
                    + f"URL: {url}\n" \
                    + f"Page {i} of {total_pages}\n\n"
                content = header + chunk

                # Save page to cache
                file_name = f"{base_name[:64]}-{url_hash[:16]}-{i}.md"
                with open(f"{cache_folder_path}/{file_name}", "w", encoding="utf-8") as file:
                    file.write(content)

            # Handle zero-based page index
            if page == 0:
                return "Error: Page number must be 1 or greater."

            # Handle out-of-range error
            if page > total_pages:
                return f"Error: Page {page} is out of range. Total pages: {total_pages}."

            # Return the requested page
            requested_file_name = f"{base_name[:64]}-{url_hash[:16]}-{page}.md"
            requested_file_path = f"{cache_folder_path}/{requested_file_name}"
            with open(requested_file_path, "r", encoding="utf-8") as file:
                return file.read()

        except requests.exceptions.RequestException as e:
            return(f"Error reading {url}: {e}")

if __name__ == "__main__":
    tool = ReadHtmlTool()
    url = "https://matthewrenze.com/articles"
    page = 1
    content = tool.execute(url, 7)
    print(content)

