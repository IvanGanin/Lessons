import math_lib as ml

#1
def test_init_prime_numbers(n):
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
#2
def test_prime(n):
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

#3
def test_list_divisor(n):
    assert isinstance(n, int)
    assert 1 <= n

    if n == 1:
        return []

    ld = []

    for i in range(2, n):
        if n % i == 0:
            ld.append(i)

    return ld

#4
def test_list_prime_numbers(n):
    assert isinstance(n, int)
    assert 1 <= n <= ml.MAX_NUMBER

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

#5
def test_max_divisor(n):
    assert isinstance(n, int)
    assert 1 <= n <= MAX_NUMBER

    if n == 1:
        return None

    for i in prime_numbers:
        if i > sqrt(n):
            return None

        if n % i == 0:
            return n // i

    return None
