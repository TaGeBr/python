import sys


# Генератор через функцию
def uneven_nums_gener(num):
    for num in range(1, num + 1, 2):
        yield num


# через next
count_num = int(input('Укажите количество чисел (n): '))
print('Иван, посмотрите, пожалуйста, комментарий внизу программы. Почему сообщение StopIteration всегда'
      ' в разном месте появляется, либо внизу, либо после первого числа')
nums_gen = uneven_nums_gener(count_num)
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

# Укажите количество чисел (n): 15
# 1
# Traceback (most recent call last):
#   File "C:\Users\днс\PycharmProjects\code\MAY_2021\LESSON5\bratkova_tani_lesson_5_task_1_1.py", line 23, in <module>
#     print(next(nums_gen))
# StopIteration
# 3
# 5
# 7
# 9
# 11
# 13
# 15
