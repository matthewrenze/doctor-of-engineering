class ReflectPromptFactory:
    def create(self) -> str:
        folder_path = "agents/prompts"
        file_name = "reflect-prompt.md"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as file:
            prompt = file.read()

        return prompt