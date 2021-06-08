src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Вывести из списка {src} числа, которые больше, чем предыдущее (сосед слева)')

# a = zip(src, src[1:])
# print(*a) # (300, 2) (2, 12) (12, 44) (44, 1) (1, 1) (1, 4) (4, 10) (10, 7) (7, 1) (1, 78) (78, 123) (123, 55)

result = (num for num_1, num in zip(src, src[1:]) if num > num_1)
print(*result)

print('\nразбор ДЗ с преподавателем')
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)
