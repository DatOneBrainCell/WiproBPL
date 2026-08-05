import numpy as np
arr = np.random.randint(1, 100, 9).reshape(3, 3)

print("Array:")
print(arr)

print("Ndim: ", arr.ndim)
print("Shape: ", arr.shape)
print("Sliced Values: ", arr[1, 0:2])

#O\P:
# Array:
# [[ 6 95 11]
#  [81  1 97]
#  [28 16 22]]
# Ndim:  2
# Shape:  (3, 3)
# Sliced Values:  [81  1]
