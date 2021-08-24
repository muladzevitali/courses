def custom_function(a, b):
    """Some docstring"""
    return 2 *2

def func(a=3, *, b=2, **kwargs):
    return a, b, kwargs

def clip(a: str, b: 'int > 0'):
    pass


print(clip.__annotations__)
clip('valeri', -34)

