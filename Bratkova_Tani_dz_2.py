# ПОПРАВИЛА ОШИБКИ И ЕЩЕ РАЗ ОТПРАВИЛА НА GitHub

print('Задание 2: список, состоящий из кубов нечётных чисел от 1 до 1000')
list_numbers = []
# в строке ниже у меня раньше было написано 1000, забыла что range генерирует меньше на 1 - исправила
for number in range(1, 1001, 2):
    list_numbers.append(number ** 3)
print(list_numbers, '\n')

print('Задание 2a: вычислить сумму чисел из списка выше, сумма цифр которых делится нацело на 7')
sum_divided_by_seven = 0
for number in list_numbers:
    summa = 0
    num_from_list = number
    while num_from_list != 0:
        summa += num_from_list % 10
        num_from_list = num_from_list // 10
    if summa % 7 == 0:
        sum_divided_by_seven += number
print(sum_divided_by_seven, 'результат проверила в Excel\n') # получается 17485588610 результат проверила в Excel

print('Задание 2b: к каждому числу прибавить 17 и заново вычислить сумму чисел, сумма цифр которых делится нацело на 7')
sum_divided_by_seven = 0

# создадим новый список, прибавив число 17 к каждому элементу из старого списка
list_numbers_new = [number+17 for number in list_numbers]

for number in list_numbers_new:
    summa = 0
    num_from_list = number
    while num_from_list != 0:
        summa += num_from_list % 10
        num_from_list = num_from_list // 10
    if summa % 7 == 0:
        sum_divided_by_seven += number

print(list_numbers_new)
print(sum_divided_by_seven, 'результат проверила в Excel\n') # получается 15392909930 результат проверила в Excel

print('Задание 2c: решить задание 2b без создания нового списка (при помощи range() + for in)')
sum_divided_by_seven = 0
for number in range(len(list_numbers)):
    summa = 0
    list_numbers[number] += 17 # благодаря range() мы можем в цикле обращаться к элементам массива list_numbers[number]
    num_from_list = list_numbers[number]
    while num_from_list != 0:
        summa += num_from_list % 10
        num_from_list = num_from_list // 10
    if summa % 7 == 0:
        sum_divided_by_seven += list_numbers[number]
print(list_numbers)
print(sum_divided_by_seven, 'результат проверила в Excel, он такой же как и в задании 2b') # получается 15392909930 результат проверила в Excel
print('{:,}'.format(sum_divided_by_seven).replace(',', ' '), 'а эту примочку я подсмотрела в интернете, чтобы отделить разряды в числе')
