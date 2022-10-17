"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет)
и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self, i=3):
        while i != 0:
            if self.__color == 'red':
                print(self.__color)
                sleep(7)
                self.__color = 'yellow'
                i -= 1
            elif self.__color == 'yellow':
                print(self.__color)
                sleep(2)
                self.__color = 'green'
                i -= 1
            elif self.__color == 'green':
                print(self.__color)
                sleep(5)
                self.__color = 'red'
                i -= 1


light = TrafficLight()
light.running(5)
