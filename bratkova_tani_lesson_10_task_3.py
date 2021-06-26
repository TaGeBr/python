"""
Реализовать программу работы с клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству
клеток (целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).
Данные методы должны выполнять увеличение,уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса
и количество клеток в ряду. Метод должен возвращать строку виду **\n\n**...,
где количество клеток между \n равно переданному аргументу, а количество рядов
определяется, исходя из общего количества клеток.
При создании экземпляра клетки должна происходить перезапись параметра,
который хранит количество клеток.
"""

class Cell:
    def __init__(self, number):
        self.number = number

    def make_cell(self, rows): # rows - это по сколько в ряду будет клеток
        return '\n'.join(['*' * rows for _ in range(self.number // rows)]) \
               + '\n' + '*' * (self.number % rows)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell((self.number - other.number)) if self.number - other.number > 0 \
            else '- невозможно, т.к. количество клеток не может быть отрицательным'

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))


cell_1 = Cell(15)
cell_2 = Cell(3)
cell_3 = Cell(4)
print(cell_1, cell_2, cell_3)
print('Сумма клеток: ', cell_1 + cell_2 + cell_3)
print('Вычитание клеток: ', cell_1 - cell_2 - cell_3)
print('Умножение клеток: ', cell_1 * cell_2 * cell_3)
print('Деление клеток: ', cell_1 / cell_2 / cell_3)
print(cell_1.make_cell(12))
