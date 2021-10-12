import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# the 3 is the number of new split arrays
arr1 = np.array_split(arr, 3)
print("arr1 is: ", arr1)

# the 2 is the number of new split arrays
arr2 = np.array_split(arr, 2)
print("arr2 is: ", arr2)

arr3 = np.array_split(arr, 3, axis=1)
print("arr3 is: ", arr3)

# the 4 is the number of new split arrays
arr4 = np.array_split(arr, 4)
print("arr4 is: ", arr4)
print()
print("Now print the splitted arrays one by one")
print("The first splitted arrays is: ", arr4[0])
print("The second splitted arrays is: ", arr4[1])
print("The third splitted arrays is: ", arr4[2])
print("The fourth splitted arrays is: ", arr4[3])
