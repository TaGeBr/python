with open('nginx_logs.txt', 'r') as f:
    list_out = []
    spam_names = {}
    for line in f:
        result = line.split()
        list_out.append((result[0], result[5].replace('"',''), result[6]))
        spam_names.setdefault(result[0], 0)

        # ниже я разбирала как работает добавление по ключу
        # x = {'one': 0, 'two': 2, 'three': 3, 'four': 4}
        # x.setdefault('ten', 10)
        # print(x) # {'one': 0, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
        # x['two'] += 5
        # print(x) # {'one': 0, 'two': 7, 'three': 3, 'four': 4, 'ten': 10}
        spam_names[result[0]] += 1

print(type(spam_names))
# я очень честно разобрала на примере ниже сотртировку по значению через лямбду, просто в голове уже каша
# d1 = {'banana': 5, 'pears': 3, 'w_apple': 10}
# list_fruits = sorted(d1.items(), key=lambda x: x[1], reverse=True)
# print(list_fruits)
spam_names = sorted(spam_names.items(), key=lambda x: x[1], reverse=True)
print(type(spam_names)) # после sorted словарь превращается в список
print(*spam_names[:5], sep='\n')

# # ЭТО ИЗ КОНСПЕКТА ПОДГОТОВИТЕЛЬНОГО КУРСА
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number): #если function истина, то мы будем добавлять число в result
#             result.append(number)
#     return result
#
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
#
# def is_even(num):
#     return num % 2 == 0 #значит число чётное
#
# print(my_filter(numbers, is_even))
#
# def is_not_even(num):
#     return num % 2 != 0 #значит число нечётное
#
# print(my_filter(numbers, is_not_even))
#
#
# print(my_filter(numbers, lambda num: num % 3 == 0 )) #пример лямбда функции - вернутся все числа, которые делятся на три


# # НИЖЕ ПРИМЕРЫ ИЗ ИНТЕРНЕТА:
# modify_list — это функция, которая принимает список L и функцию fn в качестве аргументов.
# Затем она перебирает список элемент за элементом и применяет функцию к каждому из них.
# def f(x):
#     return x * x + x
#
# def modify_list(L, fn):
#     for idx, v in enumerate(L):
#         L[idx] = fn(v)
#
# L = [1, 3, 2, 12, 6, 7]
# modify_list(L, f)
# print(L) # [1, 9, 4, 144, 36, 49]

# # Определить лямбда-функцию с одним аргументом не составляет труда.
# f = lambda x: x * x
# print(f(5)) # 25
#
# # А если их должно быть несколько, то достаточно лишь разделить значения запятыми.
# # Предположим, что нужна функция, которая берет два числовых аргумента и возвращает их произведение.
# f = lambda x, y: x * y
# print(f(5, 2)) # 10
#
# # map() — это встроенная функция Python, принимающая в качестве аргумента функцию
# # и последовательность. Она работает так, что применяет переданную функцию к каждому элементу.
# # Предположим, есть список целых чисел, которые нужно возвести в квадрат с помощью map.
#
# L = [1, 2, 3, 4, 10, 11]
# print(list(map(lambda x: x**2, L))) # [1, 4, 9, 16]

# # Сортировка словаря на основе функции len
# l1 = {'carrot': 'vegetable', 'red': 'color', 'apple': 'fruitttttttt'}
# # Возвращает список ключей, отсортированных по функции len
# print(sorted(l1, key=len))
# # Вывод: ['red', 'apple', 'carrot']
#
# # Возвращает список значений, отсортированных на основе функции len
# print(sorted(l1.values(), key=len))
# # Вывод: ['color', 'vegetable', 'fruitttttttt']
#
# # Сортировка списка на основе функции len
# l1 = ['blue', 'green', 'red', 'orange']
# print(sorted(l1, key=len))
# # Вывод: ['red', 'blue', 'green', 'orange']
#
# d1 = {'apple': 1, 'Banana': 2, 'Pears': 3}
# # Возвращает список ключей, отсортированный по значениям
# print(sorted(d1))
# # Вывод: ['Banana', 'Pears', 'apple']
#
# # Возвращает список ключей, отсортированный после применения str.lower ко всем элементам
# print(sorted(d1, key=str.lower))
# # Вывод: ['apple', 'Banana', 'Pears']

# d1 = {'banana': 5, 'pears': 3, 'w_apple': 10}
# list_fruits = sorted(d1.items(), key=lambda x: x[1], reverse=True)
# print(list_fruits)
