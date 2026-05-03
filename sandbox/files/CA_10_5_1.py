def pick():
    items = [7, 2.5, "egg"] # Valid indices: -3 to 2

    # Organize the try, except, and finally blocks in pick()
    try:
        index = int(input())

        print("Item is", items[index])

        if index == 0:
            return "Integer"
        elif index == 1:
            return "Float"
        else:
            return "String"
    except:
        return "Index out of range"
    finally:
        print("Wrap up and return")

result = pick()
print(result)
