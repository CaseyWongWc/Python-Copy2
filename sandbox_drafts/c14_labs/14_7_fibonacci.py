# 14.7 LAB: Fibonacci sequence (recursion) -- zyBooks 14.7.1
# fib(0)=0, fib(1)=1, fib(7)=13, fib(20)=6765
# negative input -> return -1

def fibonacci(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start_num = int(input())
    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")
