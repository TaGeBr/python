english_numerals = {'zero': 'ноль', 'one': 'один', 'two': 'два',
                    'three': 'три', 'four': 'четыре', 'five': 'пять',
                    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                    'nine': 'девять', 'ten': 'десять'}


def num_translate(numerals):
    return english_numerals.get(numerals)


user_numerals = input('Введите числительное на английском языке от 0 до 10, например - one: ')
print(num_translate(user_numerals))
