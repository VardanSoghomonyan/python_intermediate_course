import numpy as np

arr = np.array([1.1, 2.1, 3.1, 4.1, 5.9, 0])
new = arr.copy()
new[0] = 17
print("Original Array is: ", arr)
print("Copied Array is: ", new)

new1 = arr.view()
print("Original Array before using view is: ", arr)

new1[0] = 20
print("Original Array is: ", arr)
print("Viewed Array is: ", new1)

# base is used to refer to the base array
print("Base Array for new COPIED is: ", new.base)
print("Base Array for new1 VIEWED is: ", new1.base)
