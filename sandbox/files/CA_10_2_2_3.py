<<<<<<< HEAD
import my_lib
=======
#import my_lib
>>>>>>> 17e18c7 (Add code snippets to several files for testing purposes)

try:
    result = my_lib.magic()
    f = open(result, "r")
    print(f.read())
except AttributeError:
    print("No magic() function in my_lib")
except IOError:
    print("Could not open file.")
except:
    print("Something bad has happened.")
