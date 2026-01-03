from typing import Protocol, runtime_checkable, Any

@runtime_checkable
class Model(Protocol):

    model_name: str
    input_tokens: int
    output_tokens: int
    total_tokens: int

    def reset(self) -> None: ...

    def get_response(self, messages: list[dict[str, str]]) -> str: ...
