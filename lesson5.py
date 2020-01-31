import math_lib as dm


def all_func(number):
    print(f'Простое: {dm.test_prime(number)}')
    print(f'Делители: {dm.list_divisor(number)}')
    print(f'Самый большой простой делитель: {dm.max_prime_divisor(number)}')
    print(f'Произведение простых множителей: {dm.list_prime_numbers(number)}')
    print(f'Каноническое разложение: {number} == {dm.canonical_decomposition(number)}')
    print(f'Самый большой делитель: {dm.max_divisor(number)}')
    print()

while True:
    user_input = input(f'Введите число от 1 <= n <= {dm.MAX_NUMBER} или нажмите [Enter]: ')

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
