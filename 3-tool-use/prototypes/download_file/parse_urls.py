import os
from urllib.parse import urlparse, unquote

def get_file_name(url):

    # Parse from URL
    path = urlparse(url).path
    file_name = os.path.basename(path)
    file_name = unquote(file_name)

    # Handle no filename
    if not file_name:
        file_name = "download"

    # Handle no extension
    if '.' not in file_name:
        file_name += ".bin"

    return file_name

# Simple direct file
print(get_file_name("https://example.com/files/report.pdf"))

# File with query string
print(get_file_name("https://example.com/download?id=12345"))

# File with query string and extension
print(get_file_name("https://example.com/assets/data.csv?version=2"))

# File with fragment
print(get_file_name("https://example.com/archive/file.zip#section1"))

# Encoded characters in filename
print(get_file_name("https://example.com/files/My%20Resume.docx"))

# URL ending with a slash (no filename in path)
print(get_file_name("https://example.com/downloads/"))

# Hidden file with no extension
print(get_file_name("https://example.com/.hiddenfile"))

# Nested path
print(get_file_name("https://example.com/path/to/images/photo.jpg"))

# File with multiple dots
print(get_file_name("https://example.com/music/song.name.final.mp3"))

# Non-ASCII characters in filename
print(get_file_name("https://example.com/files/résumé.pdf"))

# No filename at all
print(get_file_name("https://example.com"))

