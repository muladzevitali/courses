from array import array
from random import random

c = array('d', (random() for i in range(10 ** 7)))
c.typecode