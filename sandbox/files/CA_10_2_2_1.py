ages = []
prompt = "Enter age ('q' to quit): "
user_input = input(prompt)
while user_input != "q":
    try:
        ages.append(int(user_input))
        user_input = input(prompt)
    except:
        print("Unable to add age.")
        user_input = input(prompt)
print(ages)
