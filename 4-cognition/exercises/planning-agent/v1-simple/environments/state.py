from dataclasses import dataclass

@dataclass
class State:
    task: str
    feedback: str
    location: str
    description: str
    inventory: str
    score: str