import os

class ListFilesTool:
    def __init__(self, folder_path):
        self.directory = folder_path

    def execute(self) -> dict:
        try:

            # Get the files
            file_names = os.listdir(self.directory)
            num_files = len(file_names)

            result = { "num_files": num_files, "file_names": file_names}

            return result

        except Exception as e:
            return { "error": str(e) }

# # DEBUG:
# tool = ListFilesTool("../data/workspaces/baseline - gpt-4.1-mini - gaia-test-10 - 0")
# result = tool.execute()
# print(result)