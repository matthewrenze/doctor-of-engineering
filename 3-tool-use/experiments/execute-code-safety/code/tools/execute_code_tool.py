import os
import sys
import shutil
import subprocess
import tempfile
import textwrap
import ast

timeout = 10
v1_header = ""
v2_header = """
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

class ExecuteCodeTool:
    def __init__(self, workspace_path: str, version: int):
        self.workspace_path = workspace_path
        self.header = v1_header if version == 1 else v2_header

    def execute(self, code: str) -> str:

        # Wrap final expression in print()
        body = textwrap.dedent(code).rstrip()
        tree = ast.parse(body, mode="exec")
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            seg = ast.get_source_segment(body, tree.body[-1].value)
            if seg and not seg.strip().startswith("print("):
                body += f"\nprint({seg})"

        # Add safety header
        code = self.header + "\n" + body

        # Create a temp folder
        with tempfile.TemporaryDirectory() as temp_folder:
            file_path = os.path.join(temp_folder, "main.py")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(code)

            try:

                # Find the python executable
                python_exe = sys.executable \
                    or shutil.which("python") \
                    or shutil.which("python3") \
                    or "python"

                # Execute the code
                process = subprocess.run(
                    args=[python_exe, "-I", file_path],
                    cwd=self.workspace_path,
                    capture_output=True,
                    text=True,
                    timeout=timeout)

                # Handle errors
                if process.returncode != 0:
                    return f"Error: {process.stderr}"

                # Return stdout
                return process.stdout

            # Handle timeout
            except subprocess.TimeoutExpired:
                return f"Error: Timeout occurred. Code execution is limited to {timeout} seconds runtime."

if __name__ == "__main__":
    tool = ExecuteCodeTool("../data/workspaces/test")
    print("# Normal usage")
    print(tool.execute("result = 1 + 2\nprint(result)"))
    print(tool.execute("from math import sqrt\nresult = sqrt(2)\nprint(result)"))
    print(tool.execute("result = sum([1,2,3,4])\nprint(result)"))
    print(tool.execute("print(\"Hello World\")"))
    print(tool.execute("for i in range(5): print(i)"))

    print("# Normal errors")
    print(tool.execute("result = 1/0\nprint(result)"))
    print(tool.execute("import time\ntime.sleep(5)"))

    print("# Allowed imports")
    print(tool.execute("import json\nprint(json.dumps({'x': 1}))"))  # -> {"x": 1}
    print(tool.execute("from math import sqrt\nprint(sqrt(9))"))  # -> 3.0
    print(tool.execute("import datetime as dt\nprint(dt.date(2025,1,1))"))  # -> 2025-01-01
    print(tool.execute("import re\nprint(bool(re.match('a+', 'aaa')))"))  # -> True
    print("---\n")

    print("# Blocked imports")
    print(tool.execute("import os"))  # ImportError: disabled
    print(tool.execute("from subprocess import Popen"))  # ImportError: disabled
    print(tool.execute("__import__('socket')"))  # ImportError: disabled
    print(tool.execute("import shutil as s"))  # ImportError: disabled
    print(tool.execute("import os.path"))  # ImportError: disabled (ensure dotted names are caught)
    print(tool.execute("from os import path"))  # ImportError: disabled
    print("---\n")

    print("# Blocked file I/O")
    print(tool.execute("open('x.txt','w')"))  # PermissionError: open() disabled
    print(tool.execute("eval('2+2')"))  # PermissionError: eval() disabled
    print(tool.execute("exec('x=1')"))  # PermissionError: exec() disabled
    print("---\n")

    print("# Blocked indirect imports")
    print(tool.execute("import importlib\nimportlib.import_module('os')"))  # ImportError: disabled
    print(tool.execute("import urllib.request\nprint('ok')"))  # ImportError: socket disabled
    print(tool.execute("import builtins\nbuiltins.__import__('os')"))  # ImportError: disabled
    print("---\n")
