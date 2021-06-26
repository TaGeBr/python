"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
© geekbrains.ru 19Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, add_matrix):
        # # оба варианта сложения матриц (две строки ниже) работают
        result = [list(map(lambda x, y: x + y, self.matrix[i], add_matrix.matrix[i])) for i in range(len(self.matrix))]
        # result = ([[x + y for x, y in zip(a, b)] for a, b in zip(self.matrix, add_matrix.matrix)])
        return Matrix(result)

        # # это был выстраданный костыль, тут я тренировалась
        # rezult = [[0, 0], [0, 0]]
        # for i in range(len(self.width)):
        #     for j in range(len(self.width[0])):
        #         rezult[i][j] = self.width[i][j] + other.width[i][j]

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])
        # НИЖЕ БЫЛО МОЁ РЕШЕНИЕ __str__, НО В ИТОГЕ ЭТО НЕ СТРОКОВЫЙ ТИП
        # # ВЫВОД МАТРИЦЫ В ПРИВЫЧНОМ ВИДЕ
        # for row in self.matrix:
        #     for x in row:
        #         print('{:4d}'.format(x), end='')
        #     print()
        # return f"Объект с параметрами ({self.matrix})"


matrix_1 = Matrix([[10, 20], [30, 40], [50, 60]])
matrix_2 = Matrix([[10, 20], [30, 40], [50, 60]])
matrix_3 = Matrix([[10, 20], [30, 40], [50, 60]])
matrix_4 = Matrix([[10, 20], [30, 40], [50, 60]])

print(matrix_1, '\n')

matrix_new = matrix_1 + matrix_2 + matrix_3 + matrix_4
print(matrix_new)
