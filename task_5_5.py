from time import perf_counter
from sys import getsizeof

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


start = perf_counter()
i = 0
src_1 = []
while i < len(src)-1:
    i += 1
    if src.count(src[i]) == 1:
        src_1.append(src[i])
print('Цикл while:')
print(src_1, getsizeof(src_1), perf_counter() - start, sep=" | ")


start = perf_counter()
src_2 = []
for x in src:
    if src.count(x) == 1:
        src_2.append(x)
print('Цикл for:')
print(src_2, getsizeof(src_2), perf_counter() - start, sep=" | ")


start = perf_counter()
result = [x for i, x in enumerate(src) if src.count(x) == 1]
print('Списковое включение:')
print(result, getsizeof(result), perf_counter() - start, sep=" | ")


start = perf_counter()
result = list(x for i, x in enumerate(src) if src.count(x) == 1)
print('Генератор:')
print(result, getsizeof(result), perf_counter() - start, sep=' | ')
