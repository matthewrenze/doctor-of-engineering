from dataclasses import dataclass

@dataclass
class Parameters:
    agent_name: str
    agent_version: int
    model_name: str
    env_name: str
    eval_name: str
    max_steps: int