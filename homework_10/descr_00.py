class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение не может быть отрицательным')
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


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