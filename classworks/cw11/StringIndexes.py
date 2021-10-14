import numpy as np

arr = np.arange(7) ** 2
print("arr is: ", arr)

print("arr[0] is: ", arr[0])

print("arr[-1] is: ", arr[-1])

print("arr[4:8] is: ", arr[4:8])

print("arr[:6], arr[6:] is: ", arr[:6], arr[6:])

print("arr[0:9:2]: ", arr[0:9:2])

print("arr[::3]: ", arr[::3])

print("arr[::-1]: ", arr[::-1])

arr[0:12:2] = -1
print(arr)
