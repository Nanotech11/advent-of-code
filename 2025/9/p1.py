from itertools import combinations
from operator import itemgetter


with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    points = [(int(x), int(y)) for x, y in (line.split(',') for line in file)]

points_dist = {(p1, p2): (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1) for p1, p2 in combinations(points, 2)}
far_points = dict(sorted(points_dist.items(), key=itemgetter(1), reverse=True))

print(list(far_points.items())[0])
