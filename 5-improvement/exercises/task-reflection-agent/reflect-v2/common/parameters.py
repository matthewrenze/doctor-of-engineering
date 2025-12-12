from dataclasses import dataclass

@dataclass
class Parameters:
    agent_name: str
    is_training: bool
    model_name: str
    env_name: str
    eval_name: str
    max_steps: int