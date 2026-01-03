from dataclasses import dataclass, field
from states.step_state import StepState

@dataclass
class GlobalState:
    task: str = ""
    current_step_id: int = 0
    step_history: list[StepState] = field(default_factory=list)