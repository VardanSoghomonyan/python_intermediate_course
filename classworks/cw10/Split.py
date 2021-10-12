import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr1 = np.array_split(arr, 3)
print("arr1 is: ", arr1)

arr2 = np.array_split(arr, 2)
print("arr2 is: ", arr2)

arr3 = np.array_split(arr, 3, axis=1)
print("arr3 is: ", arr3)
