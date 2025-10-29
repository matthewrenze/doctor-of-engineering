class PromptFactory:
    def create(self, version: int) -> str:
        if version == 0:
            file_name = "react-v0.txt"
        else:
            file_name = "react-vn.txt"
        folder_path = "agents/prompts"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as file:
            prompt = file.read()

        return prompt