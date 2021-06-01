def thesaurus(list_names):
    list_first_symb = []
    for first_symbol in list_names:
        list_first_symb.append(first_symbol[0])
    list_first_symb = list(set(list_first_symb))
    # print(list_first_symb)

    names_dict = {}
    for symbol in sorted(list_first_symb):
        list_names_one_sym = list(filter(lambda el: el.startswith(symbol), list_names))
        names_dict.setdefault(symbol, list_names_one_sym)
    return names_dict


names = ['Иван', 'Анна', 'Георгий', 'Елена', 'Марина', 'Игорь', 'Бэлла', 'Мария', 'Евгений',
         'Галина', 'Михаил', 'Антон', 'Маргарита', 'Владимир', 'Борис']
print('Исходный список:\n',names)
result = thesaurus(names)
print('\nСписок по первой букве:\n', result)
print('\nСписок по первой букве в столбец:')
for key, val in result.items():
    print(key, val)



# ЧЕРЕЗ РАСПАКОВКУ АРГУМЕНТОВ
print(f'\n\nчерез распаковку аргументов\n'.upper())


def thesaurus(*args):
    list_first_symb = []
    for first_symbol in args:
        list_first_symb.append(first_symbol[0])
    list_first_symb = list(set(list_first_symb))

    names_dict = {}
    for symbol in sorted(list_first_symb):
        list_names_one_sym = list(filter(lambda el: el.startswith(symbol), args))
        names_dict.setdefault(symbol, list_names_one_sym)
    return names_dict


names = ['Эвелина', 'Андрей', 'Эдуард', 'Александр', 'Элла']
print('Исходный список:\n',names)
result = thesaurus(*names)
print('\nСписок по первой букве:\n', result)
print('\nСписок по первой букве в столбец:')
for key, val in result.items():
    print(key, val)
