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

if __name__ == "__main__":
    result_1 = 1 + 2
    print(result_1)

    from math import sqrt
    result_2 = sqrt(2)
    print(result_2)

    result_3 = sum([1,2,3,4])
    print(result_3)

    print("Hello World")

    result_5 = 1/0

    for i in range(5): print(i)

    import time
    time.sleep(5)