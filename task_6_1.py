import re

file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
content = file_1.read()
response = re.split(' - - | "|-"|"| HTTP/1.1" |\n', content)
response = tuple(zip(*[iter(response)] * 8))
result = []
for i in range(0, len(response)):
    result.append((f'{response[i][0]}', f'{response[i][2]}'))
print(result)
