import numpy as np

list1 = [15.5, 25.11, 19.0]
list2 = [12.2, 1.3, 6.38] 

# Create two 1-dimensional (1D) arrays
# with the elements of the above lists
array1 = np.array(list1)
array2 = np.array(list2)

# Concatenate two lists
print("Concatenation of list1 and list2 =", end=" ")
print(list1 + list2)
print()

# Sum two lists
print("Sum of list1 and list2 =", end=" ")
for i in range(len(list1)):
    print(list1[i] + list2[i], end=" ")  
print("\n")

# Sum two 1D arrays
print("Sum of array1 and array2 =", end=" ")
print(array1 + array2)  
