# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# o 6 -> да
# o 7 -> да
# o 1 -> нет

def weekend(n):
    if 1 <= n <= 7:
        if n == 6 or n == 7:
            print('Да')
        else:
            print('Нет')
    else:
        print('Введен не правильный номер дня!')


day = int(input('Введите номер дня недели:'))
weekend(day)
day = int(input('Введите номер дня недели:'))
weekend(day)
