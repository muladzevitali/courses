import sys
import importer


module_1 = importer.import_('module_1', 'module_1_source.py', '.')

print(sys.modules.get('module_1', 'not found'))

import module_2
module_2.hello()