import os
import re
import hashlib

root_path = "../data/cache"

class FileCache:
    def __init__(self, folder_name: str):
        self.folder_path = f"{root_path}/{folder_name}"

    def exists(self, key: str, ext: str) -> bool:
        file_path = self._get_file_path(key, ext)
        return os.path.exists(file_path)

    def get(self, key, ext: str) -> str:
        file_path = self._get_file_path(key, ext)
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def set(self, key: str, ext: str, value: str):
        os.makedirs(self.folder_path, exist_ok=True)
        file_path = self._get_file_path(key, ext)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(value)

    def _get_file_path(self, key: str, ext: str) -> str:
        base_name = re.sub(r"https?://", "", key)
        base_name = re.sub(r"[^a-zA-Z0-9]+", "-", base_name)
        base_name = base_name.lower()
        key_hash = hashlib.md5(key.encode()).hexdigest()
        file_name = f"{base_name[:64]}-{key_hash[:16]}.{ext}"
        return f"{self.folder_path}/{file_name}"