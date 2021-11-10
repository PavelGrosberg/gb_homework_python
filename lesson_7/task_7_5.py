import os
import json

files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files, key=lambda x: x[1])[1]

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = (0, [])

for file in files:
    num, ext_list = out_dict[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    out_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)

print(out_dict)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(out_dict, f_json)
