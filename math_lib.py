from math import sqrt
from collections import Counter


def init_prime_numbers(n):  # Генерация таблицы простых чисел не превышающих n
    assert isinstance(n, int)
    assert n > 1

    pn = [2]
    for i in range(pn[-1] + 1, n + 1):
        for j in pn:
            if j > sqrt(i):
                pn.append(i)
                break

            if i % j == 0:
                break

    return pn


MAX_NUMBER = 1000
prime_numbers = init_prime_numbers(MAX_NUMBER)


def test_prime(n):  # проверка числа на простоту
    assert isinstance(n, int)
    assert 1 <= n <= MAX_NUMBER

    if n == 1:
        return False

    for i in prime_numbers:
        if i > sqrt(n):
            return True

        if n % i == 0:
            return False

    return True


def list_divisor(n):  # выводит список всех делителей числа
    assert isinstance(n, int)
    assert 1 <= n

    if n == 1:
        return []

    ld = []

    for i in range(2, n):
        if n % i == 0:
            ld.append(i)

    return ld


def max_prime_divisor(n):  # выводит самый большой простой делитель числа
    assert isinstance(n, int)
    assert 1 <= n <= MAX_NUMBER

    if n == 1:
        return None

    for i in prime_numbers[::-1]:
        if i >= n:
            continue

        if n % i == 0:
            return i

    return None


def list_prime_numbers(n):  # выводит разложение числа на простые множители
    assert isinstance(n, int)
    assert 1 <= n <= MAX_NUMBER

    if n == 1:
        return []

    pn = []
    temp = n

    for i in prime_numbers:
        if i >= n:
            return pn

        while temp % i == 0:
            pn.append(i)
            temp //= i

    return pn


def canonical_decomposition(n):  # выводит каноническое разложение числа на простые множители
    pn = list_prime_numbers(n)
    cd = sorted(list(Counter(pn).items()))
    print_str = ''
    for x, y in cd:
        print_str += f'{x} * ' if y == 1 else f'{x}**{y} * '
    return print_str[:-3]


def max_divisor(n):  # выводит самый большой делитель (не обязательно простой) числа
    assert isinstance(n, int)
    assert 1 <= n <= MAX_NUMBER

    if n == 1:
        return None

    for i in prime_numbers:
        if i > sqrt(n):
            return None

        if n % i == 0:
            return n // i  # Число деленное на наименьший простой делитель

    return None


if __name__ == '__main__':
    tpn1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    tpn2 = init_prime_numbers(100)
    print(tpn1)
    print(tpn2)
    print('Первые до 100 числа верны:', tpn1 == tpn2)