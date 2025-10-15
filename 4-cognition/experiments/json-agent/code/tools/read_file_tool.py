import os
import math
from markitdown import MarkItDown

chunk_size = 10000

class ReadFileTool:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def execute(self, file_name: str, chunk_index: int = 1) -> dict:

        try:

            # Handle optional chunk parameter
            if chunk_index is None:
                chunk_index = 1

            # Check if file exists
            file_path = f"{self.folder_path}/{file_name}"
            if not os.path.exists(file_path):
                return { "error": f"File {file_name} does not exist." }

            # Convert to markdown
            markitdown = MarkItDown(enable_plugins=True)
            result = markitdown.convert(file_path)
            text = result.markdown

            # Calculate total chunks
            total_chunks = math.ceil(len(text) / chunk_size)

            # Handle out of bounds
            if chunk_index < 1:
                return { "error": "Chunk index must be greater than 0." }

            if chunk_index > total_chunks:
                return { "error": f"Chunk index {chunk_index} is out of range. Total chunks: {total_chunks}." }

            # Get the chunk
            start = (chunk_index - 1) * chunk_size
            end = min(chunk_index * chunk_size, len(text))
            chunk_text = text[start:end]

            result = {
                "chunk_text": chunk_text,
                "chunk_index": chunk_index,
                "total_chunks": total_chunks,
            }

            return result

        except Exception as e:
            return { "error": str(e) }

# # DEBUG:
# if __name__ == "__main__":
#     os.getcwd()
#     file_path = "data/evals/gaia/3da89939-209c-4086-8520-7eb734e6b4ef.xlsx"
#     markitdown = MarkItDown()
#     text = markitdown.convert(file_path)
#     print(text)

