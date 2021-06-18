import re


def email_parse(dict_name, email_address):
    # адрес целиком, если он нормальный, то работаем с ним дальше

    # ^[a-z0-9] первый символ только цифра или латинская буква
    #[a - z0 - 9._ -]+ только лотинские буквы, цифры, . _ - с второго символа до @
    # [a-z0-9] последний символ перед @ только цифра или латинская буква
    # строго только @
    # [a-z]+ только латинские буквы
    # \.[a-z] только . и сразу же за ней только латинские буквы

    full_address = re.findall('^[a-z0-9][a-z0-9._-]+[a-z0-9]@[a-z]+\.[a-z]+', email_address)
    if not full_address:
        msg = f'wrong email: {email_address}'
        # raise ValueError(msg)
        return(msg)

    full_address = full_address[0].replace('@', '/@')
    full_address = list(full_address.split('/'))
    dict_name['username'] = full_address[0]
    dict_name['domain'] = full_address[1]
    return dict_name


if __name__ == '__main__':
    dict_email = {}
    print('КОРРЕКТНЫЕ АДРЕСА: руководствовалась правила регистрации на mail.ru')
    print(email_parse(dict_email, 'someone@geekbrains.ru'))
    print(email_parse(dict_email, '1s.o-me__one@geekbrains.ru'))
    print(email_parse(dict_email, '1som.eone@geekbrains.ru'))

    print()
    print('ДАЛЬШЕ АДРЕСА С ОШИБКАМИ: # raise ValueError(msg) я отработала в 9 строке, '
          '\nпотом закомментировала, чтобы не вылетать после него и отправила сообщение'
          '\nчерез return. Единственное, что не получилось сделать - нельзя, чтобы в username'
          '\nиспользовалось два раза подряд "..", "__", "--" или комбинация этих символов. '
          '\nТут, конечно, есть и другие моменты которые нужно доработать, но я думаю с практикой '
          '\nбуду составлять эти выражения одной левой :)')

    print('\nадрес начинается с недопустимого символа (что-то кроме цифры или латинской буквы)')
    print(email_parse(dict_email, '_som_eone@geekbrains.ru'))

    print('\nадрес содержит перед @ недопустимый символ (что-то кроме цифры или латинской буквы)')
    print(email_parse(dict_email, '1som_eone_@geekbrains.ru'))

    print('\nнет точки в почтовом домене')
    print(email_parse(dict_email, '1som_eone@geekbrainsru'))

    print('\nотсутствует часть адреса между @ и точкой')
    print(email_parse(dict_email, '1som_eone@.ru'))

    print('\nцифра в почтовом домене')
    print(email_parse(dict_email, '1som_eone@geekbr2ains.ru'))
