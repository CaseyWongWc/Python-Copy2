import my_lib
try:
    result = my_lib.magic()
except AttributeError:
    print("No magic() function in my_lib.")
