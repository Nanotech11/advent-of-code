from itertools import pairwise

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    ranges = sorted(((int(s), int(e)) for s, e in (line.split('-') for line in iter(file.readline, '\n'))))

ranges.append((ranges[-1][1] + 1, 0))
n_fresh_ids = 0
start = None
end = 0
for range_1, range_2 in pairwise(ranges):
    if range_1[1] >= range_2[0]:
        end = max(end, range_1[1], range_2[1])
        if start is None:
            start = range_1[0]
    elif start is not None:
        n_fresh_ids += end - start + 1
        start = None
    else:
        n_fresh_ids += range_1[1] - range_1[0] + 1

print(n_fresh_ids)
