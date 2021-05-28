'''
Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
'''

result_1 = 15 * 3
result_2 = 15 / 3
result_3 = 15 // 2
result_4 = 15 ** 2

print('Тип результата выражений:')
print(f'15 * 3 = {result_1} {type(result_1)} {isinstance(result_1, int)}')
print(f'15 / 3 = {result_2} {type(result_2)} {isinstance(result_2, float)}')
print(f'15 // 2 = {result_3} {type(result_3)} {isinstance(result_3, int)}')
print(f'15 ** 2 = {result_4} {type(result_4)} {isinstance(result_4, int)}')
