import requests
from bs4 import BeautifulSoup
import markdownify

url = "https://en.wikipedia.org/wiki/Philosophy"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")
    print(markdown_content)

    with open("data/bs4.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)

except requests.RequestException as e:
    print(f"Error fetching the URL: {e}")

