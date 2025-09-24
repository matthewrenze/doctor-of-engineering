import os
import subprocess
import tempfile
import textwrap

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
    code = header + "\n" + textwrap.dedent(code)
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
    print(execute("result = 1 + 2\nprint(result)"))
    print(execute("from math import sqrt\nresult = sqrt(2)\nprint(result)"))
    print(execute("result = sum([1,2,3,4])\nprint(result)"))
    print(execute("print(\"Hello World\")"))
    print(execute("for i in range(5): print(i)"))

    print("# Normal errors")
    print(execute("result = 1/0\nprint(result)"))
    print(execute("import time\ntime.sleep(5)"))

    print("# Allowed imports")
    print(execute("import json\nprint(json.dumps({'x': 1}))"))  # -> {"x": 1}
    print(execute("from math import sqrt\nprint(sqrt(9))"))  # -> 3.0
    print(execute("import datetime as dt\nprint(dt.date(2025,1,1))"))  # -> 2025-01-01
    print(execute("import re\nprint(bool(re.match('a+', 'aaa')))"))  # -> True
    print("---\n")

    print("# Blocked imports")
    print(execute("import os"))  # ImportError: disabled
    print(execute("from subprocess import Popen"))  # ImportError: disabled
    print(execute("__import__('socket')"))  # ImportError: disabled
    print(execute("import shutil as s"))  # ImportError: disabled
    print(execute("import os.path"))  # ImportError: disabled (ensure dotted names are caught)
    print(execute("from os import path"))  # ImportError: disabled
    print("---\n")

    print("# Blocked file I/O")
    print(execute("open('x.txt','w')"))  # PermissionError: open() disabled
    print(execute("eval('2+2')"))  # PermissionError: eval() disabled
    print(execute("exec('x=1')"))  # PermissionError: exec() disabled
    print("---\n")

    print("# Blocked indirect imports")
    print(execute("import importlib\nimportlib.import_module('os')"))  # ImportError: disabled
    print(execute("import urllib.request\nprint('ok')"))  # ImportError: socket disabled
    print(execute("import builtins\nbuiltins.__import__('os')"))  # ImportError: disabled
    print("---\n")




