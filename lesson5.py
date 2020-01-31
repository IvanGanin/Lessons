import math_lib as ml


def all_func(number):
    print(f'Простое: {ml.test_prime(number)}')
    print(f'Делители: {ml.list_divisor(number)}')
    print(f'Самый большой простой делитель: {ml.max_prime_divisor(number)}')
    print(f'Произведение простых множителей: {ml.list_prime_numbers(number)}')
    print(f'Каноническое разложение: {number} == {ml.canonical_decomposition(number)}')
    print(f'Самый большой делитель: {ml.max_divisor(number)}')
    print()

while True:
    user_input = input(f'Введите число от 1 <= n <= {ml1.MAX_NUMBER} или нажмите [Enter]: ')

    if user_input == '':
        break

    if user_input.isdigit():
        n = int(user_input)
        if 1 <= n <= 1000:
            all_func(n)

        else:
            print(f'Не удовлетворяет условию: 1 =< {n} <= 1000.')

    else:
        print(f'{user_input} не число.')
