from itertools import combinations, pairwise
from operator import itemgetter

with open(('input.txt', 'test.txt')[1], 'r', encoding='utf-8') as file:
    points = [(int(x), int(y)) for x, y in (line.split(',') for line in file)]

points_dist = {
    ((min(p1[0], p2[0]), min(p1[1], p2[1])), (max(p1[0], p2[0]), max(p1[1], p2[1]))): (abs(p1[0] - p2[0]) + 1)
    * (abs(p1[1] - p2[1]) + 1)
    for p1, p2 in combinations(points, 2)
}
far_points = dict(sorted(points_dist.items(), key=itemgetter(1), reverse=True))

x_min, y_min = [min(val) for val in zip(*points)]
x_max, y_max = [max(val) for val in zip(*points)]

x_walls: dict[int, set[int]] = {}
y_walls: dict[int, set[int]] = {}
points.append(points[0])
for p1, p2 in pairwise(points):
    if p1[0] != p2[0]:
        if p1[1] in y_walls:
            y_walls[p1[1]].update(range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1))
        else:
            y_walls[p1[1]] = {*list(range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1))}
    else:
        if p1[0] in x_walls:
            x_walls[p1[0]].update(range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1))
        else:
            x_walls[p1[0]] = {*list(range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1))}

for p1, p2 in far_points:
    failed = False
    hit_x_wall = False
    hit_y_wall = False
    for x in range(p1[0] + 1, p2[0]):
        if x in x_walls:
            if p1[1] in x_walls[x] or p2[1] in x_walls[x]:
                hit_x_wall = x
                break
    if hit_x_wall:

    if failed:
        continue
    for y in range(p1[1] + 1, p2[1]):
        if y in y_walls:
            if p1[0] in y_walls[y] or p2[0] in y_walls[y]:
                hit_y_wall = True
                break
    if hit_y_wall:
        pass
    if failed:
        continue
    print((p1, p2), far_points[(p1, p2)])
    break
