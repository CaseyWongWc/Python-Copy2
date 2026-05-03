user_input = input()

while user_input != "q":
    try:
        number = int(user_input)
        print(number * 4)

    except:
        print("x")

    user_input = input()

print("e")
