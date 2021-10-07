count = 1
while count < 6:
    count += 1
    duration = int(input('Вводим количество секунд:\n'))
    if duration < 0:
        print('Нет, это так не работает!')
    else:
        print('Получаем:')
    if 0 <= duration < 60:
        print(f'{duration} сек')
    if 60 <= duration < 3_600:
        print(f'{duration // 60} мин {duration % 60} сек')
    if 3_600 <= duration < 86_400:
        print(f'{duration // 3_600} час {duration % 3_600 // 60} мин {duration % 60} сек')
    if duration >= 86_400:
        print(f'{duration // 86_400} дн {duration % 86_400 // 3_600} ч {duration % 3_600 // 60} мин {duration % 60} сек')
print('\nОК')
