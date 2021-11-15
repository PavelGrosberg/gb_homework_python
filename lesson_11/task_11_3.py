class NumbersOnly(Exception):

    def __init__(self, *args):
        self.txt = ' '.join(str(x) for x in args)

    def __str__(self):
        return self.txt


class CheckedList:
    _exception = NumbersOnly('Только числа!')
    __list = []
    supported_types = (int, float)

    def append(self, data):
        t = type(data)
        if t in self.supported_types:
            self.__list.append(data)
            return
        elif t == str:
            for f in self.supported_types:
                try:
                    num = f(data)
                except ValueError:
                    continue
                else:
                    self.__list.append(num)
                    return

        raise self._exception

    @property
    def numbers_list(self):
        return self.__list

    def __str__(self):
        return str(self.numbers_list).strip('[]')


cl = CheckedList()
while True:
    user_input = input("Введите число: ")
    if user_input == 'stop':
        break
    try:
        cl.append(user_input)
    except NumbersOnly as err:
        print(f'Ошибка ввода: {err}')
print(f'Результат ввода: {cl}')
