import sys
with open('bakery2.csv', 'w') as f:
    f.write('''5978,5
    8914,3
    7879,1
    1573,7
    ''')
idx, new_val = sys.argv[1:]
with open('bakery2.csv', 'r+') as f:
    temp_file = open('bakery2.tmp', 'w+')
    change = False
    for i, line in enumerate(f, 1):
        if i == int(idx):
            temp_file.write(f'{new_val}\n')
            change = True
        else:
            temp_file.write(line)
    if not change:
        exit('error')

    temp_file.seek(0)

    f.truncate(0)
    for line in temp_file:
        f.write(line)
    temp_file.close()
