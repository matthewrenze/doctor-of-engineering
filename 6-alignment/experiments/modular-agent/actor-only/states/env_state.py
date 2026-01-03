from dataclasses import dataclass

@dataclass
class EnvState:
    feedback: str = ""
    location: str = ""
    description: str = ""
    inventory: str = ""
    score: int = 0
    max_score: int = 0
    reward: float = 0.0
    max_reward: float = 1.0
    is_done: bool = False