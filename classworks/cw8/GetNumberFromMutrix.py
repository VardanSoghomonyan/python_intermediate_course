import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 72, 83, 94, 15]])

print("get first element of second array: ", arr[1, 0])
print("get range of 2 and 3 elements of second array: ", arr[1, 2:3])
print("get 2 index elements of two arrays: ", arr[0:2, 2])
print("get 4 index elements of first array: ", arr[0:1, 4])
print("get range of 1 and 4 elements of two arrays: ", arr[0:2, 1:4])
print("get first array: ", arr[0])

arr1 = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[5, 62, 73, 84, 95], [101, 102, 103, 104, 105]]])

print("get third element of second element of second array: ", arr1[1, 0, 2])
