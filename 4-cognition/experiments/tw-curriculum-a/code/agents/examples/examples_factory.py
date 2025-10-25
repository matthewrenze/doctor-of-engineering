class ExamplesFactory(object):
    def create(self, env_name: str, agent_version) -> str:
        # Select the examples file
        if env_name == "mcqa":
            file_name = f"mcqa-v{agent_version}.txt"
        elif env_name == "open-qa":
            file_name = f"open-qa-v{agent_version}.txt"
        elif env_name.startswith("textworld"):
            file_name = f"textworld-v{agent_version}.txt"
        else:
            raise ValueError(f"Unknown env name: {env_name}")

        # Read the examples from the file
        folder_path = "agents/examples"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as f:
            examples = f.read()

        return examples