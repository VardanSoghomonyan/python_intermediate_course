import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr1 = np.array([[[110, 120, 13], [14, 15, 16]], [[17, 18, 19], [20, 21, 22]]])

arr2 = np.concatenate((arr, arr1))
print("concatenated array is: ", arr2)

# the above concat is equivalent to the below two lines, where axis=0 (default value)
arr2_1 = np.concatenate((arr, arr1), axis=0)
print("concatenated array with axis 2_1 is: ", arr2_1)

arr3 = np.concatenate((arr, arr1), axis=1)
print("concatenated array with axis 1 is: ", arr3)

arr4 = np.concatenate((arr, arr1), axis=2)
print("concatenated array with axis 2 is: ", arr4)
