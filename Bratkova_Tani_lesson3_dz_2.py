english_numerals = {'zero': 'ноль', 'one': 'один', 'two': 'два',
                    'three': 'три', 'four': 'четыре', 'five': 'пять',
                    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                    'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(numerals):
    if not numerals[0].islower():
        numerals = english_numerals.get(numerals.lower()).capitalize()
    else:
        numerals = english_numerals.get(numerals)
    return numerals


user_numerals = input('Введите числительное на английском языке от 0 до 10, например - "one" или "One": ')
print(num_translate_adv(user_numerals))
if not num_translate_adv(user_numerals):
    print('вы ввели не то, что вас просили')
