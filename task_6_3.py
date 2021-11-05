from itertools import zip_longest
import json

users_text = '''Иванов,Иван,Иванович
Петров,Петр,Петрович'''
hobby_text = '''скалолазание,охота
горные лыжи'''

# with open('users.csv', 'w+', encoding='utf-8') as users_file:
#     users_file.write(users_text)
# with open('hobby.csv', 'w+', encoding='utf-8') as hobby_file:
#     hobby_file.write(hobby_text)

out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        num_lines_users = sum(1 for line in users)  #2
        num_lines_hobby = sum(1 for line in hobby)  #2
        if num_lines_users < num_lines_hobby:
            exit(1)
        users.seek(0)
        hobby.seek(0)
        for line_users, line_hobby in zip_longest(users, hobby):
            out_dict[line_users.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby
with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)
