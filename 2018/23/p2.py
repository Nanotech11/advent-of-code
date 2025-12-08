import re
from collections import defaultdict
from collections.abc import Generator
from functools import cache
from itertools import combinations, product, takewhile
from operator import itemgetter


@cache
def get_perimeter_points(radius: int) -> Generator[tuple[int, int, int]]:
    for xd in range(radius + 1):
        extra = radius - xd
        for yd in range(extra + 1):
            zd = radius - xd - yd
            yield (xd, yd, zd)


with open(('input.txt', 'test2.txt')[0], 'r', encoding='utf-8') as file:
    bots: list[tuple] = []
    pattern = re.compile(r'^pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>,\sr=(?P<r>\d+)$')
    for line in file.readlines():
        if match := pattern.match(line):
            bots.append((int(match['x']), int(match['y']), int(match['z']), int(match['r'])))

x_min = min((point[0] for point in bots))
y_min = min((point[1] for point in bots))
z_min = min((point[2] for point in bots))
x_max = max((point[0] for point in bots))
y_max = max((point[1] for point in bots))
z_max = max((point[2] for point in bots))

n_intersect_bots_dict: dict[tuple, int] = defaultdict(lambda: 0)
for bot1, bot2 in combinations(bots, 2):
    manhattan = abs(bot1[0] - bot2[0]) + abs(bot1[1] - bot2[1]) + abs(bot1[2] - bot2[2])
    if manhattan <= bot1[3] + bot2[3]:
        n_intersect_bots_dict[bot1] += 1
        n_intersect_bots_dict[bot2] += 1
n_intersect_bots = dict(sorted(n_intersect_bots_dict.items(), key=itemgetter(1), reverse=True))

max_intersections = 0
for bot1 in takewhile(lambda x: n_intersect_bots_dict[x] >= max_intersections, n_intersect_bots):
    x, y, z, r = bot1
    perimeter_points = (
        point
        for point in product(range(r + 1), repeat=3)
        if x_min <= point[0] <= x_max and y_min <= point[1] <= y_max and z_min <= point[2] <= z_max and sum(point) == r
    )

    for point in perimeter_points:
        print(point)
        # for bot2 in bots:
        #     if
