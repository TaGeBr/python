

def thesaurus(list_names):
    # сначала получим первые буквы фамилий для ключа
    pair_name_surname = []
    for idx in list_names:
        pair_name_surname.append(idx.split(' '))
    print('В исходном списке разделили имя и фамилию\n', pair_name_surname)

    f_sym_surname = []
    for idx in range(len(pair_name_surname)):
        f_sym_surname.append(pair_name_surname[idx][1][0])
    f_sym_surname = list(set(f_sym_surname))  # первые буквы фамилий для ключа
    print('Первые буквы фамилий для ключа\n',f_sym_surname)

    list_first_symb = []
    for first_symbol in list_names:
        list_first_symb.append(first_symbol[0])
    list_first_symb = list(set(list_first_symb))

    names_dict = {}
    for symbol in sorted(list_first_symb):
        list_names_one_sym = list(filter(lambda el: el.startswith(symbol), list_names))
        names_dict.setdefault(symbol, list_names_one_sym)
    return names_dict

names = ['Иван Андреев', 'Анна Лазарева', 'Георгий Иванов', 'Елена Арбузова', 'Марина Цветаева', 'Игорь Цзин', 'Бэлла Лучникова',
         'Мария Антонова', 'Евгений Алейников', 'Галина Инженерова', 'Михаил Цой', 'Антон Рыжиков', 'Маргарита Лютикова',
         'Владимир Ростовщиков', 'Борис Акулов']
print('Исходный список\n', names)
result = thesaurus(names)
print('Ну и просто по первой букве имени - и по фамилиям, и по имени не сделала\n',result)
for key, val in result.items():
    print(key, val)
