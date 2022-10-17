"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название)
и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'Запуск отрисовки'

    def draw(self):
        print(f'{self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} маркером')


pen = Pen()
pencil = Pencil()
handle = Handle()

for el in [pen, pencil, handle]:
    el.draw()

