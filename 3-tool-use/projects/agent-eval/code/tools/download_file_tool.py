import os
import requests
from urllib.parse import urlparse, unquote
from common.file_cache import FileCache

class DownloadFileTool:

    def __init__(self, workspace_folder: str):
        self.workspace_folder = workspace_folder
        self.cache = FileCache("downloads")

    def execute(self, url: str):

        try:

            # Parse from URL
            path = urlparse(url).path
            file_name = os.path.basename(path)
            file_name = unquote(file_name)

            # Handle no filename
            if not file_name:
                file_name = "download.txt"

            # Handle no extension
            if '.' not in file_name:
                file_name += ".txt"

            # Get the file extension
            _, file_ext = os.path.splitext(file_name)

            # Download the file
            response = requests.get(url)
            response.raise_for_status()

            # Create the file path
            file_path = f"{self.workspace_folder}/{file_name}"

            # Get the number of bytes downloaded
            num_bytes = len(response.content)

            # Save the file
            with open(file_path, 'wb') as file:
                file.write(response.content)

            return f"Downloaded {num_bytes:,} bytes to {file_name}"

        except Exception as e:
            return f"Error downloading file: {e}"


# DEBUG
if __name__ == "__main__":
    workspace_folder = "downloads"
    download_tool = DownloadFileTool(workspace_folder)