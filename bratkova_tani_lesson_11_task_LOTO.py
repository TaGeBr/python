import random
class LotoCard:
    _numbers_stroked_human = 0  # сколько чисел на карточке зачеркнул игрок
    _numbers_stroked_computer = 0  # сколько чисел на карточке зачеркнул компьютер
    """_MAX_NUMBER_IN_CARD = 15 тут я хотела сделать меньше 15 чисел на карточке, и запрашивать с экрана, но потом увидела, 
    что у нас подвязано количество чисел 5 и пробелов 4 и успокоилась, но обратно переделывать нет времени, оставила так"""
    _MAX_NUMBER_IN_CARD = 15

    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        # self._MAX_NUMBER_IN_CARD = 15
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)
        for line in self._card:
            for _ in range(NEED_SPACES): # добавим четыре пробела
                line.append(' ')
            for _ in range(NEED_NUMBERS): # добавим пять чисел
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def __str__(self):
        text = f'{self.player_type} :'
        print("\033[31m {} \033[0m".format(text))
        print('-' * 22)
        return '\n'.join([' '.join(map(str, line)) for line in self._card])

    def has_number(self, keg_find, yes_no):
        self.keg_find = keg_find
        self.yes_no = yes_no
        find_ok = False
        for lst in self._card:
            try:
                index = lst.index(self.keg_find) # значит такой элемент есть
                find_ok = True
                break
            except ValueError:
                continue

        if self.yes_no == 'y' and find_ok == True:
            return True
        elif self.yes_no == 'y' and find_ok == False:
            return False
        elif self.yes_no == 'n' and find_ok == True:
            return False
        elif self.yes_no == 'n' and find_ok == False:
            return True


    def strike_out(self, keg_strike_out):
        self.keg_strike_out = keg_strike_out
        for lst in self._card:
            try:
                index = lst.index(self.keg_strike_out)
                lst[index] = '--'  # на что заменим
                if self.player_type == 'Игрок':
                    LotoCard._numbers_stroked_human += 1
                else:
                    LotoCard._numbers_stroked_computer += 1
                break
            except ValueError:
                continue


class LotoGame:
    _list_kegs = list(range(1, 91))

    def keg_pull_out(self):
        self._new_keg = random.choice(LotoGame._list_kegs)
        LotoGame._list_kegs.remove(self._new_keg)

        text = f'Новый бочонок {self._new_keg}, осталось {len(LotoGame._list_kegs)}'
        print("\033[34m{} \033[0m".format(text))
        answer = input('\033[34mХотите зачеркнуть? y/n: \033[0m')
        return self._new_keg, answer


human = LotoCard('Игрок')
computer = LotoCard('Компьютер')
no_lox = True

while (computer._numbers_stroked_computer < LotoCard._MAX_NUMBER_IN_CARD) and (computer._numbers_stroked_human < LotoCard._MAX_NUMBER_IN_CARD) and (no_lox == True):
    print(human)
    print(computer)

    game_new = LotoGame()
    keg, yes_no = game_new.keg_pull_out() # тут у нас в keg случайный бочонок, в yes_no - ответ y/n

    """
    ЕСЛИ ЗАКОММЕНТИРОВАТЬ С 106 ПО 111 СТРОЧКИ, ТО МОЖНО НЕ ВВОДИТЬ Y/N, А ПРОСТО ДАВИТЬ ENTER И ТАК ПРОВЕРИТЬ ТРИ ПОЗИЦИИ "НИЧЬЯ", "ВЫИГРАЛ КОМПЬЮТЕР!!!", "ВЫИГРАЛ ЧЕЛОВЕК"
    """
    no_lox = human.has_number(keg, yes_no)
    if no_lox == False: # игрок лох, игра окончена
        print('Игрок, увы, Вы проиграли! Игра окончена!')
    else:
        human.strike_out(keg)
        computer.strike_out(keg)

    human.strike_out(keg)
    computer.strike_out(keg)

if (computer._numbers_stroked_computer == LotoCard._MAX_NUMBER_IN_CARD) and (computer._numbers_stroked_human == LotoCard._MAX_NUMBER_IN_CARD):
    print('НИЧЬЯ!!!')
elif (computer._numbers_stroked_computer == LotoCard._MAX_NUMBER_IN_CARD):
    print('ВЫИГРАЛ КОМПЬЮТЕР!!!')
elif computer._numbers_stroked_human == LotoCard._MAX_NUMBER_IN_CARD:
    print('ВЫИГРАЛ ЧЕЛОВЕК!!!')
