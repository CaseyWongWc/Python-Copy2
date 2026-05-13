import numpy as np

# Create an array
my_array = np.array([ [1, 2], [3, 4] ])

# Delete the first row of array
new_array = np.delete(my_array, 0, axis=0)
print(new_array)

# Sort array
my_array.sort(axis=0)
print(my_array)
