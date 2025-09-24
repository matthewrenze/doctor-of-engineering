import os
from common.parameters import Parameters

# Define the ANSI colors
BOLD_WHITE = "\033[97m"
WHITE = "\033[38;5;250m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
RED = "\033[91m"
RESET = "\033[0m"

class Log:
    def __init__(self, params: Parameters, episode_id):
        folder_path = f"../data/logs/{params.agent_name} - {params.model_name} - {params.eval_name}"
        os.makedirs(folder_path, exist_ok=True)
        file_path = f"{folder_path}/{episode_id}.txt"
        self.file = open(file_path, "w", encoding="utf-8", newline="\n")

    def print(self, text):
        print(f"{WHITE}{text}{RESET}")

    def head(self, text):
        self.file.write(f"{text}\n")
        print(f"{BOLD_WHITE}{text}{RESET}")

    def info(self, text):
        self.file.write(f"{text}\n")
        print(f"{WHITE}{text}{RESET}")

    def debug(self, text):
        self.file.write(f"Debug: {text}\n")
        print(f"{YELLOW}Debug: {text}{RESET}")

    def warning(self, warning):
        self.file.write(f"Warning: {warning}\n")
        print(f"{ORANGE}Warning: {warning}{RESET}")

    def error(self, error):
        self.file.write(f"Error: {error}\n")
        print(f"{RED}Error: {error}{RESET}")

    def close(self):
        self.file.flush()
        self.file.close()

# Test the log
if __name__ == "__main__":

    params = Parameters(
        agent_name="test_agent",
        model_name="test_model",
        env_name="test_env",
        eval_name="test_eval",
        max_steps=10
    )

    log = Log(params, 0)
    log.head("Here is a heading")
    log.print("Here is printed text")
    log.info("Here is logged text")
    log.debug("Here is debug text")
    log.warning("Here is a warning message")
    log.error("Here is a error message")
    log.close()