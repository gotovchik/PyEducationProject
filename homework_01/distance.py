# 10. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D/3D пространстве.
# Пример:
# o A (3,6); B (2,1) -> 5,09
# o A (7,-5); B (1,-1) -> 7,21
from math import sqrt


def distance_2d(xa, ya, xb, yb):
    return round(sqrt((xb - xa) ** 2 + (yb - ya) ** 2), 2)


def distance_3d(xa, ya, za, xb, yb, zb):
    return round(sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (za - zb) ** 2), 2)


print(distance_2d(3, 5, 6, 2))
print(distance_3d(4, 2, 3, 6, 3, 1))
