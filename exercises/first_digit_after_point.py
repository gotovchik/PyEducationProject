#4.	Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# o	6,78 -> 7
# o	5 -> нет
# o	0,34 -> 3
# 5.	Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a = float(input('Введите число:'))
b = int((a * 10) % 10)
print(b)



