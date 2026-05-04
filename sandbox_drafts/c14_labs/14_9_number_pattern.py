# 14.9 LAB: Number pattern (zyBooks 14.9.1)
# Pattern continues one step past 0 into negative, then mirrors back.
# Ex: 12 3 -> 12 9 6 3 0 -3 0 3 6 9 12
# Ex: 8 2  -> 8 6 4 2 0 -2 0 2 4 6 8

def print_num_pattern(num1, num2):
    print(num1, end=' ')
    if num1 < 0:
        return
    print_num_pattern(num1 - num2, num2)
    print(num1, end=' ')


if __name__ == "__main__":
    user_num1 = int(input())
    user_num2 = int(input())
    print_num_pattern(user_num1, user_num2)
