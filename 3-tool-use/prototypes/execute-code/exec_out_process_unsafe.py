import subprocess
import tempfile
import os
import textwrap

def execute(code: str, timeout: float = 3.0):
    code = textwrap.dedent(code)
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
                timeout=timeout
            )
            if process.returncode != 0:
                return f"Error: {process.stderr.strip()}"

            return process.stdout.strip()

        except subprocess.TimeoutExpired:
            return "Error: Timeout"

if __name__ == "__main__":
    print(execute("result = 1 + 2\nprint(result)"))
    print(execute("from math import sqrt\nresult = sqrt(2)\nprint(result)"))
    print(execute("result = sum([1,2,3,4])\nprint(result)"))
    print(execute("print(\"Hello World\")"))
    print(execute("result = 1/0\nprint(result)"))
    print(execute("for i in range(5): print(i)"))
    print(execute("import time\ntime.sleep(5)"))
