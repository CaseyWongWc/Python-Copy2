import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Some common array operations

print("Adding arrays (array1 + array2)")
print(array1 + array2)

print("\nSubtracting arrays (array1 - array2)")
print(array1 - array2)

print("\nMultiplying arrays (array1 * array2)")
print(array1 * array2)

print("\nCalculating dot product of arrays")
print(np.dot(array1, array2))

print("\nFinding square root of each element in array1")
print(np.sqrt(array1))

print("\nFinding minimum element in array1")
print(array1.min())

print("\nFinding maximum element in array1")
print(array1.max())
