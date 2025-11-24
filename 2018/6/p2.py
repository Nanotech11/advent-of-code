import numpy as np
# pylint: disable=C0103

with open('input.txt', 'r', encoding='utf-8') as file:
    points = np.array([(int(x), int(y)) for x, y in [line.split(',') for line in file.readlines()]])
xs, ys = points.T
xs -= xs.min()
ys -= ys.min()

count = 0

grid = np.zeros((xs.max() + 1, ys.max() + 1), dtype=np.int16)
for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        manhattan = abs(xs[0] - x) + abs(ys[0] - y)
        for idx, point in enumerate(points[1:], start=1):
            manhattan += abs(point[0] - x) + abs(point[1] - y)
        if manhattan < 10000:
            count += 1
        grid[x][y] = manhattan
print(grid.T)
print(count)
