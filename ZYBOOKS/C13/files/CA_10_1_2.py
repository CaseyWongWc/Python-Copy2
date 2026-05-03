found_one = False

while not found_one:
    try:
        expiration_month = int(input())
        found_one = True
        print(f"Expiration month is {expiration_month}")
        print("Processed one valid input value")

    except:
        print("Discarded the invalid expiration month entered")
