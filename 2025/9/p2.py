from collections import defaultdict
from itertools import combinations, cycle, pairwise
from operator import itemgetter

with open(
    (
        'input.txt',
        'test.txt',
        'M.txt',
        'Mr.txt',
        'M_.txt',
        'M_r.txt',
        '25_small.txt',
    )[0],
    'r',
    encoding='utf-8',
) as file:
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


def check_inside(point: tuple) -> bool:
    u_collisions = 0
    d_collisions = 0
    for i in range(x_min - 1, point[0] + 1):
        if i in v_walls:
            for rng in v_walls[i]:
                if rng[0] <= point[1] + 0.5 <= rng[1]:
                    d_collisions += 1
                if rng[0] <= point[1] - 0.5 <= rng[1]:
                    u_collisions += 1
    if u_collisions % 2 == 0 and d_collisions % 2 == 0:
        u_collisions = 0
        d_collisions = 0
        for i in range(point[0], x_max + 1):
            if i in v_walls:
                for rng in v_walls[i]:
                    if rng[0] <= point[1] + 0.5 <= rng[1]:
                        d_collisions += 1
                    if rng[0] <= point[1] - 0.5 <= rng[1]:
                        u_collisions += 1

    return u_collisions % 2 != 0 or d_collisions % 2 != 0


def check_gaps(p1: tuple, p2: tuple) -> bool:
    for x in (p1[0], p1[0] + 1, p2[0] - 1, p2[0]):
        in_v_wall = False
        in_valid_gap = False
        for y in range(p1[1], p2[1] + 1):
            if y in h_walls:
                if any((rng[0] <= x <= rng[1] for rng in h_walls[y])):
                    in_v_wall = False
                    in_valid_gap = False
                    continue
            if in_v_wall or in_valid_gap:
                continue
            if x in v_walls:
                if any((rng[0] <= y <= rng[1] for rng in v_walls[x])):
                    in_v_wall = True
                    continue
            if check_inside((x, y)):
                in_valid_gap = True
            else:
                return False
    for y in (p1[1], p1[1] + 1, p2[1] - 1, p2[1]):
        in_h_wall = False
        in_valid_gap = False
        for x in range(p1[0], p2[0] + 1):
            if x in v_walls:
                if any((rng[0] <= y <= rng[1] for rng in v_walls[x])):
                    in_h_wall = False
                    in_valid_gap = False
                    continue
            if in_h_wall or in_valid_gap:
                continue
            if y in h_walls:
                if any((rng[0] <= x <= rng[1] for rng in h_walls[y])):
                    in_h_wall = True
                    continue
            if check_inside((x, y)):
                in_valid_gap = True
            else:
                return False
    return True
    # if p2[0] - p1[0] < p2[1] - p1[1]:    
    #     for x in range(p1[0], p2[0] + 1):
    #         in_v_wall = False
    #         in_valid_gap = False
    #         for y in range(p1[1], p2[1] + 1):
    #             if y in h_walls:
    #                 if any((rng[0] <= x <= rng[1] for rng in h_walls[y])):
    #                     in_v_wall = False
    #                     in_valid_gap = False
    #                     continue
    #             if in_v_wall or in_valid_gap:
    #                 continue
    #             if x in v_walls:
    #                 if any((rng[0] <= y <= rng[1] for rng in v_walls[x])):
    #                     in_v_wall = True
    #                     continue
    #             if check_inside((x, y)):
    #                 in_valid_gap = True
    #             else:
    #                 return False
    # else:
    #     for y in range(p1[1], p2[1] + 1):
    #         in_h_wall = False
    #         in_valid_gap = False
    #         for x in range(p1[0], p2[0] + 1):
    #             if x in v_walls:
    #                 if any((rng[0] <= y <= rng[1] for rng in v_walls[x])):
    #                     in_h_wall = False
    #                     in_valid_gap = False
    #                     continue
    #             if in_h_wall or in_valid_gap:
    #                 continue
    #             if y in h_walls:
    #                 if any((rng[0] <= x <= rng[1] for rng in h_walls[y])):
    #                     in_h_wall = True
    #                     continue
    #             if check_inside((x, y)):
    #                 in_valid_gap = True
    #             else:
    #                 return False
    return True


for p1, p2 in far_points:
    if not check_gaps(p1, p2):
        continue
    print(p1, p2)
    print(points_dist[(p1, p2)])
    break

