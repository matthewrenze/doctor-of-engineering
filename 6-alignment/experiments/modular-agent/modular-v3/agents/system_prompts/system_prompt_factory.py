class SystemPromptFactory:
    def create(self, subagent: str) -> str:

        # Get the system prompt
        agent_folder_path = f"agents/{subagent}"
        system_prompt_file_name = f"{subagent}-system-prompt.md"
        system_prompt_file_path = f"{agent_folder_path}/{system_prompt_file_name}"
        with open(system_prompt_file_path, "r") as file:
            system_prompt = file.read()

        # Add the actions
        actions_file_path = f"agents/system_prompts/actions.md"
        with open(actions_file_path, "r") as file:
            actions_content = file.read()
        system_prompt = system_prompt.replace("{actions}", actions_content)

        # Add the examples
        examples_file_path = f"agents/system_prompts/examples.md"
        with open(examples_file_path, "r") as file:
            examples_content = file.read()
        system_prompt = system_prompt.replace("{examples}", examples_content)

        return system_prompt