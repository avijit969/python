import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
# different size dimensional array
zero_dim = np.array(1233)
print(zero_dim)

one_dim = np.array([1, 2, 4, 8])
print(one_dim)

two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim)

three_dim = np.array([[[1, 2, 3], [2, 4, 7]], [[12, 4, 6], [12, 44, 98]]])
print(three_dim)

# finding dimension of array
print(two_dim.ndim)
# give an array any dimension you want
new_array = np.array(17, ndmin=5)
print(new_array)
