import re

import numpy as np

bots_list: list[tuple[int, int, int, int]] = []
pattern = re.compile(r'^pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>,\sr=(?P<r>\d+)$')
with open('input.txt', 'r', encoding='utf-8') as file:
# with open('test_input2.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if match := pattern.match(line):
            bots_list.append((int(match['x']), int(match['y']), int(match['z']), int(match['r'])))
bots = np.array(bots_list)

bots[:, 0] -= (delta_x := bots[:, 0].min())
bots[:, 1] -= (delta_y := bots[:, 1].min())
bots[:, 2] -= (delta_z := bots[:, 2].min())
max_dim = bots[:, :-1].max()
print(max_dim)
max_intersections = 0
max_intersection_points: list[tuple[int]] = []

for i in range(0, max_dim, 2048):
    x_indeces, y_indeces, z_indeces = np.indices((2048, 2048, 2048)) + i
    for bot in bots:
        # if bot[0]
        # manhattan = abs(x_indeces - point[]).sum()
        np.zeros((2048, 2048, 2048))
