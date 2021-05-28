original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'Исходный список: {original_list}') # исходный список

original_list_new = []

for idx in range(len(original_list)):
    current_item = original_list[idx]
    for idx_1 in current_item:
        has_number = False  # изначально предполагаем, что в элементе списка числа нет
        if idx_1.isdigit():  # в этом элементе списка есть число
            has_number = True

    if has_number:
        if '+' in original_list[idx]:  # если в элементе списка есть еще и знак +, то добавим его после кавычек
            original_list_new.extend(['"', f'+{int(current_item):02d}', '"'])
        else:
            original_list_new.extend(['"', f'{int(current_item):02d}', '"'])
    else:
        original_list_new.extend([current_item])

print(f'Промежуточный список: {original_list_new}\n')

print('ну а теперь соберем строку с учетом пробелов и кавычек, я пока увы не знаю способа лучше, поэтому собрала так :)')
result = ''
quotation_marks = 1 # закрывающая кавычка будет делится на два без остатка
in_quotation_marks = False
for idx in range(len(original_list_new)):
    if original_list_new[idx] == '"' and quotation_marks % 2 != 0: # после нечетной кавычки пробел не добавляем
        result += original_list_new[idx]
        quotation_marks += 1
        in_quotation_marks = True
    elif original_list_new[idx] == '"' and quotation_marks % 2 == 0: # после четной кавычки пробел добавляем
        result += original_list_new[idx] + ' '
        quotation_marks += 1
        in_quotation_marks = False
    elif in_quotation_marks: # это значит что мы находимся внутри кавычек и добавлять пробел после числа не будем
        result += original_list_new[idx]
    else:
        result += original_list_new[idx] + ' '

print(f'Результат: {result}')
