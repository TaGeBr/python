# https://proglib.io/p/vse-chto-nuzhno-znat-o-dekoratorah-python-2020-05-09
# https://pythonworld.ru/osnovy/dekoratory.html
# https://tproger.ru/translations/demystifying-decorators-in-python/

from functools import wraps


def val_checker(val_check):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args): # wrapper в переводе с английского обёртка
            # print(val_check(*args)) # УРА ЗАРАБОТАЛО!!!!!!!!! тут наш отрицательный или
            # положительный икс залетает в лямбда функцию и выдает False или True
            if not val_check(*args):
                raise ValueError(f'wrong val {str(*args)}')
            result = func(*args)
            return result
        return wrapper
    return actual_decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Описание функции calc_cube()"""
    print(f'{calc_cube.__name__}({x}: {type(x)})')
    return x ** 3


print()
print(calc_cube(5))

print('\nтут работает маскировка декоратора, если декоратор включен:')
print(calc_cube.__name__)
print(calc_cube.__doc__)
