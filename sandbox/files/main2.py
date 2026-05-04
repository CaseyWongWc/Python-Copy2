def compute_nth_fib(num):
    # base cases
    if num == 0:
        return 0
    elif num == 1:
        return 1
    # recursive case
    else:
        return compute_nth_fib(num - 1) + compute_nth_fib(num - 2)

# User input and print
n = int(input())
print(compute_nth_fib(n))
