from Helpers.helpings import *

# raise ValueError(123)

try:
    a = 1
    print(a)
    # out: 1
    b
    print(b)
except Exception as e:
    print(e)
    # out: name 'b' is not defined
1 + 1
# val: 2


try:
    res = 1 / 0
    print("Yay!")
except ZeroDivisionError:
    print("Nope!")
    # out: Nope!

print("Done!")
# out: Done!


cmd(
# out: python: can't open file '/home/runner/workspace/\ntry:\n    res=1/0\n    print("Yay!")    \nexcept IndexError:\n    print("Nope!")\n': [Errno 2] No such file or directory
    "python",
    """
try:
    res=1/0
    print("Yay!")    
except IndexError:
    print("Nope!")
""",
)


try:
    res = 1 / 0
    print("Yay!")
except ZeroDivisionError:
    print("Nope!")
    # out: Nope!
except Exception as e:
    print(e)

print("Done!")
# out: Done!


def test():
    try:
        res = 1 / 0
    except:
        print("something is wrong")
        # out: something is wrong
        return
    finally:
        print("Finallyyyy!")
        # out: Finallyyyy!


test()
# val: None


nums = [-1, 0, 1]
for num in nums:
    try:
        res = 10 / num
        print(f"10 / {num} = {res}")
        # out: 10 / -1 = -10.0
    except:
        print("Something is wrong")
        # out: Something is wrong
        break
    finally:
        print("Finallyyy!")
        # out: Finallyyy!
        # out: Finallyyy!


try:
    lst = 10 * [0]
    x = lst[9]
    print("Done")
    # out: Done
except IndexError:
    print("Index out of bound")
else:
    print("Nothing is wrong")
    # out: Nothing is wrong
finally:
    print("Finally we are here")
    # out: Finally we are here
print("Continue")
# out: Continue


def main():
    try:
        f()
        print("after the function call")
    except ZeroDivisionError:
        print("Divided by zero!")
        # out: Divided by zero!
    except:
        print("Exception")


def f():
    print(1 / 0)


main()  # Call the main function
# val: None


def func1():
    print("start func 1")
    # out: start func 1
    try:
        x = 1 / 1
        func2()
        # val: None
    except:
        print("something's wrong")
    print("end func 1")
    # out: end func 1


def func2():
    print("start func 2")
    # out: start func 2
    # out: start func 2
    try:
        x = 1 / 0
    except:
        print("something's wrong")
        # out: something's wrong
        # out: something's wrong
    print("end func 2")
    # out: end func 2
    # out: end func 2


func1()
# val: None
func2()
# val: None


try:
    res = 1 / 0
except ArithmeticError:
    print("ArithmeticError")
    # out: ArithmeticError
except ZeroDivisionError:
    print("ArithmeticError")
print("Continue")
# out: Continue


def invite_alex():
    print("Alex calling")
    # out: Alex calling
    invite_ben()
    # val: None
    print("Alex finishes calling")
    # out: Alex finishes calling


def invite_ben():
    print("Ben calling")
    # out: Ben calling
    # out: Ben calling
    invite_carol()
    # val: None
    # val: None
    print("Ben finishes calling")
    # out: Ben finishes calling
    # out: Ben finishes calling


def invite_carol():
    print("Carol confirm")
    # out: Carol confirm
    # out: Carol confirm
    # out: Carol confirm
    print("Carol hang up!")
    # out: Carol hang up!
    # out: Carol hang up!
    # out: Carol hang up!


invite_carol()
# val: None
invite_ben()
# val: None
invite_alex()
# val: None


def countdown(n):
    if n == 0:  # Base case - stop here
        print("Happy New Year!")
        # out: Happy New Year!
        return

    print(n)
    # out: 3
    # out: 2
    # out: 1
    countdown(n - 1)  # Recursive case
    # val: None
    # val: None
    # val: None


countdown(3)
# val: None
print("Done!")
# out: Done!


def countdown(n):
    if n == 0:  # Base case - stop here
        print("Happy New Year!")
        # out: Happy New Year!
        return
    print(n)
    # out: 3
    # out: 2
    # out: 1
    countdown(n - 1)  # Recursive case
    # val: None
    # val: None
    # val: None


countdown(3)
# val: None
print("Done!")
# out: Done!


def factorial(n):
    if n == 1:
        return 1  # base case
    return n * factorial(n - 1)  # recursive case


print(factorial(4))
# out: 24


def factorial(g):
    print(g)
    # out: 4
    # out: 3
    # out: 2
    # out: 1
    if g == 1:
        return 1  # base case
    return g * factorial(g - 1)  # recursive case


print(factorial(4))
# out: 24


def fac(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


#print(fac(1000))
#cmd(
#    "python",
#    "-c",
#    "try:\n    res=1/0\n    print('Yay!')\nexcept IndexError:\n    print('Nope!')",
#)




try:
    filename = str("goog.py")
    with open(filename, "r") as f:
        for line in f:
            print(float(line))
except FileNotFoundError:
    print("That file does not exist.")
except ValueError:
    print("One line was not a number.")
    # out: One line was not a number.
except Exception as e:
    print(e)
finally:
    print("Program finished.")
    # out: Program finished.


def countdown(n):
    if n == 0:
        print("done")
        # out: done
        return
    print(n)
    # out: 3
    # out: 2
    # out: 1
    countdown(n - 1)
    # val: None
    # val: None
    # val: None

countdown(3)
# val: None

def factorial(n):
    print(n)
    # out: 4
    # out: 3
    # out: 2
    # out: 1
    if n == 1:
        print("done")
        # out: done
        return 1
    print (f"{n} * factorial({n-1})")
    # out: 4 * factorial(3)
    # out: 3 * factorial(2)
    # out: 2 * factorial(1)
    return n * factorial(n - 1)

factorial(4)
# val: 24






class NegativeNumberError(Exception):
    pass

def square(n):
    if n < 0:
        raise NegativeNumberError("number cannot be negative")
    return n * n

try:
    print(square(-3))
except NegativeNumberError as e:
    print(e)
    # out: number cannot be negative

#

class fart(Exception):
    pass
def isbool_(n):
     if n == True or n == False:
        return True
     else:
        raise fart("not a bool💥")
try:
    print(isbool_(1),"i am true")
    # out: True i am true
    print(isbool_("yes"))
except fart as e:
    print(e)
    # out: not a bool💥
