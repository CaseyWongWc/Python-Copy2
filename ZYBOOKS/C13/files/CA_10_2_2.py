import math

try:
    x_value = float(input())
    print(f"20 raised to the power of {x_value} is {math.pow(20, x_value)}")
except ValueError:
    print("float(): Input is not a float.")
except OverflowError:
    print(f"math.pow(): result of 20 raised to the power of {x_value} is too large.")
