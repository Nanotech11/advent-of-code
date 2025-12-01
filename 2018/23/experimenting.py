import numpy as np

space = np.zeros((10, 10))
point = np.array((0, 0, 2))

# x_indices, y_indices = np.indices(space.shape)
# manhattan = abs(x_indices - point[0]) + abs(y_indices - point[1])

indeces = np.indices(space.shape)
manhattan = abs(indeces[1:] - point[:-1]).sum()

space[manhattan <= point[-1]] += 1
print(space.T)
