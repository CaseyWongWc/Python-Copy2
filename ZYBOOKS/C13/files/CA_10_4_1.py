def get_column():
    column = input()
    if (column < "a") or (column > "h"):
        raise ValueError("Column must be between a and h")
    return column

def get_row():
    row = int(input())
    if (row < 1) or (row > 8):
        raise ValueError("Row must be between 1 and 8")
    return row

try:
    column = get_column()
    row = get_row()

    print(f"Move to square {column}{row}")

except ValueError as excpt:
    print(excpt)
