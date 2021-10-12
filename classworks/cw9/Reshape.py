import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# number of elements in the base array should be equal to the number of elements of the new array
# makes the array to 2X6 matrix
arr1 = arr.reshape(2, 6)
print("reshaped 2X6 matrix is: ", arr1)
print()

# makes the array to 2X3X2 matrix
arr2 = arr.reshape(2, 3, 2)
print("reshaped 2X3X2 matrix is: ", arr2)

# to call the base array after the reshape
arr3 = arr.reshape(2, 6)
print("the base of reshaped 2X6 matrix is: ", arr3)

# if you don't know the number of rows/columns you should put -1 amd system will define it itself
arr4 = arr.reshape(2, 2, -1)
print("the matrix of reshaped 2X2X? matrix is: ", arr4)

# if you want to make the array to 1 dimensional then argument of reshape should be -1
arr6 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print("the one dimensional array is: ", arr6.reshape(-1))
