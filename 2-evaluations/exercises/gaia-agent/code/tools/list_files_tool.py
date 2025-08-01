import os

class ListFilesTool:
    def __init__(self, folder_path):
        self.directory = folder_path

    def execute(self):
        try:
            filenames = os.listdir(self.directory)
            filenames_text = "\n".join(filenames)
            return filenames_text
        except Exception as e:
            return str(e)

# # DEBUG:
# tool = ListFilesTool("../data/workspaces/baseline - gpt-4.1-mini - gaia-test-10 - 0")
# result = tool.execute()
# print(result)