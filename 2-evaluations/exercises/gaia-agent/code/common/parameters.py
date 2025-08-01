from dataclasses import dataclass

@dataclass
class Parameters:
    agent_name: str
    model_name: str
    eval_name: str
    max_steps: int