import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
print(array[5])
two_dim = np.array([[1, 2, 3], [5, 6, 7]])
print(two_dim[1, 0])

# indexing of three-dimensional array
three_dim = np.array([[[1, 2], [3, 4]], [[5, 6], [2, 4]]])
print(three_dim[0, 1, 1])

