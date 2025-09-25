import requests

# Set the parameters
url = "https://matthewrenze.com/about/resume.pdf"
folder_path = "downloads"

# Get the filename
file_name = url.split("/")[-1]
file_path = f"{folder_path}/{file_name}"

# Download the file
response = requests.get(url)
response.raise_for_status()

# Save the file
with open(file_path, 'wb') as file:
    file.write(response.content)

