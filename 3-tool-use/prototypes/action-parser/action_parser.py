import ast
from typing import List, Tuple

class ActionParser:
    def parse(self, action: str) -> Tuple[str, List[str]]:

        try:
            action = action.strip()
            node = ast.parse(action, mode="eval")
            name = node.body.func.id
            args = [ast.unparse(a) for a in node.body.args]
            args = [a.strip("\"'") for a in args]
            return name, args

        except Exception as e:
            raise ValueError(f"Invalid action format") from e


if __name__ == "__main__":
    p = ActionParser()
    samples = [
        "calculate(\"2+2\")",
        "search_web(\"query\")",
        "read_html(\"http://example.com\", 2)",
        "finish(\"Las Vegas, NV\")",
    ]
    for source in samples:
        target = p.parse(source)
        print(f"{source} -> {target}")
