class Codewars:
    def array_diff(self, b):    # Исключение из основного списка всех элементов из второго
        return [x for x in self if x not in b]

