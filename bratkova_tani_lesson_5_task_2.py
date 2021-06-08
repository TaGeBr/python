import sys

count_num = int(input('Укажите количество чисел (n): '))
nums_gen = (num for num in range(1, count_num + 1, 2))
print(type(nums_gen), 'размер в памяти', sys.getsizeof(nums_gen))
# for idx in nums_gen:
#     print(idx)

# for idx in range(20):
#     print(next(nums_gen))

print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
