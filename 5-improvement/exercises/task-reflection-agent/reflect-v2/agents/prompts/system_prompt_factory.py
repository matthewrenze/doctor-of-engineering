class SystemPromptFactory:
    def create(self, is_training: bool) -> str:
        folder_path = "agents/prompts"
        file_name = "system-prompt-train.md" if is_training else "system-prompt-test.md"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as file:
            prompt = file.read()

        return prompt