from itertools import combinations, cycle, pairwise
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

x_walls: dict[int, set] = {}
y_walls: dict[int, set] = {}
for point in points:
    x_walls[point[0]] = set() # type: ignore
    y_walls[point[1]] = set() # type: ignore
out_dir = ''
travel_dir = ''
sentinel_point = ()
looping_points = pairwise(cycle(points))
for p1, p2 in looping_points:
    if p1[0] == p2[0] == x_min:
        sentinel_point = p1
        out_dir = 'L'
        if p1[1] < p2[1]:
            travel_dir = 'D'
        else:
            travel_dir = 'U'
        break
    if p1[0] == p2[0] == x_max:
        sentinel_point = p1
        out_dir = 'R'
        if p1[1] < p2[1]:
            travel_dir = 'D'
        else:
            travel_dir = 'U'
    if p1[1] == p2[1] == y_min:
        sentinel_point = p1
        out_dir = 'U'
        if p1[0] < p2[0]:
            travel_dir = 'R'
        else:
            travel_dir = 'L'
        break
    if p1[1] == p2[1] == y_max:
        sentinel_point = p1
        out_dir = 'D'
        if p1[1] < p2[1]:
            travel_dir = 'R'
        else:
            travel_dir = 'L'
        break

print(sentinel_point)

for p1, p2 in looping_points:
    if p1 == sentinel_point:
        break
    if p1[0] < p2[0]:
        if out_dir == 'R':
            y_walls[p1[1]].update(range(p1[0] + 1, p2[0]))
            if travel_dir == 'U':
                out_dir = 'D'
            elif travel_dir == 'D':
                out_dir = 'U'
        elif out_dir == 'L':
            y_walls[p1[1]].update(range(p1[0], p2[0]))
            if travel_dir == 'U':
                out_dir = 'U'
            elif travel_dir == 'D':
                out_dir = 'D'
        travel_dir = 'R'
    elif p1[0] > p2[0]:
        if out_dir == 'R':
            y_walls[p1[1]].update(range(p2[0] + 1, p1[0] + 1))
            if travel_dir == 'U':
                out_dir = 'U'
            elif travel_dir == 'D':
                out_dir = 'D'
        elif out_dir == 'L':
            y_walls[p1[1]].update(range(p2[0] + 1, p1[0]))
            if travel_dir == 'U':
                out_dir = 'D'
            elif travel_dir == 'D':
                out_dir = 'U'
        travel_dir = 'L'
    elif p1[1] < p2[1]:
        if out_dir == 'U':
            x_walls[p1[0]].update(range(p1[1], p2[1]))
            if travel_dir == 'R':
                out_dir = 'R'
            elif travel_dir == 'L':
                out_dir = 'L'
        elif out_dir == 'D':
            x_walls[p1[0]].update(range(p1[1] + 1, p2[1]))
            if travel_dir == 'R':
                out_dir = 'L'
            elif travel_dir == 'L':
                out_dir = 'R'
        travel_dir = 'D'
    else:
        if out_dir == 'U':
            x_walls[p1[0]].update(range(p2[1]+1, p1[1]))
            if travel_dir == 'R':
                out_dir = 'L'
            elif travel_dir == 'L':
                out_dir = 'R'
        elif out_dir == 'D':
            x_walls[p1[0]].update(range(p2[1]+1, p1[1]+1))
            if travel_dir == 'R':
                out_dir = 'R'
            elif travel_dir == 'L':
                out_dir = 'L'
        travel_dir = 'U'

looping_points = pairwise(cycle(reversed(points)))
for p1, p2 in looping_points:
    if p1[0] == p2[0] == x_min:
        sentinel_point = p1
        out_dir = 'L'
        if p1[1] < p2[1]:
            travel_dir = 'D'
        else:
            travel_dir = 'U'
        break
    if p1[0] == p2[0] == x_max:
        sentinel_point = p1
        out_dir = 'R'
        if p1[1] < p2[1]:
            travel_dir = 'D'
        else:
            travel_dir = 'U'
        break
    if p1[1] == p2[1] == y_min:
        sentinel_point = p1
        out_dir = 'U'
        if p1[0] < p2[0]:
            travel_dir = 'R'
        else:
            travel_dir = 'L'
        break
    if p1[1] == p2[1] == y_max:
        sentinel_point = p1
        out_dir = 'D'
        if p1[1] < p2[1]:
            travel_dir = 'R'
        else:
            travel_dir = 'L'
        break

print(sentinel_point)

for p1, p2 in looping_points:
    if p1 == sentinel_point:
        break
    if p1[0] < p2[0]:
        if out_dir == 'R':
            y_walls[p1[1]].update(range(p1[0] + 1, p2[0]))
            if travel_dir == 'U':
                out_dir = 'D'
            elif travel_dir == 'D':
                out_dir = 'U'
        elif out_dir == 'L':
            y_walls[p1[1]].update(range(p1[0], p2[0]))
            if travel_dir == 'U':
                out_dir = 'U'
            elif travel_dir == 'D':
                out_dir = 'D'
        travel_dir = 'R'
    elif p1[0] > p2[0]:
        if out_dir == 'R':
            y_walls[p1[1]].update(range(p2[0] + 1, p1[0] + 1))
            if travel_dir == 'U':
                out_dir = 'U'
            elif travel_dir == 'D':
                out_dir = 'D'
        elif out_dir == 'L':
            y_walls[p1[1]].update(range(p2[0] + 1, p1[0]))
            if travel_dir == 'U':
                out_dir = 'D'
            elif travel_dir == 'D':
                out_dir = 'U'
        travel_dir = 'L'
    elif p1[1] < p2[1]:
        if out_dir == 'U':
            x_walls[p1[0]].update(range(p1[1], p2[1]))
            if travel_dir == 'R':
                out_dir = 'R'
            elif travel_dir == 'L':
                out_dir = 'L'
        elif out_dir == 'D':
            x_walls[p1[0]].update(range(p1[1] + 1, p2[1]))
            if travel_dir == 'R':
                out_dir = 'L'
            elif travel_dir == 'L':
                out_dir = 'R'
        travel_dir = 'D'
    else:
        if out_dir == 'U':
            x_walls[p1[0]].update(range(p2[1]+1, p1[1]))
            if travel_dir == 'R':
                out_dir = 'L'
            elif travel_dir == 'L':
                out_dir = 'R'
        elif out_dir == 'D':
            x_walls[p1[0]].update(range(p2[1]+1, p1[1]+1))
            if travel_dir == 'R':
                out_dir = 'R'
            elif travel_dir == 'L':
                out_dir = 'L'
        travel_dir = 'U'

print(x_walls)
print(y_walls)

for p1, p2 in far_points:
    failed = False
    p = False
    if p2 == (9, 7):
        p = True
    for x in range(p1[0] + 1, p2[0]):
        if p:
            print(x, x in x_walls)
        if x in x_walls:
            if p1[1] in x_walls[x] or p2[1] in x_walls[x]:
                failed = True
                break
    if failed:
        continue
    for y in range(p1[1] + 1, p2[1]):
        if p:
            print(y, y in y_walls)
        if y in y_walls:
            if p1[0] in y_walls[y] or p2[0] in y_walls[y]:
                failed = True
                break
    if failed:
        continue
    print((p1, p2), far_points[(p1, p2)])
    break
