class ZeroDivEx(Exception):

    def __init__(self, *args):
        self.data = args

    def __str__(self):
        return ' '.join(map(str, self.args))



while True:
    user_input = input('Введите делитель, для деления 5: ')
    if not user_input:
        print('Делитель не определен')
        continue
    try:
        num = float(user_input)
    except Exception as err:
        print('Нужно ввести число!', err)
        continue
    try:
        if num == 0:
            raise ZeroDivEx('Попытка деления на 0!', 'Это так не работает!')
        else:
            print(f'Результат деления 5/{num}= {5/num}')
    except Exception as err:
        print(err)
