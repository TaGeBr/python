print('сначала решение "в лоб" как подсказывали в методичке')
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for num in src:
    if src.count(num) == 1:
        result.append(num)
print(result,'\n')

print('теперь оптимизированное решение')
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
[result.append(num) for num in src if src.count(num) == 1]
print(result)

print('\nразбор ДЗ с преподавателем')
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])
