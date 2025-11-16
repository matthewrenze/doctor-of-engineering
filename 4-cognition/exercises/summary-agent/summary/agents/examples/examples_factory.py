class ExamplesFactory(object):
    def create(self, env_name: str) -> str:
        # Select the examples file
        if env_name.startswith("textworld"):
            file_name = "textworld.md"
        else:
            raise ValueError(f"Unknown env name: {env_name}")

        # Read the examples from the file
        folder_path = "agents/examples"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as f:
            examples = f.read()

        return examples