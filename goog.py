from Helpers.helpings import *


try:
    a=1
    print(a)
    # out: 1
    b
    print(b)
except Exception as e:
    print(e)
    # out: name 'b' is not defined
1+1
# val: 2




try:
    res = 1/0
    print("Yay!")
except ZeroDivisionError:
    print("Nope!")
    # out: Nope!

print("Done!")
# out: Done!





cmd("python",'''
# out: python: can't open file '/home/runner/workspace/\ntry:\n    res=1/0\n    print("Yay!")    \nexcept IndexError:\n    print("Nope!")\n': [Errno 2] No such file or directory
try:
    res=1/0
    print("Yay!")    
except IndexError:
    print("Nope!")
''')











try:
    res = 1/0
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
        print('something is wrong')
        # out: something is wrong
        return
    finally:
        print('Finallyyyy!')
        # out: Finallyyyy!

test()
# val: None




nums = [-1, 0, 1]
for num in nums:
    try:
        res = 10 / num
        print(f'10 / {num} = {res}')
        # out: 10 / -1 = -10.0
    except:
        print('Something is wrong')
        # out: Something is wrong
        break
    finally:
        print('Finallyyy!')
        # out: Finallyyy!
        # out: Finallyyy!






try:
    lst = 10 * [0]
    x = lst[9]
    print('Done')
    # out: Done
except IndexError:
    print('Index out of bound')
else:
    print('Nothing is wrong')
    # out: Nothing is wrong
finally:
    print('Finally we are here')
    # out: Finally we are here
print('Continue')
# out: Continue








def main():
    try:
        f()
        print('after the function call')
    except ZeroDivisionError:
        print('Divided by zero!')
        # out: Divided by zero!
    except:
        print('Exception')

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
    res = 1/0
except ArithmeticError:
    print('ArithmeticError')
    # out: ArithmeticError
except ZeroDivisionError:
    print('ArithmeticError')
print('Continue')
# out: Continue






