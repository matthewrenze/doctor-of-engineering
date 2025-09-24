import ast, math

_ALLOWED = {k: getattr(math, k) for k in ["sqrt", "sin", "cos", "log", "exp", "pi", "e"]}

def execute(expr: str):
    try:
        node = ast.parse(expr, mode="eval")
        if not isinstance(node.body, (ast.Constant, ast.Tuple, ast.List, ast.Dict, ast.Set, ast.BinOp, ast.UnaryOp, ast.Compare, ast.Call, ast.Attribute, ast.Name)):
            raise ValueError("Unsupported expression")
        return eval(compile(node, "<expr>", "eval"), {"__builtins__": {}}, _ALLOWED)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    result_1 = execute("1+2")
    print(result_1)

    result_2 = execute("sqrt(2)")
    print(result_2)

    result_3 = execute("sin(1)")
    print(result_3)

    result_4 = execute("print(\"Hello World\")")
    print(result_4)