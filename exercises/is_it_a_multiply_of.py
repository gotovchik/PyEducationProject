# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.'


def is_it_mupliply_of(num):
    return ((num % 5 == 0 and num % 10 == 0) or (num % 15 == 0)) and not num % 30 == 0


a = int(input('Введите число:'))
print(is_it_mupliply_of(a))
