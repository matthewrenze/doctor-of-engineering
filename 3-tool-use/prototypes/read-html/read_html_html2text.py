import requests
import html2text

url = "https://en.wikipedia.org/wiki/Philosophy"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    html_content = response.text
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False

    markdown_content = converter.handle(html_content)
    print(markdown_content)

    # Save to disk
    with open("data/html2text.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")


