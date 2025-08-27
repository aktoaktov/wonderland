import time
from math import floor, sqrt
from pprint import pprint
from random import randint

def mul(a, b, c):
    k = len(a)

    res = [0] * (2 * k - 1)
    for i in range(k):
        for j in range(k):
            res[i + j] += a[i] * b[j]

    for i in range(2 * k - 2, k - 1, -1):
        for j in range(k):
            res[i - k + j] += res[i] * c[j]

    return res[:k]



def matrix_pow(p, c):
    k = len(c)

    if p == 0:
        return [1] + [0] * (k - 1)
    if p == 1:
        return [0, 1] + [0] * (k - 2)

    half = matrix_pow(p // 2, c)
    res = mul(half, half, c)

    if p % 2 == 1:
        res = mul(res, [0, 1] + [0] * (k - 2), c)

    return res

def linear(c, v, n):
    k = len(c)

    coeff = matrix_pow(n - 1, c)

    # Вычисляем x_n как линейную комбинацию начальных значений
    x_n = 0
    for i in range(k):
        x_n += coeff[i] * initial[k - 1 - i]
    return x_n


