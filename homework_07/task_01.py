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
    __color: str = ''

    @staticmethod
    def running(__color: str = 'red', i: int = 3):
        while i != 0:
            if __color == 'red':
                print(__color)
                sleep(7)
                __color = 'yellow'
                i -= 1
            elif __color == 'yellow':
                print(__color)
                sleep(2)
                __color = 'green'
                i -= 1
            elif __color == 'green':
                print(__color)
                sleep(5)
                __color = 'red'
                i -= 1
        return __color


light = TrafficLight()
COLOR = 'red'
CYCLE = 10
light.running(COLOR, CYCLE)
