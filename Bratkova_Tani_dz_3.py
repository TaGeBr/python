user_numbers = int(input('Введите число (работает для любого числа): '))
num = user_numbers
if num in [11, 12, 13, 14]:
    print(num, 'процентов\n')
elif num % 10 == 1:
    print(num, 'процент\n')
elif num % 10 in [2, 3, 4]:
    print(num, 'процента\n')
else:
    print(num, 'процентов\n')

print('Список склонений для чисел от 1 до 20:')
for number in range(1, 21):
    num = number
    if num in [11, 12, 13, 14]:
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    elif num % 10 in [2, 3, 4]:
        print(num, 'процента')
    else:
        print(num, 'процентов')
