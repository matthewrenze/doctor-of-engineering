import requests


def get_extension(url):
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get('Content-Type', '').lower()

        if '/' not in content_type:
            return ".txt"

        ext = content_type.split('/')[-1].split(';')[0]
        if ext == 'plain':
            return '.txt'
        elif ext == 'jpeg':
            return '.jpg'
        else:
            return f'.{ext}'

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return '.bin'

# DEBUG
if __name__ == "__main__":
    print(get_extension("https://matthewrenze.com/about/resume.pdf"))
    print(get_extension("https://httpbin.org/image/png"))
    print(get_extension("https://httpbin.org/image/jpeg"))
    print(get_extension("https://httpbin.org/image/html"))
    print(get_extension("https://httpbin.org/robots.txt"))
    print(get_extension("https://jsonplaceholder.typicode.com/posts/1"))
