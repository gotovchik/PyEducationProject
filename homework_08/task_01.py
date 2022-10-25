"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init()__), который должен принимать данные (список списков)
для формирования матрицы. [[], [], []]
Следующий шаг — реализовать перегрузку метода
__str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, col):
        self.col = col

    def __str__(self):
        return '\n'.join(map(str, self.col))

    def __add__(self, other):
        return [[self.col[i][j] + other.col[i][j] for j in range
        (len(self.col[0]))] for i in range(len(other.col))]


matrix1 = Matrix([[3, 5, 6],
                  [1, 2, 3],
                  [4, 5, 7]])
print(f'Первая матрица:\n{matrix1}')

matrix2 = Matrix([[7, 9, 12],
                  [4, 5, 7],
                  [12, 4, 6]])
print(f'Вторая матрица:\n{matrix2}')

res_matrix = matrix1 + matrix2
print('Результат суммы матриц:')
for i in res_matrix:
    print(i)
