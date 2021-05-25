duration_user = input('Введите время в секундах - можно несколько разных значений через пробел: ')
# print(type(duration_user), duration_user)

# теперь преобразуем в список, но пока он будет из строк
duration_user = duration_user.split()
# print(type(duration_user), duration_user)

# теперь преобразуем в список из чисел
duration_user = [int(num) for num in duration_user]
# print(type(duration_user), duration_user)

for idx in range(len(duration_user)): # В этой строке я поправила переменную для индекса - вспомнила что i лучше не использовать
    duration = duration_user[idx]
    if duration < 60:
        print('duration = ', duration)
        print(duration, 'сек')
    elif duration >= 60 and duration < 3600:
        print('duration = ', duration)
        print(duration // 60, 'мин', duration % 60, 'сек')
    elif duration >= 3600 and duration < 86400:
        print('duration = ', duration)
        hours = duration // 3600
        minutes = ((duration-(duration // 3600 * 3600))) // 60
        seconds = duration % 60
        print(hours, 'час', minutes, 'мин', seconds, 'сек')
    else:
        print('duration = ', duration)
        days = duration // 86400
        hours = ((duration - (duration // 86400 * 86400))) // 3600
        minutes = ((duration - (duration // 3600 * 3600))) // 60
        seconds = duration % 60
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
