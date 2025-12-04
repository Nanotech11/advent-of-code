import numpy as np

with open(('input.txt', 'test.txt')[0], 'r', encoding='utf-8') as file:
    grid = np.array([list(line.strip()) for line in file])

total = 0
prev_total = -1
while total != prev_total:
    prev_total = total
    for row_i in range(grid.shape[0]):
        for col_i in range(grid.shape[1]):
            if grid[row_i, col_i] == '.':
                continue
            mask = np.zeros(grid.shape)
            mask[max(row_i-1, 0):min(row_i+2, grid.shape[0]), max(col_i-1, 0):min(col_i+2, grid.shape[1])] = 1
            surrounding = (grid[mask == 1] == '@').sum()
            if surrounding <= 4:
                grid[row_i, col_i] = '.'
                total += 1
print(total)
