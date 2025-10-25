import math
import builtins

class CalculateTool:
    def __init__(self):
        safe_builtins = dict(vars(builtins))
        blacklist = ["open", "__import__", "exec", "eval", "compile", "input", "help", "exit", "quit"]
        for b in blacklist:
            safe_builtins.pop(b, None)
        self.globals = {
            "__builtins__": safe_builtins,
            "math": math,
            **math.__dict__}

    def execute(self, expression: str) -> str:
        try:
            result = eval(expression, self.globals, {})
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"


# DEBUG:
if __name__ == "__main__":
    tool = CalculateTool()
    assert tool.execute("2 + 3 * 4 - 5") == "9"
    assert tool.execute("(7 - (2 + 3)) * (4 - 1)") == "6"
    assert tool.execute("round(10/3, 6)") == "3.333333"
    assert tool.execute("2**52") == "4503599627370496"
    assert tool.execute("sqrt(75260986245481)") == "8675309.0"

