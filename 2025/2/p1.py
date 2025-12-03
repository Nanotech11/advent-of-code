from itertools import chain
import re

with open('input.txt', 'r', encoding='utf-8') as file:
    ranges = chain.from_iterable(
        range(int(s), int(e) + 1) for s, e in (group.split('-') for group in file.read().split(','))
    )

pattern = re.compile(r'^(\d+)\1$')
invalids = set()
for i in ranges:
    str_i = str(i)
    if pattern.match(str_i):
        invalids.add(i)

print(sum(invalids))
