import os

class ListFilesTool:
    def __init__(self, folder_path):
        self.directory = folder_path

    def execute(self):
        try:

            # Get the files
            file_names = os.listdir(self.directory)
            num_files = len(file_names)

            # Create the output
            output = f"Workspace contains {num_files} file(s):\n"
            output += "\n".join(file_names)

            return output

        except Exception as e:
            return str(e)

# # DEBUG:
# tool = ListFilesTool("../data/workspaces/baseline - gpt-4.1-mini - gaia-test-10 - 0")
# result = tool.execute()
# print(result)