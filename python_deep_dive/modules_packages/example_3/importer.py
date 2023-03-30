import os.path
import sys
import types

print("running import.py")

def import_(module_name, module_file, module_path):
    if module_name in sys.modules:
        return sys.modules[module_name]

    module_rel_path = os.path.join(module_path, module_file)
    absolute_file_path = os.path.abspath(module_rel_path)

    # read source code from file
    with open(module_rel_path, 'r') as f:
        source = f.read()

    # create module object
    module = types.ModuleType(module_name)
    module.__file__ = absolute_file_path

    sys.modules[module_name] = module

    # compile source code
    code = compile(source, filename=absolute_file_path, mode='exec')

    # execute compiled source code
    exec(code, module.__dict__)

    return sys.modules[module_name]
