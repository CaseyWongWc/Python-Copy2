# 14.10 LAB: Count the digits (zyBooks 14.10.1)
# Function name: digit_count() -- non-negative int, returns # digits
# Hint: digit count +1 each time num // 10
# Ex: 345 -> 3

def digit_count(num):
    if num < 10:
        return 1
    return 1 + digit_count(num // 10)


if __name__ == "__main__":
    num = int(input())
    digit = digit_count(num)
    print(digit)
