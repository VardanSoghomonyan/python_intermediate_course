import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# the above triple for loop can be replaced by nditer iterator
for x in np.nditer(arr, flags=["buffered"], op_dtypes='S'):
    print("print matrix by creating temporary buffered matrix and setting the elements to String: ", x)

for x in np.nditer(arr[:, ::2]):
    print("print whole matrix by 2 steps movement: ", x)

# to get the elements' indexes use ndenumerate iterator
for x, idx in np.ndenumerate(arr):
    print("get element with index: ", x, idx)
