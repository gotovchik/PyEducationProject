class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=MetaSingleton):
    pass


obj_0 = MyClass()
obj_1 = MyClass()
print(obj_0 is obj_1)
