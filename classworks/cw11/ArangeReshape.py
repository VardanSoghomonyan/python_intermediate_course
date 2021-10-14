import numpy as np

arr = np.arange(81).reshape(3, 3, 3, 3)
print("arr1 is: ", arr)

# if ... is written, it means all before the specified values
print("arr[...,1,1,1,1]: ", arr[..., 1, 1, 1, 1])
print("arr[...,1,1,1]: ", arr[..., 1, 1, 1])
print("arr[...,1,1]: ", arr[..., 1, 1])
print("arr[...,1]: ", arr[..., 1])

# if : is written, it means all after the specified values
print("arr[..., 1,1,:]: ", arr[..., 1, 1, :])
