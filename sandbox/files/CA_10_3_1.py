valid_password = False
while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError("Invalid")

        valid_password = True
        print("Accepted")

    except ValueError as excpt:
        print(f"Error: {excpt}")
