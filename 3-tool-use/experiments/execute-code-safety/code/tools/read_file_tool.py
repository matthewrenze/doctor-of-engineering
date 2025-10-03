import os
import math
from markitdown import MarkItDown

chunk_size = 10000

class ReadFileTool:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def execute(self, file_name, chunk: int = 1) -> str:

        try:

            # Handle optional chunk parameter
            if chunk is None:
                chunk = 1

            # Check if file exists
            file_path = f"{self.folder_path}/{file_name}"
            if not os.path.exists(file_path):
                return f"File {file_name} does not exist."

            # Convert to markdown
            markitdown = MarkItDown(enable_plugins=True)
            result = markitdown.convert(file_path)
            text = result.markdown

            # Calculate total chunks
            total_chunks = math.ceil(len(text) / chunk_size)

            # Handle out of bounds
            if chunk < 1:
                return "Chunk index must be greater than 0."
            if chunk > total_chunks:
                return f"Chunk index {chunk} is out of range. Total chunks: {total_chunks}."

            # Get the chunk
            start = (chunk - 1) * chunk_size
            end = min(chunk * chunk_size, len(text))
            chunk_text = text[start:end]
            footer = f"\n[End of chunk {chunk} of {total_chunks}]"

            return chunk_text + footer

        except Exception as e:
            return str(e)

# # DEBUG:
# if __name__ == "__main__":
#     os.getcwd()
#     file_path = "data/evals/gaia/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
#     markitdown = MarkItDown()
#     text = markitdown.convert(file_path)
#     print(text)

