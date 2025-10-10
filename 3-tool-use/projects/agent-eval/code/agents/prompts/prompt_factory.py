class PromptFactory:
    def create(self) -> str:
        file_name = "react.txt"
        folder_path = "agents/prompts"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as file:
            prompt = file.read()

        return prompt