class PromptFactory:
    def create(self, agent_name: str) -> str:
        if agent_name == "baseline":
            file_name = "baseline.txt"
        elif agent_name == "react":
            file_name = "react.txt"
        else:
            raise ValueError(f"Unknown agent type: {agent_name}")


        folder_path = "agents/prompts"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as file:
            prompt = file.read()

        return prompt