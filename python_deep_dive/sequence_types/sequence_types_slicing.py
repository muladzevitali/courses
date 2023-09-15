import functools

s = slice(None, 20, 3)

my_list = [1, 2, 3, 4]
my_list.__getitem__(2)


class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print("called __len__")
        return self.n

    def __getitem__(self, item):
        if item < 0 or item >= self.n + 10:
            raise IndexError

        if isinstance(item, int):
            return f'value({item})'


for i in Silly(19):
    print(i)


class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < 0:
                item = max(0, self.n + item)

            if item >= self.n:
                raise IndexError

            return Fib._fib(item)

        if isinstance(item, slice):
            start, stop, step = item.indices(self.n)
            rng = range(start, stop, step)

            return [Fib._fib(index) for index in rng]

        raise TypeError

    @staticmethod
    @functools.lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1

        return Fib._fib(n - 1) + Fib._fib(n - 2)


fib = Fib(100)

a = list(fib)

print(fib[1])
print(fib[0: 30])
