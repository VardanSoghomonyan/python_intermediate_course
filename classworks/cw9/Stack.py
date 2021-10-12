import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr1 = np.array([[[110, 120, 13], [14, 15, 16]], [[17, 18, 19], [20, 21, 22]]])

arr2 = np.stack((arr, arr1))
print("stacked array is: ", arr2)

# the above stack is equivalent to the below two lines, where axis=0 (default value)
arr2_1 = np.stack((arr, arr1), axis=0)
print("stacked array with axis 2_1 is: ", arr2_1)

arr3 = np.stack((arr, arr1), axis=1)
print("stacked array with axis 1 is: ", arr3)

arr4 = np.stack((arr, arr1), axis=2)
print("stacked array with axis 2 is: ", arr4)

arr5 = np.stack((arr, arr1), axis=3)
print("stacked array with axis 3 is: ", arr5)

# horizontal stack
arr6 = np.hstack((arr, arr1))
print("hstacked array is: ", arr6)

# vertical stack
arr7 = np.vstack((arr, arr1))
print("vstacked array is: ", arr7)

# depth stack
arr8 = np.dstack((arr, arr1))
print("dstacked array is: ", arr8)
