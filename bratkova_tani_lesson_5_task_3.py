from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9Г']

tutors_klass = (tut_class for tut_class in zip(tutors, klasses))
print(tutors_klass)
print(*tutors_klass)
print(*tutors_klass, 'Тут генератор уже истощился')


print('\nВариант когда второй список короче первого')

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б']

# longest = range(len(tutors))
# tutors_klass = (tut_class for tut_class in zip_longest(tutors, klasses, longest, fillvalue='?'))

tutors_klass = (tut_class for tut_class in zip_longest(tutors, klasses, fillvalue = None))
print(tutors_klass)
print(*tutors_klass)
