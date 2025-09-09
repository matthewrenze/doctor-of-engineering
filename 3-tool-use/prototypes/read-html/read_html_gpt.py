import os
import requests
import html2text
from openai import AzureOpenAI

CLEANER_PROMPT = """
# Role 
 - You are a webpage cleaner.
 - Your task is to clean the markdown text of a webpage.
 - Your goal is to remove any unnecessary elements while preserving the essential information.

# Instructions
1. Preserve key structural elements
 - retrain all headings (#, ##, ###, etc.), paragraphs, lists, tables, blockquotes, and code blocks.
 - Ensure the hierarchy and formatting remain intact
2. Keep relevant content
 - Ensure the main body text, articles, blog content, documentation, and other relevant content are preserved.
 - Maintain inline formatting (bold, italics, links, code, etc.) where necessary for readability.
 - Do not alter factual information or rewrite content -- only remove irrelevant elements.
3. Remove unnecessary elements
 - Remove ads, banners, pop-ups, promotions, etc.
 - Remove navigation menus, sidebars, and footers.
 - Remove any copyright notices, social media buttons, or unrelated links.
 - Remove any inline scripts, tracking codes, or unrelated metadata.
4. Enhance readability
 - Fix broken markdown or spacing issues
 - Remove redundant blank lines while keeping necessary paragraph separation.
 - Convert malformed markdown to proper formatting. 
"""

CLEANER_EXAMPLE_PROMPT = """
# Article Title  

**Welcome to our website!**  

[Subscribe to our newsletter](#)  

## Introduction  
This article explains how LLMs work.  

---  
### Sponsored Content  
[Buy AI courses now](#)  

## How LLMs Work  
Large language models are trained on vast amounts of text data.  

#### Advertisement  
[Click here for a special offer!](#)  

### Conclusion  
LLMs are powerful tools for AI research.  

© 2024 AI News. All rights reserved.  
"""

CLEANER_EXAMPLE_RESPONSE = """
# Article Title  

## Introduction  
This article explains how LLMs work.  

## How LLMs Work  
Large language models are trained on vast amounts of text data.  

### Conclusion  
LLMs are powerful tools for AI research.
"""

url = "https://en.wikipedia.org/wiki/Philosophy"

# Fetch the HTML
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()

# Convert HTML to Markdown
html_content = response.text
converter = html2text.HTML2Text()
converter.ignore_links = False
converter.ignore_images = False
markdown_content = converter.handle(html_content)

print(markdown_content)
print("\n\n===================================================")
print("===================================================")
print("===================================================\n\n")

# Create the messages
messages = [
    {"role": "system", "content": CLEANER_PROMPT},
    {"role": "user", "content": CLEANER_EXAMPLE_PROMPT},
    {"role": "assistant", "content": CLEANER_EXAMPLE_RESPONSE},
    {"role": "user", "content": markdown_content}]

# Create the client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_URL"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01")

# Get the response from the API
api_response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    temperature=0.0)

# Extract the content
content = api_response.choices[0].message.content.strip()
print(content)

# Save
with open("data/gpt.md", "w", encoding="utf-8") as file:
    file.write(content)