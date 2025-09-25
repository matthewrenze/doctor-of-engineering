import os
import re
import hashlib

root_path = "../data/cache"

class Cache:
    def __init__(self, folder_name: str, file_ext: str):
        self.folder_path = f"{root_path}/{folder_name}"
        self.file_ext = file_ext

    def exists(self, key: str) -> bool:
        file_path = self._get_file_path(key)
        return os.path.exists(file_path)

    def get(self, key):
        file_path = self._get_file_path(key)
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def set(self, key, value):
        os.makedirs(self.folder_path, exist_ok=True)
        file_path = self._get_file_path(key)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(value)

    def _get_file_path(self, key: str) -> str:
        base_name = re.sub(r"https?://", "", key)
        base_name = re.sub(r"[^a-zA-Z0-9]+", "-", base_name)
        base_name = base_name.lower()
        key_hash = hashlib.md5(key.encode()).hexdigest()
        file_name = f"{base_name[:64]}-{key_hash[:16]}.{self.file_ext}"
        return f"{self.folder_path}/{file_name}"