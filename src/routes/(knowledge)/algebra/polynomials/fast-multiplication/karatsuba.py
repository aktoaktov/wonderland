@cache
def m_count(n):
    if n == 0:
        return 1
    else:
        return 2 * m_count(n // 2) + m_count((n - 1) // 2)


def karatsuba(p, q):
    global M, A
    # Удаляем ведущие нули
    p = trim_zeros(p)
    q = trim_zeros(q)
    # Базовый случай: если один из многочленов нулевой
    if not p or not q:
        return []
    # Базовый случай: умножение констант
    if len(p) == 1 and len(q) == 1:
        M += 1
        return [p[0] * q[0]]
    # Выравниваем длины, не дополняя нулями
    n = max(len(p), len(q))
    k = n // 2
    # Разбиваем на части
    a = p[:k] if len(p) >= k else p
    b = p[k:] if len(p) > k else []
    c = q[:k] if len(q) >= k else q
    d = q[k:] if len(q) > k else []
    # Рекурсивные вызовы (3 умножения)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    # Вычисляем a + b и c + d с учётом разных длин
    a_plus_b = add_poly(a, b)
    c_plus_d = add_poly(c, d)
    A += len(a_plus_b) + len(c_plus_d)  # Учёт сложений
    ad_plus_bc = karatsuba(a_plus_b, c_plus_d)
    # Вычисляем (a+b)(c+d) - ac - bd
    ad_plus_bc = subtract_poly(subtract_poly(ad_plus_bc, ac), bd)
    A += 2 * max(len(ad_plus_bc), len(ac), len(bd))  # Учёт вычитаний
    # Собираем результат
    result = [0] * (len(p) + len(q) - 1)
    for i, val in enumerate(ac):
        result[i] += val
    for i, val in enumerate(ad_plus_bc):
        result[i + k] += val
    for i, val in enumerate(bd):
        result[i + 2 * k] += val
    return result


def trim_zeros(poly):
    """Удаляет ведущие нули."""
    while len(poly) > 0 and poly[-1] == 0:
        poly = poly[:-1]
    return poly or [0]


def add_poly(p, q):
    """Сложение многочленов p + q."""
    return [a + b for a, b in zip(p, q)] + p[len(q):] + q[len(p):]


def subtract_poly(p, q):
    """Вычитание многочленов p - q."""
    return [a - b for a, b in zip(p, q)] + p[len(q):] + [-x for x in q[len(p):]]


for n in range(0, 100):
    M = 0  # Умножения
    A = 0  # Сложения/вычитания
    p = [randint(1, 10) for _ in range(n + 1)]
    q = [randint(1, 10) for _ in range(n + 1)]
    result = karatsuba(p, q)
    print(n, '-', M, m_count(n))
    # print(M, end=' ')

plt.plot([m_count(n) for n in range(1, 1_000_00)])
plt.plot([3 ** (floor(log2(n)) + 1) for n in range(1, 1_000_00)])
plt.plot([n ** log2(3) for n in range(1, 1_000_00)])
plt.plot([3 * n ** log2(3) for n in range(1, 1_000_00)])
# plt.xscale('log')
plt.show()
