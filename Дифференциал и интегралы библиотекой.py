# -*- coding: utf-8 -*-


import numpy
from sympy import *
import time
import scipy
from scipy import integrate

time1 = time.time()
x = Symbol('x')


########################################
y1 = lambda x: 5 ** x  # Исходная функция
yperv = integrate.quad(y1, -10, 10)[0]
print(f'Ваш интеграл: {yperv}\nот функции {y1(x)}')
###############################################


print('---------------------------')


y = cos(x)  # Исходная функция дифференцирования
ydiff = y.diff()
print()
print(f'Ваша производная: {ydiff}\nот функции {y}')
