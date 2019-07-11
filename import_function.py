import glob
import importlib
import sys
import os
from collections import deque
MODULE_PATH = deque(glob.glob('/home/kuchi-chan/development/Python_Projects/pytest_sandbox/tests/data/mypkg/*_pb2.py'),4)


def get_imports(path: deque):
    while path:
        elem = path.pop()
        print(os.path.basename(elem).rstrip('.py'))
        print(elem)
        spec = importlib.util.spec_from_file_location(os.path.basename(elem).rstrip('.py'), elem)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        try:
            spec.loader.exec_module(module)
        except (ModuleNotFoundError, AttributeError):
            path.appendleft(elem)
        else:
            print(module)
            yield module


if __name__ == "__main__":
    a = get_imports(MODULE_PATH)
    for i in range(4):
        print('hello')
        next(a)


