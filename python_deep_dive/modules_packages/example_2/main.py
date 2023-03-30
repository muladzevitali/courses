import os.path
import types
import sys

module_name = 'module_1'
module_file = 'module_1_source.py'
module_path = '.'


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

import module_1

module_1.hello()