class PromptFactory:
    def create(self, version: int) -> str:
        file_name = f"react-v{version}.txt"
        folder_path = "agents/prompts"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as file:
            prompt = file.read()

        return prompt