import time
from math import floor, sqrt
from pprint import pprint
from random import randint


def martix_mul(a, b):
    k = len(a)
    c = [[0 for _ in range(k)] for _ in range(k)]

    for i in range(k):
        for j in range(k):
            for l in range(k):
                c[i][j] += a[i][l] * b[l][j]

    return c


def fast_pow(a, n):
    result = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]

    while n > 0:
        if n % 2 == 1:
            result = martix_mul(result, a)
        a = martix_mul(a, a)
        n //= 2

    return result


def scalar_mul(a, b):
    return sum(i * j for i, j in zip(a, b))


def linear(c, v, n):
    k = len(c)

    m = [c.copy()]
    for i in range(1, k):
        m.append([0 for _ in range(i - 1)] + [1] + [0 for _ in range(k - i)])

    fast_pow(m, n - k)

    return scalar_mul(m[0], v)


for n in range(100, 10_001, 100):
    k = floor(sqrt(n))

    c = [randint(1, 100) for _ in range(k)]
    v = [randint(1, 100) for _ in range(k)]

    __ = time.time()
    linear(c, v, n)
    __ = time.time() - __

    print(f'{n:>6}', __)
