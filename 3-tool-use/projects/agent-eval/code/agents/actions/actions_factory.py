class ActionsFactory:
    def create(self, env_name: str) -> str:

        # Select the action file
        if env_name == "mcqa":
            file_name = "qa.txt"
        elif env_name == "open-qa":
            file_name = "qa.txt"
        elif env_name == "textworld":
            file_name = "textworld.txt"
        else:
            raise ValueError(f"Unknown action type: {env_name}")

        # Read the actions from the file
        folder_path = "agents/actions"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as f:
            actions = f.read()

        return actions