import os
import subprocess
import tempfile
import textwrap
import ast

header = """
import builtins
def _blocked_import(name, *a, **k):
    if name in {"os", "subprocess", "sys", "socket", "shutil"}:
        raise ImportError(f"Import of {name} is disabled")
    return orig_import(name, *a, **k)
orig_import = builtins.__import__
builtins.__import__ = _blocked_import
open = lambda *a, **k: (_ for _ in ()).throw(PermissionError("open() disabled"))
exec = lambda *a, **k: (_ for _ in ()).throw(PermissionError("exec() disabled"))
eval = lambda *a, **k: (_ for _ in ()).throw(PermissionError("eval() disabled"))
"""

def execute(code: str, timeout: float = 3.0):

    # Wrap final expression in print()
    body = textwrap.dedent(code).rstrip()
    tree = ast.parse(body, mode="exec")
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        seg = ast.get_source_segment(body, tree.body[-1].value)
        if seg and not seg.strip().startswith("print("):
            body += f"\nprint({seg})"

    # Add safety header
    code = header + "\n" + body

    with tempfile.TemporaryDirectory() as temp_folder:
        file_path = os.path.join(temp_folder, "main.py")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(code)

        try:
            process = subprocess.run(
                args=["python", "-I", file_path],
                cwd=temp_folder,
                capture_output=True,
                text=True,
                timeout=timeout)

            # Handle errors
            if process.returncode != 0:
                return process.stderr

            # Return stdout
            return process.stdout

        # Handle timeout
        except subprocess.TimeoutExpired:
            return "Error: Timeout"

if __name__ == "__main__":
    print("# Normal usage")
    print(execute("1 + 2"))
    print(execute("from math import sqrt\nsqrt(2)"))
    print(execute("sum([1,2,3,4])"))
    print(execute("print(\"Hello World\")"))
    print(execute("for i in range(5): i"))