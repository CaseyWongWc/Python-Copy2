numbers = [2, 4, 5, 8]
user_input = input()
while user_input != "end":
    try:
        num_val = int(user_input)
        if num_val < 0:
            # Possible IndexError if num_val is less than 0
            print(numbers[num_val])
        else:
            # Possible ZeroDivisionError
            print(20 // num_val)          # Truncates to an integer
    except ZeroDivisionError:
        print("r")
    except IndexError:
        print("s")
    user_input = input()
print("OK")
