import ast
from typing import List, Tuple, Any

class ActionParser:
    def parse(self, action: str) -> Tuple[str, List[str]]:

        try:

            # Get the root node
            node = ast.parse(action.strip(), mode="eval")

            # Handle non-functions
            if not isinstance(node.body, ast.Call):
                raise ValueError("Action must be a function call.")

            # Get the function name
            func_node = node.body.func
            func_name = func_node.id

            # Get the arguments
            args: List[Any] = []
            for a in node.body.args:
                args.append(ast.literal_eval(a))

            return func_name, args

        except Exception as e:
            raise ValueError(f"Invalid action format.") from e


if __name__ == "__main__":
    p = ActionParser()
    samples = [
        # Normal cases
        "calculate(\"2+2\")",
        "search_web(\"query\")",
        "read_html(\"http://example.com\", 2)",
        "execute_code(\"print('hello world')\")",
        "finish(\"Las Vegas, NV\")",

        # Edge cases
        "execute_code(\"print('a')\\nprint('b')\")",
        "execute_code(\"\"\"print('a')\nprint('b')\"\"\")",
    ]
    for source in samples:
        target = p.parse(source)
        print(f"{source} -> {target}")