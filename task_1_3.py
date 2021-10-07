count = 1
while count < 11:
    count += 1
    percent = int(input('Введите процент:\n'))
    if percent <= 0 or percent > 100:
        print('Нет, это так не работает!')
    elif 10 < percent % 100 < 15:
        print(f'{percent} процентов')
    elif percent % 100 == 0:
        print(f'{percent} процентов')
    elif percent % 10 == 1:
        print(f'{percent} процент')
    elif 1 < percent % 10 < 5:
        print(f'{percent} процента')
    elif 4 < percent % 100 < 100:
        print(f'{percent} процентов')
print('\nOK')
