import re

import numpy as np

bots_list: list[tuple[int, int, int, int]] = []
pattern = re.compile(r"^pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>,\sr=(?P<r>\d+)$")
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        if match := pattern.match(line):
            bots_list.append((int(match['x']), int(match['y']), int(match['z']), int(match['r'])))
bots = np.array(bots_list, dtype=np.int64)

max_r_bot_i = bots[:, -1].argmax()
max_r = bots[:, -1].max()
bots[:, 0] -= bots[max_r_bot_i][0]
bots[:, 1] -= bots[max_r_bot_i][1]
bots[:, 2] -= bots[max_r_bot_i][2]

in_r_bots = bots[np.abs(bots[:, :-1]).sum(axis=1) <= max_r]
print(len(in_r_bots))
