import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print("print matrix with one loop: ", x)

for x in arr:
    for y in x:
        print("print matrix with two loops: ", y)

# the above double for loop can be replaced by nditer iterator
for x in np.nditer(arr):
    print("print matrix with iterator: ", x)
