def pnp(num1, num2):
    print(num1, end=' ')
    if num1 < 0:
        return
    pnp(num1 - num2, num2)
    print(num1, end=' ')
pnp(12, 3)
