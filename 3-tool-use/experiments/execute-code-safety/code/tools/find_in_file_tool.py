import os
from markitdown import MarkItDown

window_size = 1000

class FindInFileTool:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def execute(self, file_name: str, text: str, match: int):
        try:

            # Handle missing text
            if not text:
                return "Text must be non-empty."

            # Handle optional match
            if match is None:
                match = 1

            # Handle out-of-bounds match
            if match < 1:
                return "Match index must be a 1-based integer."

            file_path = f"{self.folder_path}/{file_name}"
            if not os.path.exists(file_path):
                return f"File {file_name} does not exist."

            # Convert to markdown
            markitdown = MarkItDown(enable_plugins=True)
            result = markitdown.convert(file_path)
            markdown = result.markdown

            # Convert to lower case
            text_lower = text.lower()
            markdown_lower = markdown.lower()

            # Find all matches
            matches = []
            pos = -1
            while True:
                pos = markdown_lower.find(text_lower, pos + 1)
                if pos == -1:
                    break
                matches.append(pos)

            # Handle no matches
            total_matches = len(matches)
            if total_matches == 0:
                return f"No matches found for '{text}'."

            # Handle out-of-bounds match
            if match > total_matches:
                return f"Match index {match} is out of range. Total matches: {total_matches}."

            # Get the match snippet
            idx = matches[match - 1]
            half = window_size // 2
            start = max(0, idx - half)
            end = min(len(markdown), start + window_size)
            snippet = markdown[start:end]
            footer = f"\n[Match {match} of {total_matches} at location {idx:,}]"
            return snippet + footer

        except Exception as e:
            return f"Error: {str(e)}"