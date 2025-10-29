class ExamplesFactory(object):
    def create(self, env_name: str, agent_version) -> str:
        # Select the examples file
        if env_name.startswith("textworld"):
            if agent_version == 0:
                file_name = "textworld-v0.txt"
            else:
                file_name = "textworld-vn.txt"
        else:
            raise ValueError(f"Unknown env name: {env_name}")

        # Read the examples from the file
        folder_path = "agents/examples"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as f:
            examples = f.read()

        return examples