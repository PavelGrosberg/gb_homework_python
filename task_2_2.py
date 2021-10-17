phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(phrase)-1:
    i += 1
    if phrase[i].isnumeric():
        phrase[i] = f'"{int(phrase[i]):02}"'
    if "+" in phrase[i]:
        phrase[i] = f'"{int(phrase[i]):+03}"'
print(' '.join(phrase))