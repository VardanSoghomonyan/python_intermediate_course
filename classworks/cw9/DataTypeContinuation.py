import numpy as np

arr = np.array([1.1, 2.1, 3.1, 4.1, 5.9, 0])

arr1 = arr.astype('i')
print(arr1)
print(arr1.dtype)

arr2 = arr.astype(int)
print(arr2)
print(arr2.dtype)

arr3 = arr.astype(bool)
print(arr3)
print(arr3.dtype)
