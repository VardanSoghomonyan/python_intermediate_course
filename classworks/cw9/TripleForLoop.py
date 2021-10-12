import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print("print matrix with one loop: ", x)

for x in arr:
    for y in x:
        for z in y:
            print("print matrix with two loops: ", z)

# the above triple for loop can be replaced by nditer iterator
for x in np.nditer(arr):
    print("print matrix with iterator: ", x)
