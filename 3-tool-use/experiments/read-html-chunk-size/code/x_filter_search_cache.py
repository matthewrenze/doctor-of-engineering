import os
import glob

cache_folder_path = "../data/cache/search"

for path in glob.glob(os.path.join(cache_folder_path, "*.md")):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = [ln for ln in lines if not ln.lstrip().startswith("Snippet:")]

    if new_lines != lines:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
