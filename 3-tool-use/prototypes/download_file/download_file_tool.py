import os
import requests
from urllib.parse import urlparse, unquote

folder_path = "downloads"

class DownloadFileTool:
    def __init__(self, workspace_folder: str):
        self.workspace_folder = workspace_folder
        pass

    def execute(self, url: str):

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

        # Save the file
        with open(file_path, 'wb') as file:
            file.write(response.content)
