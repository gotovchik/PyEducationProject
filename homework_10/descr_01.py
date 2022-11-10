class Size:
    def __set__(self, instance, value):
        if 0 > value:
            raise ValueError('Размер не может быть меньше 0 и больше 250')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Clothes:
    size = Size()
    height = Size()

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_fabric_quantity(self):
        coat = self.size / 6.5 + 0.5
        suit = 2 * self.height + 0.3
        value = coat + suit
        return [coat, suit, value]


fabric = Clothes(25, 1.87)
cloth = fabric.get_fabric_quantity()
print(f'Расход ткани на пальто = {cloth[0]}')
print(f'Расход ткани на костюм = {cloth[1]}')
print(f'Общий расход ткани = {cloth[2]}')
