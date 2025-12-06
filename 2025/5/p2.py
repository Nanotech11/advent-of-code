from itertools import pairwise
with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    ranges: list[tuple[int, int]] = []
    max_end = 0
    while (line := file.readline().strip()) != '':
        s, e = line.split('-')
        max_end = max(max_end, int(e))
        ranges.append((int(s), int(e)))

ranges.sort()
ranges.append((max_end + 1, 0))
n_fresh_ids = 0
start = 0
end = 0
for range_pair in pairwise(ranges):
    if range_pair[0][1] >= range_pair[1][0]:
        end = max(end, range_pair[0][1], range_pair[1][1])
        if not start:
            start = range_pair[0][0]
    elif start:
        n_fresh_ids += end - start + 1
        start = 0
    else:
        n_fresh_ids += range_pair[0][1] - range_pair[0][0] + 1

print(n_fresh_ids)
