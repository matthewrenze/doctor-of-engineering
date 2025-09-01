import os
from markitdown import MarkItDown

class ReadFileTool:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def execute(self, file_name):
        try:
            file_path = f"{self.folder_path}/{file_name}"
            if not os.path.exists(file_path):
                return f"File {file_name} does not exist."
            markitdown = MarkItDown()
            result = markitdown.convert(file_path)
            text = result.markdown
            if len(text) > 10000:
                text = text[:10000] + "\n\n[...truncated...]"
            return text
        except Exception as e:
            return str(e)

# # DEBUG:
# if __name__ == "__main__":
#     os.getcwd()
#     file_path = "data/evals/gaia/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
#     markitdown = MarkItDown()
#     text = markitdown.convert(file_path)
#     print(text)

