names_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
print(names_list)
for idx in names_list:
    name_person = idx.split()
    apostrophe = "'"
    print(f'{apostrophe}Привет, {name_person[-1].capitalize()}!{apostrophe}')
