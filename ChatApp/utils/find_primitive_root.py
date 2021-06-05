"""
I took parts of this code from https://www.geeksforgeeks.org/primitive-root-of-a-prime-number-n-modulo-n/
"""
from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if not n % 2 or not n % 3:
        return False
    i = 5
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6

    return True


def power(x, y, p):
    res = 1
    x %= p
    while y > 0:
        if y & 1:
            res = (res * x) % p

        y >>= 1
        x = (x * x) % p

    return res


def find_prime_factors(s, n):
    while n % 2 == 0:
        s.add(2)
        n = n // 2

    for i in range(3, int(sqrt(n)), 2):
        while n % i == 0:
            s.add(i)
            n //= i
    if n > 2:
        s.add(n)


def find_primitive(n):
    s = set()
    if not is_prime(n):
        return -1
    phi = n - 1
    find_prime_factors(s, phi)
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if power(r, phi // it, n) == 1:
                flag = True
                break
        if not flag:
            return r
    return -1
