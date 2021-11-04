from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    """
    There should be a doc string here
    """
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
