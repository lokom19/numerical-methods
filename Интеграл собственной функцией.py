# -*- coding: utf-8 -*-

import numpy
from sympy import *
import time
import scipy
from scipy import integrate
import math

try:
    def f(x):
        return 1



    def f2(a, b, h):
        integ = 0
        for x in range(a, b, h):
            integ += ((f(x) + f(x - h)) / 2) * h
        return integ


    print(f2(-10, 10, 1))
except:
    print('Ошибка')



