from dataclasses import dataclass

@dataclass
class AgentState:
    thought: str = ""
    action: str = ""