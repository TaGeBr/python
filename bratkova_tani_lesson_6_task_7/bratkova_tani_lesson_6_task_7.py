import sys

with open('bakery.txt', 'w') as f: # вернем цифры к исходному условию задачи
    f.write('5978,5\n8914,3\n7879,1\n1573,7')

which_replace = int(sys.argv[1])
val_new = sys.argv[2]

with open('bakery.txt', 'r+') as f:
    # это не чтение файла целиком, а построчно положили в список
    list_bakery = [line.strip() for idx, line in enumerate(f)]
    print(list_bakery, 'старое содержимое файла')
    if which_replace not in list(range(1, len(list_bakery)+1)):
        exit('error')
    else:
        list_bakery[which_replace-1] = val_new # здесь мы заменяем нужный элемент
    print(list_bakery, 'новое содержимое файла')

    f.seek(0) # ох, и потратила я времени, если не перейти на начало файла то добавляет много nul
    f.truncate(0)
    for elem in list_bakery:
        f.write(elem)
        f.write('\n')
