import io
import contextlib

def execute(code: str):
    globals = {"__builtins__": __builtins__}
    locals = {}
    out = io.StringIO()
    err = io.StringIO()
    try:
        with contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(err):
            exec(code, globals, locals)

        # Return result
        if "result" in locals:
            return str(locals["result"])

        # Return errors
        errors = err.getvalue()
        if errors:
            return errors

        # Return stdout
        return out.getvalue()
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(execute("result = 1 + 2"))
    print(execute("from math import sqrt\nresult = sqrt(2)"))
    print(execute("result = result = sum([1,2,3,4])"))
    print(execute("print(\"Hello World\")"))
    print(execute("result = 1/0"))
    print(execute("for i in range(5): print(i)"))
