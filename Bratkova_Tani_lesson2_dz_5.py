price_list = [57.8, 46.51, 97, 31.12, 98, 125.52, 570, 5.03, 9, 75.7, 82]
print(price_list, id(price_list))
price_list_1 = ['%.2f' % number for number in price_list] # все числа в массиве c двумя знаками после запятой
price_list_one = [] # это массив для формата 57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп,...

for idx in price_list_1:
    integer_part, float_part = idx.split('.')  # здесь отделили целую часть от дробной
    new_price = f'{integer_part} руб {float_part} коп'
    price_list_one.append(new_price)
message = ', '.join(price_list_one)
print(message)

print('\nсписок - сортировка цен по возрастанию (не создавали новый список - id не изменился:)')
print(price_list, id(price_list))
price_list.sort()
print(price_list, id(price_list))

print('\nсписок сортировка цен по убыванию (создали новый список - id изменился:)')
print(price_list, id(price_list))
price_list = sorted(price_list, reverse=True)
print(price_list, id(price_list))

print('\nцены пяти самых дорогих товаров:')
price_list = [57.8, 46.51, 97, 31.12, 98, 125.52, 570, 5.03, 9, 75.7, 82]
print(price_list, id(price_list))
price_list.sort(reverse=True)
print(price_list[:5][::-1], id(price_list)) # добавила [::-1], чтобы было в порядке возрастания и сделала новый commit на ГитХаб
