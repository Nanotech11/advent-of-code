import re
from itertools import chain, islice

with open(('input.txt', 'test2.txt')[1], 'r', encoding='utf-8') as file:
    bots: list[tuple] = []
    pattern = re.compile(r'^pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>,\sr=(?P<r>\d+)$')
    for line in file.readlines():
        if match := pattern.match(line):
            bots.append((int(match['x']), int(match['y']), int(match['z']), int(match['r'])))

delta_x, delta_y, delta_z = (min(val) for val in islice(zip(*bots), 3))
bots = [(x - delta_x, y - delta_y, z - delta_z, r) for x, y, z, r in bots]
max_dim = max(chain.from_iterable(islice(zip(*bots), 3)))

