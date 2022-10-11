"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
"""

# Было без LC

# def get_digits(num):
#     col = []
#     for ch in str(num):
#         if ch.isdigit():
#             col.append(int(ch))
#     return col
# digits = get_digits(number)

number = float(input('Enter the real number: '))

# Стало
digits = [int(i) for i in str(number) if i.isdigit()]
print(f'The amount of the digits of the number is {sum(digits)}')