from random import randint
from .find_primitive_root import is_prime, find_primitive


def generate_pg():
    p = randint(5, 30)
    while not is_prime(p):
        p = randint(2 ** 2047, 2 ** 2048)
    return p, find_primitive(p)
