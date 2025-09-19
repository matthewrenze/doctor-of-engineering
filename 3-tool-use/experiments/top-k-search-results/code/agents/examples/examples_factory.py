class ExamplesFactory(object):
    def create(self, agent_name: str, env_name: str) -> str:
        # Select the examples file
        if agent_name == "baseline":
            if env_name == "mcqa":
                file_name = "baseline-mcqa.txt"
            elif env_name == "open-qa":
                file_name = "baseline-open-qa.txt"
            else:
                raise ValueError(f"Unknown env name: {env_name}")

        elif agent_name.startswith("react"):
            if env_name == "mcqa":
                file_name = "react-mcqa.txt"
            elif env_name == "open-qa":
                file_name = "react-open-qa.txt"
            else:
                raise ValueError(f"Unknown env name: {env_name}")

        else:
            raise ValueError(f"Unknown agent name: {agent_name}")

        # Read the examples from the file
        folder_path = "agents/examples"
        file_path = f"{folder_path}/{file_name}"
        with open(file_path, "r") as f:
            examples = f.read()

        return examples