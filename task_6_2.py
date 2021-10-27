import re
from collections import Counter

file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
content = file_1.read()
response = re.split(' - - | "|-"|"| HTTP/1.1" |\n', content)
response = tuple(zip(*[iter(response)] * 8))
result = []
for i in range(0, len(response)):
    result.append((f'{response[i][0]}', f'{response[i][2]}'))
print(result)
dct = {}
for i in range(0, len(result)):
    dct.setdefault(i, result[i][0])
values = dct.values()
counts = Counter(values)
max_val = max(counts.values())
spammer_ip = {k: v for k, v in counts.items() if v == max_val}
print(f' Спамер: {spammer_ip}')
