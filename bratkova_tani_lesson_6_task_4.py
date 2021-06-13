"""
Task 4
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее
проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить
объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел
после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""

from itertools import zip_longest
out_dict = {}
with open('task4.txt', 'w', encoding='utf-8') as f:
    with open('users.txt', encoding='utf-8') as users:
        with open('hobby.txt', encoding='utf-8') as hobby:
            num_lines_users = sum(1 for line in users) # подсчитаем кол-во строк в users.txt
            num_lines_hobby = sum(1 for line in hobby) # подсчитаем кол-во строк в hobby.txt

            if num_lines_users < num_lines_hobby:
                print('Людей меньше, чем хобби, поэтому согласно условию задачи выходим')
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                # f.write(f'{line_user.strip()}: '
                #         f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')
                f.write(f'{line_user.strip()}: {line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')
