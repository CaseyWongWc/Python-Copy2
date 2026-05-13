#h=s.get_handle()
def f(n):
    z=f"f({n})";z
    if n == 1:
        return 1
    return n * f(n - 1)
print(f(4))
