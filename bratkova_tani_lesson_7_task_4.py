"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os

print('хотела уже сдать "костыль" в виде if... elif, написала его и тут родилось '
      'решение, проверила на маленьких и больших папках - это работает!')

folder = input('Скопируйте сюда путь к любой папке: ')

size_statistics = {} # в байтах
# в список ниже можно положить любые значения, т.е. любые желаемые границы
borders = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8, 10 ** 9, 10 ** 10, 10 ** 11, 10 ** 12]

for dirpath, dirnames, filenames in os.walk(folder):
    for idx_num, filename in enumerate(filenames):
        size_next_file = int(os.path.getsize(os.path.join(dirpath, filename)))
        upper_border = size_next_file
        size_list = [num for i, num in enumerate(borders) if upper_border < borders[i]]
        # print(size_next_file, size_list)
        size_statistics.setdefault(size_list[0], 0)
        size_statistics[size_list[0]] += 1

print(dict(sorted(size_statistics.items())))





