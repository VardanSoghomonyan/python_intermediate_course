import numpy as np

# set arrays minimum dimension by ndmin
arr = np.array([1, 2, 3, 4, 5], ndmin=5)
# ndim gets the dimension of array
print("number of dimensions: ", arr.ndim)
