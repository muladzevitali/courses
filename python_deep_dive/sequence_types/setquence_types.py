import sys
from dis import dis
from timeit import timeit

dis(compile('(1,2,3, "a")', "string", "eval"))

dis(compile('[1,2,3, "a"]', "string", "eval"))

dis(compile('(1,2,3, "a", [1, 2, 3, "a"])', "string", "eval"))

timeit('(1,2,3, "a")', number=10_000_000)
timeit('[1,2,3, "a"]', number=10_000_000)


def fn1():
    pass


dis(compile('(fn1, 10, 20)', "string", "eval"))

timeit('([1,2,3, "a"], 1, 2)', number=10_000_000)
timeit('[[1,2,3, "a"], 1, 2]', number=10_000_000)

timeit('list((1,2,3,4))', number=10_000_000)

# Storage efficiency
t = tuple()
prev = sys.getsizeof(t)
for i in range(10):
    c = tuple(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f"{i + 1} items: {size_c}, delta:{delta}")

t = list()
prev = sys.getsizeof(t)
for i in range(10):
    c = list(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f"{i + 1} items: {size_c}, delta:{delta}")

l = list()
prev = sys.getsizeof(l)
print(f'0 items: {prev}')
for i in range(255):
    l.append(i)
    size_c = sys.getsizeof(l)
    delta, prev = size_c - prev, size_c
    print(f"{i + 1} items: {size_c}, delta:{delta}")

t = tuple(range(100_000))
l = list(range(100_000))

timeit('t[-1]', number=10_000_000, globals=globals())
timeit('l[-1]', number=10_000_000, globals=globals())

a = [1, 2]
b = [a, 30]
a.append(b)

from copy import deepcopy