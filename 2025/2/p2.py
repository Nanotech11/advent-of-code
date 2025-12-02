import re
from itertools import chain

with open('input.txt', 'r', encoding='utf-8') as file:
    ranges = chain.from_iterable(
        range(int(s), int(e) + 1) for s, e in (group.split('-') for group in file.read().split(','))
    )

invalids = set()
for i in ranges:
    str_i = str(i)
    for j in range(len(str_i) // 2):
        pattern = re.compile(rf'^({str_i[: j + 1]})+$')
        if match := pattern.match(str_i):
            invalids.add(i)
            break

print(sum(invalids))
