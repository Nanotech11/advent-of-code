import re

import numpy as np

bots_list: list[tuple[int, int, int, int]] = []
pattern = re.compile(r'^pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>,\sr=(?P<r>\d+)$')
with open('input.txt', 'r', encoding='utf-8') as file:
# with open('test_input2.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if match := pattern.match(line):
            bots_list.append((int(match['x']), int(match['y']), int(match['z']), int(match['r'])))
bots = np.array(bots_list, dtype=np.int32)

max_intersections = 0
max_intersection_points = []
for bot in bots:
    for i in range(bot[-1] + 1):
        print('2nd loop')
        xs = (bot[0] - i, bot[0] + i)
        extra = bot[-1] - i
        for j in range(extra):
            ys = (bot[1] - j, bot[1] + j)
            zs = (bot[2] - (extra - j), bot[2] + (extra - j))
            for x in xs:
                for y in ys:
                    for z in zs:
                        intersection_count = 0
                        for comp_bot in bots:
                            # 7 layers deep btw. Super efficient code :D
                            if abs(x - comp_bot[0]) + abs(y - comp_bot[1]) + abs(z - comp_bot[2]) <= comp_bot[-1]:
                                intersection_count += 1
                        if intersection_count > max_intersections:
                            max_intersections = intersection_count
                            max_intersection_points = [(x, y, z)]
                        elif intersection_count == max_intersections:
                            max_intersection_points.append((x, y, z))

print(max_intersections)
print(max_intersection_points)
