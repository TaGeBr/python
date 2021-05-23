list_numbers = int(input('Введите количество чисел (по условию задачи количество 20, но работает для любого количества): '))
list_numbers = list(range(1, list_numbers+1))
print(list_numbers)

for number in list_numbers:
    num = list_numbers[number-1]
    if num in [11, 12, 13, 14]:
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    elif num % 10 in [2, 3, 4]:
        print(num, 'процента')
    else:
        print(num, 'процентов')
