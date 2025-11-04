# INTRODUCTION OF NUMPY 💀

import numpy as np

# Array banana
arr = np.array([10, 20, 30, 40])
print("Original Array:", arr)

# Shape and size
print("Shape:", arr.shape)
print("Size:", arr.size)

# 2D Array
matrix = np.array([[1, 2], [3, 4]])
print("\n2D Matrix:\n", matrix)

# Element-wise operations
print("Array * 2:", arr * 2)
print("Array + 5:", arr + 5)

# Slicing
print("Sliced Array:", arr[1:3])

# Random numbers
rand = np.random.randint(100, 1000, size=(3, 3))
print("\nRandom 3x3 Matrix:\n", rand)
