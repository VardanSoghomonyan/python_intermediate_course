import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("get data type of arr: ", arr.dtype)

arr1 = np.array(["1", "2", "3", "4", "5", "apple"])

# prints with unicode item length
print("get data type of arr1: ", arr1.dtype)

arr2 = np.array(['1', '2', '3', '4', 'apple', 7])

# prints with unicode item length
print("get data type of arr2: ", arr2.dtype)

arr3 = np.array([1, 2, 3, 4, 5], dtype='S')

# prints bite size of item
print("get arr3: ", arr3)
print("get data type of arr3: ", arr3.dtype)

# creates 4 bite integers with i4
arr4 = np.array([1, 2, 3, 4, 5], dtype='i4')

print("get arr4: ", arr4)
print("get data type of arr4: ", arr4.dtype)

# creates 2 bite integers with i2
arr5 = np.array([1, 2, 3, 4, 5], dtype='i2')

print("get arr5: ", arr5)
print("get data type of arr5: ", arr5.dtype)
