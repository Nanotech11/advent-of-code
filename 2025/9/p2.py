from collections import defaultdict
from functools import cache
from itertools import combinations, cycle, pairwise
from operator import itemgetter

with open(('input.txt', 'test.txt', 'custom_test1.txt', 'custom_test2.txt')[0], 'r', encoding='utf-8') as file:
    points = [(int(x), int(y)) for x, y in (line.split(',') for line in file)]

points_dist = {
    ((min(p1[0], p2[0]), min(p1[1], p2[1])), (max(p1[0], p2[0]), max(p1[1], p2[1]))): (abs(p1[0] - p2[0]) + 1)
    * (abs(p1[1] - p2[1]) + 1)
    for p1, p2 in combinations(points, 2)
}
far_points = dict(sorted(points_dist.items(), key=itemgetter(1), reverse=True))

x_min, y_min = [min(val) for val in zip(*points)]
x_max, y_max = [max(val) for val in zip(*points)]

cycling_points = cycle(points)
sentinel_point = next(cycling_points)
v_walls = defaultdict(list)
h_walls = defaultdict(list)
for p1, p2 in pairwise(cycling_points):
    if p1[0] == p2[0]:
        v_walls[p1[0]].append((min((p1[1], p2[1])), max((p1[1], p2[1]))))
    elif p1[1] == p2[1]:
        h_walls[p1[1]].append((min((p1[0], p2[0])), max((p1[0], p2[0]))))
    if p1 == sentinel_point:
        break


@cache
def check_inside(p1: tuple, p2: tuple) -> bool:
    # print(f'inside checking {p1} to {p2}')
    collisions = 0
    y_check = p1[1] + 0.5
    for i in range(x_min - 1, p1[0] + 1):
        # print(i)
        if i in v_walls:
            # print(f'i is in v_wall: {v_walls[i]}. We are checking y={y_check}')
            for rng in v_walls[i]:
                if rng[0] <= y_check <= rng[1]:
                    # print('this is a collision')
                    collisions += 1
                else:
                    pass
                    # print('this is not a collision')
    # print(f'There are {collisions} collisions, returning {collisions % 2 != 0}')
    return collisions % 2 != 0


def h_partition(p1: tuple, p2: tuple) -> bool:
    for x in range(p1[0] + 1, p2[0]):
        if x in v_walls:
            for rng in v_walls[x]:
                if rng[0] <= p1[1] <= rng[1] or rng[0] <= p2[1] <= rng[1]:
                    return h_partition((x, p1[1]), p2) and v_partition(p1, (x, p2[1]))
    return check_inside(p1, p2)


def v_partition(p1: tuple, p2: tuple) -> bool:
    # print(f'v_partitioning {p1} to {p2}')
    for y in range(p1[1] + 1, p2[1]):
        if y in h_walls:
            for rng in h_walls[y]:
                if rng[0] <= p1[0] <= rng[1] or rng[0] <= p2[0] <= rng[1]:
                    return v_partition((p1[0], y), p2) and h_partition(p1, (p1[0], y))
    return check_inside(p1, p2)


for p1, p2 in far_points:
    # print(f'\n\nRECTANGLE: {p1} to {p2}, area: {far_points[(p1, p2)]}\n\n')
    if h_partition(p1, p2) and v_partition(p1, p2):
        print(p1, p2, f'area: {far_points[(p1, p2)]}')
        break
