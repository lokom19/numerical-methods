# -*- coding: utf-8 -*-
import numpy as np
import sys

try:
    n = int(input('Введите n (ширинну матрицы): '))
    m = int(input('Введите m (длину матрицы): '))

    if n <= 0 or m <= 0:
        print('Запустите программу заново и введите числовые положительные значения')
        sys.exit()
except:
    print('Введите корректные данные: ')

matrix = [[input('Введите число: ') for x in range(n)] for y in range(m)]
print('-----------------------')

print('Превоначальная матрица: ')
for i in range(0, m):
    print(matrix[i])
matrix_biblio = np.matrix(matrix)
print('-----------------------')
print(f'Транспонированная библиотекой матрица:\n {matrix_biblio.transpose()}')
#print(matrix)
# print([[x[i] for x in matrix] for i in range(n)])
print(f'Транспонированная собственной функцией матрица: {[[x[i] for x in matrix] for i in range(n)]}')


# for i in range(n):
#     for x in matrix:
#         print([x[i]]*m)