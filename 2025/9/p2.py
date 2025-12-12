from itertools import combinations, cycle, pairwise
from operator import itemgetter

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    points = [(int(x), int(y)) for x, y in (line.split(',') for line in file)]

points_dist = {
    ((min(p1[0], p2[0]), min(p1[1], p2[1])), (max(p1[0], p2[0]), max(p1[1], p2[1]))): (abs(p1[0] - p2[0]) + 1)
    * (abs(p1[1] - p2[1]) + 1)
    for p1, p2 in combinations(points, 2)
}
far_points = dict(sorted(points_dist.items(), key=itemgetter(1), reverse=True))

x_min, y_min = [min(val) for val in zip(*points)]
x_max, y_max = [max(val) for val in zip(*points)]

