import numpy as np

with open('input.txt', 'r', encoding='utf-8') as file:
    points = np.array([(int(x), int(y)) for x, y in [line.split(',') for line in file.readlines()]])
xs, ys = points.T
xs -= xs.min()
ys -= ys.min()
bounds = (xs.min(), xs.max() + 1, ys.min(), ys.max() + 1)

counts = np.zeros((len(points)), dtype=np.int16)
unboundeds = np.zeros((len(points)), dtype=np.int16)

grid = np.zeros((xs.max() + 1, ys.max() + 1), dtype=np.int16)
for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        manhattan = abs(xs[0] - x) + abs(ys[0] - y)
        for idx, point in enumerate(points[1:], start=1):
            if manhattan == 0:
                break
            if (val := abs(point[0] - x) + abs(point[1] - y)) <= manhattan:
                if val == manhattan:
                    grid[x][y] = -1
                else:
                    grid[x][y] = idx
                    manhattan = val
        if grid[x][y] != -1:
            counts[grid[x][y]] += 1
        if x in bounds or y in bounds:
            unboundeds[grid[x][y]] = 1

bounded_counts = counts.copy()
bounded_counts[unboundeds == 1] = 0
highest = bounded_counts.max()
highest_idx = bounded_counts.argmax()

print(grid.T)
print(counts)
print(bounded_counts)
print(f'{highest} @ {highest_idx}')
