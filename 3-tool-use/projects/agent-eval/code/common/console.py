YELLOW = "\033[38;5;226m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

def debug(message: str):
    print(f"{YELLOW}Debug: {message}{RESET}")

def warn(message: str):
    print(f"{ORANGE}Warning: {message}{RESET}")
