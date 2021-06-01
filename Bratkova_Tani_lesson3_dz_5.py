from random import choice

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']


def get_jokes(num_jokes, flag, list_1, list_2, list_3):
    """this function returns n jokes of three words taken from three lists"""
    jokes = []
    # так как будем удалять использованные слова при параметре flag = нет, то сделаем копии списков
    nouns_copy, adverbs_copy, adjectives_copy = list_1.copy(), list_2.copy(), list_3.copy()
    for idx in range(num_jokes):
        word_1 = choice(nouns_copy)
        word_2 = choice(adverbs_copy)
        word_3 = choice(adjectives_copy)
        jokes.append(f'{word_1} {word_2} {word_3}')
        if not flag:
            nouns_copy.remove(word_1)
            adverbs_copy.remove(word_2)
            adjectives_copy.remove(word_3)
    return jokes

how_many_jokes = 0
print(help(get_jokes))
while how_many_jokes < 1 or how_many_jokes > 5:
    how_many_jokes = int(input('Введите количество шуток от 1 до 5: '))
flag_repeat = False
if input('Можно ли повторять слова в шутках? (да/нет): ') == 'да':
    flag_repeat = True

# пять разных вариантов, где списки поменяны местами, получим пять разных результатов
print(get_jokes(how_many_jokes, flag_repeat, nouns, adverbs, adjectives))
print(get_jokes(how_many_jokes, flag_repeat, adverbs, nouns, adjectives))
print(get_jokes(how_many_jokes, flag_repeat, adjectives, adverbs, nouns))
print(get_jokes(how_many_jokes, flag_repeat, adverbs, adjectives, nouns))
print(get_jokes(how_many_jokes, flag_repeat, adjectives, nouns, adverbs))

# с именованными параметрами, параметры специально не по порядку, чтобы видно было как это работает
print(f'\nС именованными параметрами:\n{get_jokes(how_many_jokes, flag_repeat, list_3=adjectives, list_1=nouns, list_2=adverbs)}')
