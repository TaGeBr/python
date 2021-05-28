# это решение мне нравится - оно красивое, здесь мы берем элемент списка и проверяем число ли это, и сразу обрамляем в кавычки
print('РЕШЕНИЕ 1 - КРАСИВОЕ!!!')
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(original_list)

for idx in range(len(original_list)):

    elem_list = original_list[idx]

    if '+' in elem_list:  # если вдруг перед числом стоит + то уберем его пока
        elem_list = elem_list.replace('+', '')
        if elem_list.isdigit():
            original_list[idx] = f'"+{int(elem_list):02d}"'
    elif elem_list.isdigit():  # ну а это просто числа (без знака плюс), которые встречаются в тексте
        original_list[idx] = f'"{int(elem_list):02d}"'

print(' '.join(original_list),'\n')


# а тут решение не такое красивое - это я вначале мучилась и оставила для примера, тут мы просто добавляем текст в строку
print('РЕШЕНИЕ 2 - НЕ ТАКОЕ КРАСИВОЕ КАК 1 РЕШЕНИЕ!!!')
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(original_list) # исходный список

line_end = '' # Строка в которой соберем наше новое предложение

for idx in range(len(original_list)):

    has_number = False # изначально предполагаем, что в элементе списка числа нет

    for idx_1 in original_list[idx]:
        if idx_1.isdigit(): # в этом элементе списка есть число
            has_number = True

    if has_number:
        if '+' in original_list[idx]: # если в элементе списка есть еще и знак +, то добавим его после кавычек
            line_end += f'"+{int(original_list[idx]):02d}"'
        else:
            line_end += f'"{int(original_list[idx]):02d}"'
    else:
        line_end += original_list[idx]
    line_end += ' '

print(line_end)
