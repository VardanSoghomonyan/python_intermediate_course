import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# get appropriate elements by given indexes
print("from 1 index to the 3 index: ", arr[1:3])
print("from the beginning to the 4 index: ", arr[:4])
print("from 2 index to the end: ", arr[2:])
print("from -2 index to the end: ", arr[-2:])
print("from the beginning to the -3 index: ", arr[:-3])
print("gets nothing", arr[-1:-3])
print("from -3 index to the -1 index: ", arr[-3:-1])
print("gets elements between first and forth elements with 2 steps: ", arr[0:3:2])
print("gets elements from array with 2 steps: ", arr[::2])
print("gets elements from array with 1 steps from the end: ", arr[::-1])
