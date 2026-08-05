import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("Array: ", arr)
print("Ndim: ", arr.ndim)
print("Shape: ", arr.shape)

arr = arr.reshape(2, 3)
print("New Array:")
print(arr)

print("New Shape: ", arr.shape)

#O\P:
# Array:  [1 2 3 4 5 6]
# Ndim:  1
# Shape:  (6,)
# New Array:
# [[1 2 3]
#  [4 5 6]]
# New Shape:  (2, 3)
