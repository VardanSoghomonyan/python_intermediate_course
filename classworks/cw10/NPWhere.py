import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 6, 4])
arr1 = np.where(arr == 4)
print("arr1 is: ", arr1)

arr2 = np.where(arr % 2 == 0)
print("arr2 is: ", arr2)

x = np.searchsorted(arr, 6)
print(x)

x = np.searchsorted(arr, 0)
print(x)

# if you want to set it in the right side
x = np.searchsorted(arr, 6, side='right')
print(x)

print("sorted array is: ", np.sort(arr))

twoD = np.array([[3, 2, 1], [4, 15, 5]])
print("sorted 2D array is: ", np.sort(twoD))

