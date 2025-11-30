import numpy as np

space = np.zeros((10, 10))
point = np.array((3, 4, 2))

x_indices, y_indices = np.indices(space.shape, sparse=True)

manhattan = np.abs(x_indices - point[0]) + np.abs(y_indices - point[1])
space[manhattan <= point[-1]] += 1
print(space)
