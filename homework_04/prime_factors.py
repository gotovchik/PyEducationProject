# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from math import sqrt


def get_prime_factors(n):
    prime_factors = []
    # находим сколько раз число можно разделить на 2
    while n % 2 == 0:
        prime_factors.append(2)
        n /= 2
    # у каждого составного числа не может быть более 1 простого множителя > sqrt(n)
    # множители нечетные, поэтому шаг цикла = 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n /= i
    # оставшееся число либо простой множитель, либо равен 1
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors


def show_prime_factors(n, col):
    for i in col:
        print(f'{int(n)}|{i}')
        n /= i


print('Привет!\nЭто программа покажет вам список всех простых множителей числа.')
number = int(input('Введите число: '))
factors = get_prime_factors(number)
print(f'Список простых множителей: {factors}')
show_prime_factors(number, factors)
