# homework lesson: 7, task 1
"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""
matrix_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix_2 = [[3, 5, 8, 3], [8, 3, 7, 1]]
# тест на 3/2
matrix_3 = [[31, 22], [37, 43], [51, 86]]
matrix_4 = [[11, 3], [5, 2], [10, 4]]
# тест на 2/4
matrix_5 = [[3, 5, 8, 3], [8, 3, 7, 1]]
matrix_6 = [[1, 1, 1, 1], [1, 1, 1, 1]]
# тест на 3/3
matrix_7 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix_8 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


# [int(matrix_3[i][j]) for i in range(len(matrix_3)) for j in range(len(matrix_3[i]))]
# [int(matrix_4[i][j]) for i in range(len(matrix_4)) for j in range(len(matrix_4[i]))]

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self, result=''):
        for row in self.matrix:
            result += f"{'   '.join(map(str, row))}  \n"
        return result

    def __add__(self, other):
        tmp1 = list(sum(self.matrix, []))  # приведение матрицы к плоскому виду
        tmp2 = list(sum(other.matrix, []))
        tmp3 = [str(sum(i)) for i in zip(tmp1, tmp2)]  # сложение соответствующих элементов
        return Matrix([tmp3[i:i + len(self.matrix[0])] for i in range(0, len(tmp3), len(self.matrix[0]))])
        #  приведение списка к матричному виду


m = Matrix(matrix_7)
n = Matrix(matrix_8)
print(m)
print(m + n)
