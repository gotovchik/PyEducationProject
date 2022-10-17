"""
Задание 4.
Реализуйте базовый класс Car.
У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, speed, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} движется со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60 and not self.is_police:
            print(f'{self.color} {self.name} превышает скорость')
        else:
            print(f'{self.color} {self.name}'
                  f' движется со скоростью {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40 and not self.is_police:
            print(f'{self.color} {self.name} превышает скорость')
        else:
            print(f'{self.color} {self.name}'
                  f' движется со скоростью {self.speed}')


class PoliceCar(Car):
    pass


sport = SportCar('Lamborghini', 'Red', 260, 0)
sport.go()
sport.turn('налево')
sport.show_speed()
sport.stop

police = PoliceCar('Ford', 'Black and White', 120, 1)
police.go()
police.turn('направо')
police.show_speed()
police.stop()

work = WorkCar('Caterpillar', 'Yellow', 55, 0)
work.go()
work.show_speed()
work.stop()

town = TownCar('Toyota', 'White', 80, 0)
town.go()
town.turn('налево')
town.turn('направо')
town.show_speed()
town.stop()
