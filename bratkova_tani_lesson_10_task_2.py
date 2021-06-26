"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    _materials = 0  # эта переменная для общего расхода материалов

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc_method(self):
        pass


class Coat(Clothes):

    @property
    def calc_method(self): # self - размер
        calc = round((self.param / 6.5 + 0.5), 2)
        Clothes._materials += calc
        return calc


class Suit(Clothes):

    @property # если не указать этот декоратор, то получим <bound method Suit.calc_method of <__main__.Suit object at 0x00000262FD6C7F70>>
    def calc_method(self): # self - рост
        calc = round((2 * self.param + 0.3), 2)
        Clothes._materials += calc
        return calc


my_coat = Coat(48)
print(f'Расход ткани на пальто (размер {my_coat.param}) - {my_coat.calc_method} м,'
      f' тут конечно \nна два пальто хватит, но видимо человек, писавший методичку, не в теме :)\n')

my_suit = Suit(1.80)
print(f'Расход ткани на костюм (рост {my_suit.param}) - {my_suit.calc_method} м\n')

my_suit_1 = Suit(1.88)
print(f'Расход ткани на еще один костюм (рост {my_suit_1.param}) - {my_suit_1.calc_method} м\n')

print(f'Общий расход материалов - {Clothes._materials} м')
