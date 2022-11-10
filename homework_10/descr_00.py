class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение не может быть отрицательным')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Road:
    length = NonNegative()
    width = NonNegative()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_mass(self, weight, depth):
        return self.length * self.width * weight * depth


obj = Road(5000, 20)
print(f'{obj.calc_mass(25, 0.05) / 1000} тонн')