import math
import requests
import html2text

url = "https://en.wikipedia.org/wiki/Philosophy"
page_size = 10000

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    html_content = response.text
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False

    markdown = converter.handle(html_content)

    total_pages = math.ceil(len(markdown) / page_size - 1)

    for i in range(1, total_pages + 1):
        start = (i - 1) * page_size
        end = min(i * page_size, len(markdown))
        chunk = markdown[start:end]
        print(f"\n\n--- Page {i} of {total_pages} ---\n\n")
        print(chunk)

        # Save to disk
        file_name = f"page_{i}.md"
        with open(f"data/pages/{file_name}", "w", encoding="utf-8") as file:
            file.write(chunk)

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")


