try:
    filename = input("File: ")
    with open(filename, "r") as f:
        for line in f:
            print(float(line))
except FileNotFoundError:
    print("That file does not exist.")
except ValueError:
    print("One line was not a number.")
except Exception as e:
    print(e)
finally:
    print("Program finished.")