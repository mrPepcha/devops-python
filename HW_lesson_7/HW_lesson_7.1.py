#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
#Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

from typing import List

class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

    def __add__(self, other: "Matrix") -> "Matrix":
        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])



matrix1 = Matrix([[1, 9], [9, 0]])
matrix2 = Matrix([[11, 22], [33, 44]])
print(matrix1, '\n')
print(matrix2, '\n')
print(matrix1 + matrix2)
