class CellStorage:

    def __init__(self, count: int):
        if not type(count) is int:
            raise TypeError(f'Count должно быть натуральным числом, но получено {type(count)}')
        if count < 0:
            raise ValueError(f'Count должно быть больше или равно нулю, но получено {type(count)}')
        self.count = count

    @classmethod
    def __check_other(cls, other):
        if not type(other) is cls:
            raise TypeError(f'Поддерживается только {cls.__name__}, но получено {type(other)}')

    def __add__(self, other):
        self.__check_other(other)
        return CellStorage(self.count + other.count)

    def __sub__(self, other):
        self.__check_other(other)
        return CellStorage(self.count - other.count)

    def __mul__(self, other):
        self.__check_other(other)
        return CellStorage(self.count * other.count)

    def __truediv__(self, other):
        self.__check_other(other)
        return CellStorage(self.count//other.count)

    def make_order(self, cells_in_row):
        end = self.count + self.count // cells_in_row + 1
        return ''.join('\n' if not x % (cells_in_row + 1) else '*' for x in range(1, end))

    def __repr__(self):
        return f'CellStorage({self.count})'

storage = CellStorage(17)
st2 = CellStorage(2)
print(storage / st2)
print(storage - st2)
print(storage + st2)
print(storage * st2)
print(storage.make_order(5))
print('-'*17)
print(storage.make_order(7))
print('-'*17)
print(storage.make_order(17))
print('-' * 17)
