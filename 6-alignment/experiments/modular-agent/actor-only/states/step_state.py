from dataclasses import dataclass, field
from states.agent_state import AgentState
from states.env_state import EnvState

@dataclass
class StepState:
    step_id: int = 0
    env_state: EnvState = field(default_factory=EnvState)
    agent_state: AgentState = field(default_factory=AgentState)