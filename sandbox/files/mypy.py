# in: 9
# in: A
# in: L
# in: q
user_input = input()
while user_input != "q":
    try:
        number = int(user_input)
        print(number * 3)
    except:
        print("x")
    user_input = input()
print("e")
