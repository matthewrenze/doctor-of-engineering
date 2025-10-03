import os
import shutil
import requests
from urllib.parse import urlparse, unquote
from common.cache import Cache

class DownloadFileTool:

    def __init__(self, workspace_path: str):
        self.workspace_folder = workspace_path
        self.cache = Cache("downloads")

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
            file_ext = file_ext.lower().lstrip(".")

            # Get the file paths
            cache_file_path = self.cache.get_file_path(url, file_ext)
            workspace_file_path = f"{self.workspace_folder}/{file_name}"

            # Download file, if not cached
            if not self.cache.exists(url, file_ext):

                # Download the file
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
                response.raise_for_status()

                # Save the file
                with open(cache_file_path, 'wb') as file:
                    file.write(response.content)

            # Copy from cache to workspace
            shutil.copyfile(cache_file_path, workspace_file_path)

            # Get the file size
            num_bytes = os.path.getsize(workspace_file_path)

            return f"Downloaded {num_bytes:,} bytes to {file_name}"

        except Exception as e:
            return f"Error downloading file: {e}"


# DEBUG
if __name__ == "__main__":
    workspace_folder = "downloads"
    download_tool = DownloadFileTool(workspace_folder)