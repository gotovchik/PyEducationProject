# Было:
# def is_prime(num):
#     prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
#     i = 5
#     d = 2

#     while prime and i * i <= num:
#         prime = num % i != 0
#         i += d
#         d = 6 - d
#     return prime

# number = int(input('Введите число: '))
# if is_prime(number):
#     print('Это простое число!')
# else:
#     print('Это не простое число!')

# После изменений:

def get_divisors(num):
    return sum([num % x == 0 for x in range(1, num + 1)])


number2 = int(input('Введите число: '))
if get_divisors(number2) == 2:
    print('Это простое число!')
else:
    print('Это не простое число!')