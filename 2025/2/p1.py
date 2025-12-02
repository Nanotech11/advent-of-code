from itertools import chain

with open('input.txt', 'r', encoding='utf-8') as file:
    ranges = chain.from_iterable(
        range(int(s), int(e) + 1) for s, e in (group.split('-') for group in file.read().split(','))
    )

invalids = set()
for i in ranges:
    str_i = str(i)
    if str_i[: len(str_i) // 2] == str_i[len(str_i) // 2 :]:
        invalids.add(i)

print(sum(invalids))
