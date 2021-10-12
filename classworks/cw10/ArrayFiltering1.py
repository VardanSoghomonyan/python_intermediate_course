import numpy as np

arr = np.array([41, 42, 43, 44])
filter_array = []

for element in arr:
    if element > 42:
        filter_array.append(True)
    else:
        filter_array.append(False)

print("Boolean values are: ", filter_array)
print("New array is: ", arr[filter_array])

# the above code can be written with this way
filter_array = arr > 42

print("Boolean values are: ", filter_array)
print("New array is: ", arr[filter_array])
