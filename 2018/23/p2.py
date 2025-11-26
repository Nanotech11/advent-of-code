import re

import numpy as np

bots_list: list[tuple[int, int, int, int]] = []
pattern = re.compile(r'^pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>,\sr=(?P<r>\d+)$')
# with open('input.txt', 'r', encoding='utf-8') as file:
with open('test_input2.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if match := pattern.match(line):
            bots_list.append((int(match['x']), int(match['y']), int(match['z']), int(match['r'])))
bots = np.array(bots_list, dtype=np.int64)

bots[:, 0] -= (delta_x := bots[:, 0].min())
bots[:, 1] -= (delta_y := bots[:, 1].min())
bots[:, 2] -= (delta_z := bots[:, 2].min())
x_max = bots[:, 0]
y_max = bots[:, 1]
z_max = bots[:, 2]

space = np.zeros((x_max + 1, y_max + 1, z_max + 1))


