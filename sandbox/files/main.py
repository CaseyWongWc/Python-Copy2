def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return -1
    finally:
        print("Result is", result)

print(divide(4, 2))
print(divide(4, 0))
