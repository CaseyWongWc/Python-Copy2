value_list = [4.2, 4.1, 3.0, 3.6, 9.6, 0.1, 6.2, 7.9, 2.5, 0.7]

try:
    list_index = int(input())
    print(f"value = {value_list[list_index]}")
except ValueError:
    print("int(): An integer is expected.")
except IndexError:
    print("Index is out of range.")
