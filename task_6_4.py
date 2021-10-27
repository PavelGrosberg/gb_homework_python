from itertools import zip_longest
with open('task4.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
            num_lines_users = sum(1 for line in users)  #2
            num_lines_hobby = sum(1 for line in hobby)  #2
            if num_lines_users < num_lines_hobby:
                exit(1)
            users.seek(0)
            hobby.seek(0)
            for line_users, line_hobby in zip_longest(users, hobby):
                f.write(f'{line_users.strip()}: {line_hobby.strip() if line_hobby is not None else line_hobby}\n')
