# https://proglib.io/p/vse-chto-nuzhno-znat-o-dekoratorah-python-2020-05-09
# https://pythonworld.ru/osnovy/dekoratory.html
# https://tproger.ru/translations/demystifying-decorators-in-python/

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args): # wrapper в переводе с английского обёртка
        print('здесь мы летим луну - это действие принадлежит обертке')
        print('сейчас функция сработает из обертки!!!')
        result = func(*args)
        print('а здесь возвращаемся с луны - и это действие тоже принадлежит обертке')
        return result # здесь возвращается возведение в степень, если не сделать тут return, то вернется None
    return wrapper # а здесь отваливаются космические ступени


@type_logger # тут можно вкл/выкл декоратор поставив #
def calc_cube(x):
    """Описание функции calc_cube()"""
    print(f'{calc_cube.__name__}({x}: {type(x)}) в этом месте работает функция')
    return x ** 3


calc_cube(5)
print('и здесь мы не видим самого возведения в 3-ю степень, т.к. функция отработала, '
      'вернула результат, но мы никуда не положили этот результат')

print()
print(calc_cube(5), 'это вернул return функции calc_cube(5) - тут мы положили результат в print')

print()
result = calc_cube(3.14)
print(result, 'это вернул return функции calc_cube(3.14) - тут мы положили результат в переменную')

print('\nтут работает маскировка декоратора, если декоратор включен:')
print(calc_cube.__name__)
print(calc_cube.__doc__)

# Ниже код, который я взяла из интернета, запустила посмотрела на результат работы и сразу поняла как
# работают декораторы. Потому что очень удачный пример. И сразу же выполнила ДЗ. Через час после окончания
# вебинара это задание было сделано. Потом я конечно еще подчистила помарочки после 4-ой задачи.

# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#         return return_value
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
#
# webpage = fetch_webpage('https://google.com')
# print(webpage)

