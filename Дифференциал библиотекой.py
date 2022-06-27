# -*- coding: utf-8 -*-

import numpy
from sympy import *
import time
import scipy
from scipy import integrate
from scipy.misc import derivative

ycor_diff1 = []
xcor_diff1 = []
diff_list1 = []


def f(x):
    return sin(x)  # Исходная функция дифференцирования


def diff1(a, b, h):
    c = 1000
    for x in range(int(a * c), int(b * c) + 1, int(h * c)):
        diff1 = derivative(f, x/c, h)
        diff_list1.append(diff1)
        ycor_diff1.append(f(x/c))
        xcor_diff1.append(x/c)
        print(f'x {x/c} Производная {diff1}')
    return xcor_diff1, ycor_diff1, diff_list1

diff1(-1, 1, 0.001)