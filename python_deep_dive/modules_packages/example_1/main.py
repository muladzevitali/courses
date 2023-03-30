import sys
print(f"-------running main.py: {__name__}")

import module_1

print('importing module 1 again')

import module_1

print(module_1)
del globals()['module_1']
import module_1

module_1.pprint('main.globals', globals())

print(sys.path)
print(sys.modules['module_1'])
print(f"-------end of {__name__}-------")

