class Date:
    __data = {'day': 1, 'month': 1, 'year': 2000}
    __format_str = '{:s}{:02d}-{:02d}-{:d}'

    def __init__(self, str_date=None):
        if str_date:
            dt = Date.convert(str_date)
            if Date.is_valid(dt):
                self.__data = dt
            else:
                raise ValueError('Not valid date', str_date)

    @staticmethod
    def is_valid(data: dict):
        if not type(data) is dict:
            return False
        if not data.keys() == Date.__data.keys():
            return False
        if data['month'] < 1 or data['month'] > 12 or data['year'] < 0:
            return False
        leap = 1 if data['year'] % 4 == 0 else 0
        days = (31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if data['day'] < 1 or data['day'] > days[data['month'] - 1]:
            return False
        return True

    @classmethod
    def convert(cls, str_date):
        return {k: int(v) for k, v in zip(cls.__data.keys(), str_date.split('-'))}

    def __str__(self):
        return self.__format_str.format('', *self.__data.values())

    def __repr__(self):
        return self.__format_str.format('Date: ', *self.__data.values())


print(Date.is_valid({'day': 31, 'month': 13}))
print(Date.is_valid({'day': 16, 'month': 13, 'year': 2000}))
print(Date.is_valid({'day': 32, 'month': 12, 'year': 2000}))
print(Date.is_valid({'day': 29, 'month': 2, 'year': 2021}))
print(Date.is_valid({'day': 29, 'month': 2, 'year': 2020}))
print(Date.is_valid({'day': 31, 'month': 8, 'year': 2020}))

a = Date.convert('12-12-2020')
print(a)
print(Date.is_valid(a))

b = Date('12-11-2020')
print([b, b, b])
print(b)

c = Date('1-1-0')
print(c)

d = Date('32-11-2020')
print(d)
