with "README.MD":
    # zyBooks Chapter 12 (Files)

    ## Checklist + scores

    | Section | Earned | Possible | Status | Notes |
    | --- | ---: | ---: | --- | --- |
    | 12.1 | 1 | 8 | ⏳ In progress | P 12.1.1 (1/1), 12.1.2 (0/3). C 12.1.1 (0/4). |
    | 12.2 | 0 | 11 | ⬜ Not started | P 12.2.1 (0/3), 12.2.2 (0/1), 12.2.3 (0/3). C 12.2.1 (0/4). |
    | 12.3 | 0 | 7 | ⬜ Not started | P 12.3.1 (0/1), 12.3.2 (0/3), 12.3.3 (0/3). |
    | 12.4 | 0 | 6 | ⬜ Not started | P 12.4.1 (0/4), 12.4.2 (0/2). |
    | 12.5 | 0 | 2 | ⬜ Not started | P 12.5.1 (0/2). |
    | 12.6 | 0 | 4 | ⬜ Not started | P 12.6.1 (0/2). C 12.6.1 (0/2). |
    | 12.7 | 0 | 2 | ⬜ Not started | P 12.7.1 (0/2). |
    | 12.8 | 0 | 10 | ⬜ Not started | Lab 12.8.1 (0/10). |
    | 12.9 | 0 | 10 | ⬜ Not started | Lab 12.9.1 (0/10). |
    | 12.12 | 0 | 10 | ⬜ Not started | Lab 12.12.1 (0/10). |

    Total so far: 1 / 70

    ## Links
    - https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/12/section/1
##############################################################################
'''12.1 Reading files

Open with open(path), read with .read() / .readlines() / .readline(),
iterate with `for line in f`, then close with .close().
Returns a file object. .read() => whole file as a string.
.readlines() => list of lines (each ending with "\n" except maybe the last).
.readline() => one line at a time, useful for huge files.
'''
##############################################################################
# Set up a sample text file the examples can actually read.
with "myfile.txt":
    Because he's the hero Gotham deserves,
    but not the one it needs right now.
##############################################################################
# Figure 12.1.1 — open, read, close, print.
with Scratch:
    print("Opening file myfile.txt.")
    # out: Opening file myfile.txt.
    f = open("myfile.txt")

    print("Reading file myfile.txt.")
    # out: Reading file myfile.txt.
    contents = f.read()

    print("Closing file myfile.txt.")
    # out: Closing file myfile.txt.
    f.close()
    # val: None

    print("\nContents of myfile.txt:")
    # out: 
    # out: Contents of myfile.txt:
    print(contents)
    # out: 5
    # out: 423
    # out: 234
##############################################################################
# Set up readme.txt for the participation activity (1, 2, 3).
with "readme.txt":
    line one
    line two
    line three
    line four
##############################################################################
'''participation activity 12.1.2: Opening files and reading text.
1) Open the file "readme.txt" for reading.
2) Read up to 500 bytes from "readme.txt" into the contents variable.
3) Print the second line of "readme.txt".
'''
# 1) open
with Scratch as p1:
    my_file = open("readme.txt")
    my_file.close()
    # val: None

# 2) read up to 500 bytes
with Scratch as p2:
    my_file = open("readme.txt")
    contents = my_file.read(500)
    print(contents)
    # out: line one
    # out: line two
    # out: line three
    # out: line four
    my_file.close()
    # val: None

# 3) print the second line
with Scratch as p3:
    my_file = open("readme.txt")
    lines = my_file.readlines()
    print(lines[1], end="")
    # out: line two
    my_file.close()
    # val: None
##############################################################################
# Figure: average of integers in a file (mydata.txt with one int per line).
with "mydata.txt":
    105
    # out: 6
    # out: 3
    # out: 1
    # out: j
    # out: Ana
    # out: Ben
    # out: 5
    # out: Enter age ('q' to quit): Ana
    # out: Enter age ('q' to quit): Ben
    # out: Enter age ('q' to quit): 5
    # out: Enter age ('q' to quit): 6
    # out: Enter age ('q' to quit): q
    # out: seven
    # out: 0
    # out: 10
    # out: end
    # out: 2
    # out: 0
    # out: -8
    # out: end
    # out: 11
    # out: 60
    # out: -30
    # out: apples84
    # out: blue183
    # out: magenta46
    # out: 0
    # out: 43
    # out: 1
    # out: Enter number: 1
    # out: Lee 18
    # out: continue 123
    # out: lee 18
    # out: Lee 18
    # out: Lua 21
    # out: Mary Beth 19
    # out: Stu 33
    # out: -1
    # out: Lee 18
    # out:     Lua 21
    # out:     Mary Beth 19
    # out:     Stu 33
    # out:     -1
    # out: Lee 18
    # out:     Lua 21
    # out:     Mary Beth 19
    # out:     Stu 33
    # out:     -1
    # out: Lee 18
    # out: Lua 21
    # out: Mary Beth 19
    # out: Stu 33
    # out: -1
    # out: 5
    # out: 12
    # out: -2
    # out: -15
    # out: 0
    # out: 10
    # out: 5
    # out: 15
    # out: 3
    # out: 5345
    # out: 0
    # out: Reagan
    65
    78
    90
    62
##############################################################################
with Scratch:
    print("Reading in data....")
    # out: Reading in data....
    f = open("mydata.txt")
    lines = f.readlines()
    f.close()
    # val: None

    print("\nCalculating average....")
    # out: 
    # out: Calculating average....
    total = 0
    for ln in lines:
        total += int(ln)

    avg = total / len(lines)
    print(f"Average value: {avg}")
    # out: Average value: 80.0
##############################################################################
# Echo the contents of a file using `for line in f`.
with Scratch:
    f = open("myfile.txt")
    for line in f:
        print(line, end="")
        # out: 5
        # out: 423
        # out: 234
    f.close()
    # val: None
##############################################################################
'''CHALLENGE ACTIVITY 12.1.1: Reading files.

Level 1: assign my_file by calling my_file.read() (just read it once).
Level 2: open the file from input(), assign to my_file, then close it.
Level 3: for-loop over the file with `for ... in ...` and print each line.
Level 4: combo of the above.

The grader feeds the filename via input(). For our notebook we fake it with
`# in: myfile.txt` so the Scratch block can actually run.
'''
##############################################################################
# Level 1 answer
with Scratch:
    # in: myfile.txt
    my_file = open(input())
    # out: myfile.txt
    my_file.read()
    # val: 5
    # val: 423
    # val: 234

# Level 2 answer
with Scratch:
    # in: myfile.txt
    my_file = open(input())
    # out: myfile.txt
    my_file.close()
    # val: None

# Level 3 answer
with Scratch:
    # in: myfile.txt
    my_file = open(input())
    # out: myfile.txt
    for line in my_file:
        print(line, end="")
        # out: 5
        # out: 423
        # out: 234
    print()
    # out: 
    my_file.close()
    # val: None

# Level 4 answer (open from input, for-line iterate, close)
with Scratch:
    # in: myfile.txt
    my_file = open(input())
    # out: myfile.txt
    for line in my_file:
        print(line, end="")
        # out: 5
        # out: 423
        # out: 234
    print()
    # out: 
    my_file.close()
    # val: None
1
# val: 1
##############################################################################
'''CHALLENGE 10.1.1 (carry-over from Ch 10): Handling exceptions.
user_input = input()
while user_input != "q":
    try:
        number = int(user_input)
        print(number * 3)
    except:
        print("x")
    user_input = input()
print("e")
Input: 9 / 5 / q
'''
with Scratch:
    # in: 9
    # in: 5
    # in: q
    user_input = input()
    # out: 9
    while user_input != "q":
        try:
            number = int(user_input)
            print(number * 3)
            # out: 27
            # out: 15
        except:
            print("x")
        user_input = input()
        # out: 5
        # out: q
    print("e")
    # out: e
##########################
'''challenge activity
10.1.1: Handling exceptions using try and except.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

user_input = input()
while user_input != "q":
    try:
        number = int(user_input)
        print(number * 3)
    except:
        print("x")
    user_input = input()
print("e")
Input
9
A
L
q
Output
1
2
3
4
Check
Next
1
2
3
4

Feedback?'''


##############################################################################
# Same challenge, but using `as RUN` instead of `as Scratch`.
# Saves to disk AND runs in a fresh subprocess. All stdout lands as one
# consolidated # out: block under the LAST body line — no import needed.
with "mypy.py" as RUN:
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
    # out: 36
    # out: x
    # out: x
    # out: e
####################################################
with "mypy.py" as RUN:
    # in: 9
    # in: A
    # in: L
    # in: q
    user_input = input()
    while user_input != "q":
        try:
            number = int(user_input)
            print(number * 4)
        except:
            print("x")
        user_input = input()
    print("e")
    # out: 36
    # out: x
    # out: x
    # out: e

with Scratch as a:
    print("1")
    # out: 1
a
# val: Scratch(out=['1'], err=[], outs='1')

'''9
J
M
A
8
q'''
'''challenge activity
10.1.1: Handling exceptions using try and except.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

user_input = input()
while user_input != "q":
    try:
        number = int(user_input)
        print(number * 4)
    except:
        print("x")
    user_input = input()
print("e")
Input
9
J
M
A
8
q
Output
1
2
3
4
Check
Next
1
2
3
'''
# in: 9
# in: J
# in: A
# in: 8
# in: q
with Scratch as a:
    
    user_input = input()
    # out: 9
    while user_input != "q":
        try:
            number = int(user_input)
            print(number * 4)
            # out: 36
            # out: 32
        except:
            print("x")
            # out: x
            # out: x
        user_input = input()
        # out: J
        # out: A
        # out: 8
        # out: q
    print("e")
    # out: e
with "my.py" as RUN:
    # in: 9
    # in: J
    # in: A
    # in: 8
    # in: q
    user_input = input()

    while user_input != "q":
        try:
            number = int(user_input)
            print(number * 4)

        except:
            print("x")

        user_input = input()

    print("e")
    # out: 36
    # out: x
    # out: x
    # out: 32
    # out: e
from Helpers.helpings import *
setin("6","3","1","j","5","q")
# val: None
user_input = input()
try:
    while user_input != "q":
        number = int(user_input)
        print(number * 4)
        # out: 24
        # out: 12
        # out: 4
        user_input = input()
except:
    print("x")
    # out: x
print("e")
# out: e
####################################################
'''challenge activity
10.1.2: Handling exceptions.
712910.5105864.qx3zqy7

Jump to level 1
The while loop reads values from input until an integer is read. Add an except block in the while loop to handle an exception and output "Discarded the invalid expiration month entered".

Click here for example 1 (valid input)
Ex: If the input is:
5
6
then the output is:

Expiration month is 5
Processed one valid input value
Click here for example 2 (invalid input)
Ex: If the input is:
Ana
Ben
5
6
then the output is:

Discarded the invalid expiration month entered
Discarded the invalid expiration month entered
Expiration month is 5
Processed one valid input value
found_one = False

while not found_one:
    try:
        expiration_month = int(input())
        found_one = True
        print(f"Expiration month is {expiration_month}")
        print("Processed one valid input value")

# Your code goes here
'''
setin("Ana","Ben","5","6")
# val: None
with Scratch as a:"test.py"
    print("1")
    # out: 1
a.out
# val: ['1']
found_one = False
setin("Ana","Ben","5","6")
# val: None
with Scratch as a:"CA_10_1_2.py"
    found_one = False

    while not found_one:
        try:
            expiration_month = int(input())
            found_one = True
            print(f"Expiration month is {expiration_month}")
            # out: Expiration month is 5
            print("Processed one valid input value")
            # out: Processed one valid input value

        except:
            print("Discarded the invalid expiration month entered")
            # out: Discarded the invalid expiration month entered
            # out: Discarded the invalid expiration month entered
a.out
# val: ['Discarded the invalid expiration month entered', 'Discarded the invalid expiration month entered', 'Expiration month is 5', 'Processed one valid input value']
##############################################################################
'''## 10.2 Multiple exception handlers

Sometimes the code in a try block may generate different types of exceptions. In the previous BMI example, a ValueError was generated when the int() function passed a string argument that contained letters. Other types of errors (such as NameError, TypeError, etc.) might also be generated, and thus a program may need to have unique exception-handling code for each error type. Multiple exception handlers can be added to a try block by adding additional except blocks and specifying the type of exception that each except block handles.

> **Multiple except blocks.**

### PARTICIPATION ACTIVITY: Multiple exception handlers.

Static figure:
Begin Python code:
try:
    # ...  # No error
    # ...  # Causes TypeError
    # ...
except ValueError:
    # Handle exception, e.g., print message 1
except TypeError:
    # Handle exception, e.g., print message 2
except:
    # Handle any other exception type

# ... Resume normal code below except
End Python code. All code but the first two lines of the try block and the except TypeError block is crossed out. A monitor is shown with output "Error message 2...".

Step 1: Multiple exception handlers can be added to a try block by adding additional except blocks and specifying the particular type of exception that each except block handles. The program begins executing the try block. The first line executes with no error, then the next line causes a TypeError. All code but the first two lines of the try block and the except TypeError block is crossed out, then the program executes the except TypeError block. "Error message 2..." appears and outputs to the monitor. The program resumes execution after the try and except block.

An except block with no type (as in the above BMI example) handles any unspecified exception type, acting as a catchall for all other exception types. Good practice is to generally* avoid* the use of a catchall except clause. A programmer should instead specify the particular exceptions to be handled. Otherwise, a program bug might be hidden when the catchall except clause handles an unexpected type of error.

If no exception handler exists for an error type, then an unhandled exception may occur. An unhandled exception causes the interpreter to print the exception that occurred and halt.

The following program introduces a second exception handler to the BMI program, handling a case where the user enters "0" as the height, which would cause a ZeroDivisionError exception to occur when calculating the BMI.

> **BMI example with multiple exception types.**
> ```python
> user_input = ""
> while user_input != "q":
>     try:
>         weight = int(input("Enter weight (in pounds): "))
>         height = int(input("Enter height (in inches): "))
> 
>         bmi = (float(weight) / float(height * height)) * 703
>         print(f"BMI: {bmi}")
>         print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov
>     except ValueError:
>         print("Could not calculate health info.\n")
>     except ZeroDivisionError:
>         print("Invalid height entered. Must be > 0.")
> 
>     user_input = input('Enter any key ("q" to quit): ')
> ```
> ```
> Enter weight (in pounds): 150
> Enter height (in inches): 66
> BMI: 24.207988980716255
> (CDC: 18.6-24.9 normal)
> 
> Enter any key ("q" to quit): a
> Enter weight (in pounds): One-hundred fifty
> Could not calculate health info.
> 
> Enter any key ("q" to quit): a
> Enter weight (in pounds): 150
> Enter height (in inches): 0
> Invalid height entered. Must be > 0.
> Enter any key ("q" to quit): q
> ```

In some cases, multiple exception types should be handled by the same exception handler. A tuple can be used to specify all of the exception types for which a handler's code should be executed.

> **Multiple exception types in a single exception handler.**
> ```python
> try:
>     # ...
> except (ValueError, TypeError):
>     # Exception handler for any ValueError or TypeError that occurs.
> except (NameError, AttributeError):
>     # A different handler for NameError and AttributeError exceptions.
> except:
>     # A different handler for any other exception type.
> ```

### PARTICIPATION ACTIVITY: Multiple exceptions.

ages = []
prompt = "Enter age ("q" to quit): "
user_input = input(prompt)
while user_input != "q":
      try:
            ages.append(int(user_input))
            user_input = input(prompt)

**1.** Fill in the missing code so that any type of error in the try block is handled. print("Unable to add age.")
            user_input = input(prompt)
print(ages)
Answer: except:
*Hint: An except clause with no specific exception type will handle any error that occurs.*
*An except clause with no specific exception type acts as a catchall for handling exceptions.*

import my_lib
try:
      result = my_lib.magic()

**2.** An AttributeError occurs if a function does not exist in an imported module. Fill in the missing code to handle AttributeErrors gracefully and generate an error if other types of exceptions occur. print("No magic() function in my_lib.")
Answer: except AttributeError:
*Hint: Specify the specific type of exception that you want to handle.*
*Only exceptions of type AttributeError will be handled in the except clause. Other exception types will generate an error.*

import my_lib
try:
      result = my_lib.magic()
      f = open(result, "r")
      print f.read()

**3.** If a file cannot be opened, then an IOError may occur. Fill in the missing code so that the program specially handles AttributeErrors and IOErrors, and also doesn't crash for any other type of error. print("Could not open file.")
except AttributeError:
      print("No magic() function in my_lib")
except:
      print("Something bad has happened.")
Answer: except IOError:
*Hint: Add an exception clause for the IOError exception type.*
*Exceptions are handled based on their type. An IOError will execute the handler code in the except IOError block, an AttributeError will execute the except AttributeError block, and any other exception is handled by the catchall except block.*

### CHALLENGE ACTIVITY: Enter the output of multiple exception handlers.

**Level 1:**

What is the output?

```python
user_input = input()
while user_input != "end":
    try:
        # Possible ValueError
        divisor = int(user_input)
        # Possible ZeroDivisionError
        print(60 // divisor) # Truncates to an integer
    except ValueError:
        print("v")
    except ZeroDivisionError:
        print("z")
    user_input = input()
print("OK")
```

*The try statement has two except clauses. When a value that is not an integer is input, a ValueError is generated and "v" is output. When the input is 0, a ZeroDivisionError error is generated and "z" is output. Whether or not an error occurs, the loop continues with new input. Finally, user_input is "end" and "OK" is printed.*

**Level 2:**

What is the output?

```python
numbers = [2, 4, 5, 8]
user_input = input()
while user_input != "end":
    try:
        num_val = int(user_input)
        if num_val < 0:
            # Possible IndexError if num_val is less than 0
            print(numbers[num_val])
        else:
            # Possible ZeroDivisionError
            print(20 // num_val)          # Truncates to an integer
    except ZeroDivisionError:
        print("r")
    except IndexError:
        print("s")
    user_input = input()
print("OK")
```

*[explanation]*

**Level 3:**

What is the output?

```python
user_input = input()
while user_input != "end":
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError because
            # compute() is not defined
            print(compute(divisor))
        else:
            # Possible ZeroDivisionError
            print(20 // divisor)     # Truncates to an integer
    except ValueError:
        print("v")
    except ZeroDivisionError:
        print("z")
    except:
        print("x")
    user_input = input()
print("OK")
```

*[explanation]*

### CHALLENGE ACTIVITY: Handling exceptions with math operations and common data types. (2 Levels)

**Level 1:**

**Task:**
Complete the following tasks:
- Write an exception handler to catch [...] and output [...]
- Write an exception handler to catch [...] and output [...]

**Explanation pattern:**
In the try block:
- [...] is assigned with the [...] returned by [...](input()). [...]
- [...] After the try block:
- `except [...]:` creates a handler to catch the [...] exception. [...] is output in the [...] handler.
- `except [...]:` creates a handler to catch the [...] exception. [...] is output in the [...] handler.

**Code structure:**
```python
# Your code goes here
```

**Level 2:**

**Task:**
[...] [...] [...]. In the try block, [...] is read from input[...]. Complete the following tasks:
- Write an exception handler to catch [...] and output "[...]"
- Write an exception handler to catch [...] and output "[...]"

**Explanation pattern:**
In the try block:
- [...] is assigned with the [...] returned by [...](input()). If the string returned by input() cannot be converted to [...], then [...]() causes a [...].
- [...] After the try block:
- `except [...]:` creates a handler to catch the [...] exception. "[...]" is output in the [...] handler.
- `except [...]:` creates a handler to catch the [...] exception. "[...]" is output in the [...] handler.

**Code structure:**
```python
# Your code goes here
```

Exploring further:

 - Python built-in exception types'''
####################################################
'''participation activity
10.2.2: Multiple exceptions.
1)
Fill in the missing code so that any type of error in the try block is handled.
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

Check

Show answer
2)
An AttributeError occurs if a function does not exist in an imported module. Fill in the missing code to handle AttributeErrors gracefully and generate an error if other types of exceptions occur.
import my_lib
try:
      result = my_lib.magic()

      print("No magic() function in my_lib.")

Check

Show answer
3)
If a file cannot be opened, then an IOError may occur. Fill in the missing code so that the program specially handles AttributeErrors and IOErrors, and also doesn't crash for any other type of error.
import my_lib
try:
      result = my_lib.magic()
      f = open(result, "r")
      print f.read()

      print("Could not open file.")
except AttributeError:
      print("No magic() function in my_lib")
except:
      print("Something bad has happened.")

Check

Show answer

Feedback?'''
1
# val: 1
with Scratch:"test.py"
    print("1")
    # out: 1
1
# val: 1
2
# val: 2
3
# val: 3
setin("Ana","Ben","5","6","q")
# val: None
with Scratch:"CA_10_2_2_1.py"
    # in: 5
    # in: q
    ages = []
    prompt = "Enter age ('q' to quit): "
    user_input = input(prompt)
    while user_input != "q":
        try:
            ages.append(int(user_input))
            # val: None
            # val: None
            user_input = input(prompt)
        except:
            print("Unable to add age.")
            # out: Unable to add age.
            # out: Unable to add age.
            user_input = input(prompt)
    print(ages)
    # out: [5, 6]
1
# val: 1

with "CA_10_2_2_2.py":
    import my_lib
    try:
        result = my_lib.magic()
    except AttributeError:
        print("No magic() function in my_lib.")
1
# val: 1
with "CA_10_2_2_3.py":
    #import my_lib
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

print("Done with all the exception handling.")
# out: Done with all the exception handling.
make_file("1.txt")
# val: PosixPath('/workspaces/Python-Copy2/sandbox/files/1.txt')
####################################################
'''4
seven
0
10
end


'''
setin("seven","0","10","end")
# val: None
with Scratch as a:"CA_10_2_1.py"
    
    user_input = input()
    while user_input != "end":
        try:
            # Possible ValueError
            divisor = int(user_input)
            # Possible ZeroDivisionError
            print(60 // divisor) # Truncates to an integer
            # out: 6
        except ValueError:
            print("v")
            # out: v
        except ZeroDivisionError:
            print("z")
            # out: z
        user_input = input()
    print("OK")
    # out: OK
a.out
# val: ['v', 'z', '6', 'OK']
1
# val: 1
'''challenge activity
10.2.1: Enter the output of multiple exception handlers.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

numbers = [2, 4, 5, 8]
user_input = input()
while user_input != "end":
    try:
        num_val = int(user_input)
        if num_val < 0:
            # Possible IndexError if num_val is less than 0
            print(numbers[num_val])
        else:
            # Possible ZeroDivisionError
            print(20 // num_val)          # Truncates to an integer
    except ZeroDivisionError:
        print("r")
    except IndexError:
        print("s")
    user_input = input()
print("OK")
Input
2
0
-8
end
Output
1
2
3'''
setin("2","0","-8","end")
# val: None
with Scratch as a:"CA_10_2_1.py"
    numbers = [2, 4, 5, 8]
    user_input = input()
    while user_input != "end":
        try:
            num_val = int(user_input)
            if num_val < 0:
                # Possible IndexError if num_val is less than 0
                print(numbers[num_val])
            else:
                # Possible ZeroDivisionError
                print(20 // num_val)          # Truncates to an integer
                # out: 10
        except ZeroDivisionError:
            print("r")
            # out: r
        except IndexError:
            print("s")
            # out: s
        user_input = input()
    print("OK")
    # out: OK
a.out
# val: ['10', 'r', 's', 'OK']
####################################################
'''
user_input = input()
while user_input != "end":
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError because
            # compute() is not defined
            print(compute(divisor))
        else:
            # Possible ZeroDivisionError
            print(20 // divisor)     # Truncates to an integer
    except ValueError:
        print("v")
    except ZeroDivisionError:
        print("z")
    except:
        print("x")
    user_input = input()
print("OK")
Input
one
0
5
-3
end
Output
v
z
4
x
OK
'''
####################################################
'''challenge activity
10.2.2: Handling exceptions with math operations and common data types.
712910.5105864.qx3zqy7

Jump to level 1
Complete the following tasks:

Write an exception handler to catch ValueError and output "float(): Input is not a float."
Write an exception handler to catch OverflowError and output "math.pow(): result of 20 raised to the power of ", followed by x_value and " is too large."
Click here to show example
Ex: If the input is red, then the output is:

float(): Input is not a float.

Ex: If the input is 1030.0, then the output is:

math.pow(): result of 20 raised to the power of 1030.0 is too large.
import math

try:
    x_value = float(input())
    print(f"20 raised to the power of {x_value} is {math.pow(20, x_value)}")


'''
with "CA_10_2_2.py":
    import math

    try:
        x_value = float(input())
        print(f"20 raised to the power of {x_value} is {math.pow(20, x_value)}")
    except ValueError:
        print("float(): Input is not a float.")
    except OverflowError:
        print(f"math.pow(): result of 20 raised to the power of {x_value} is too large.")
####################################################
'''challenge activity
10.2.2: Handling exceptions with math operations and common data types.
712910.5105864.qx3zqy7

Jump to level 1
List value_list contains elements 4.2, 4.1, 3.0, 3.6, 9.6, 0.1, 6.2, 7.9, 2.5, and 0.7. In the try block, integer list_index is read from input. The element at list_index of value_list is output. Complete the following tasks:

Write an exception handler to catch ValueError and output "int(): An integer is expected."
Write an exception handler to catch IndexError and output "Index is out of range."
Click here to show example
Ex: If the input is four, then the output is:

int(): An integer is expected.

Ex: If the input is 11, then the output is:
Index is out of range.
value_list = [4.2, 4.1, 3.0, 3.6, 9.6, 0.1, 6.2, 7.9, 2.5, 0.7]

try:
    list_index = int(input())
    print(f"value = {value_list[list_index]}")

# Your code goes here

'''
1
# val: 1
with "CA_10_2_2_2.py":
    value_list = [4.2, 4.1, 3.0, 3.6, 9.6, 0.1, 6.2, 7.9, 2.5, 0.7]

    try:
        list_index = int(input())
        print(f"value = {value_list[list_index]}")
    except ValueError:
        print("int(): An integer is expected.")
    except IndexError:
        print("Index is out of range.")
        
setin("11")
# val: None
with Scratch as a:"CA_10_2_2_3.py"
    value_list = [4.2, 4.1, 3.0, 3.6, 9.6, 0.1, 6.2, 7.9, 2.5, 0.7]

    try:
        list_index = int(input())
        print(f"value = {value_list[list_index]}")
    except ValueError:
        print("int(): An integer is expected.")
    except IndexError:
        print("Index is out of range.")
        # out: Index is out of range.

1
# val: 1
####################################################
'''## 10.3 Raising exceptions

Consider the BMI example once again, in which a user enters a weight and height, and that outputs the corresponding body-mass index. The programmer may wish to ensure that a user enters only valid heights and weights (ex.: greater than 0). Thus, the programmer must introduce error-checking code.

A naive approach to adding error-checking code is to intersperse if-else statements throughout the normal code. Of particular concern is the highlighted code, which is new branching logic added to the normal code, making the normal code flow of "get weight, get height, then print BMI" harder to see. Furthermore, the second check for negative values before printing the BMI is redundant and prone to a programming error caused by inconsistency with the earlier checks (e.g., checking for <= here rather than just <).

> **BMI example with error-checking code but without using exception-handling constructs.**
> | user_input = "" while user_input != "q":     weight = int(input("Enter weight (in pounds): "))     if weight < 0:         print("Invalid weight.")     else:         height = int(input("Enter height (in inches): "))         if height <= 0:             print("Invalid height")              if (weight < 0) or (height <= 0):         print("Cannot compute info.")     else:         bmi = (float(weight) / float(height * height)) * 703         print(f"BMI: {bmi}")         print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov              user_input = input('Enter any key ("q" to quit): ') |

The following program shows the same error checking carried out using exception-handling constructs. The normal code is enclosed in a try block. Code that detects an error can execute a raise statement, which causes immediate exit from the try block and the execution of an exception handler. The exception handler prints the argument passed by the raise statement that brought execution.  Notice  that the normal code flow is not obscured by new if-else statements. You can clearly see that the flow is "get weight, get height, then print BMI".

> **BMI example with error-checking code that raises exceptions.**
> ```python
> user_input = ""
> while user_input != "q":
>     try:
>         weight = int(input("Enter weight (in pounds): "))
>         if weight < 0:
>             raise ValueError("Invalid weight.")
> 
>         height = int(input("Enter height (in inches): "))
>         if height <= 0:
>             raise ValueError("Invalid height.")
> 
>         bmi = (float(weight) * 703) / (float(height * height))
>         print(f"BMI: {bmi}")
>         print("(CDC: 18.6-24.9 normal)\n")
>         # Source www.cdc.gov
> 
>     except ValueError as excpt:
>         print(excpt)
>         print("Could not calculate health info.\n")
> 
>     user_input = input('Enter any key ("q" to quit): ')
> ```
> ```
> Enter weight (in pounds): 166
> Enter height (in inches): 55
> BMI: 38.57785123966942
> (CDC: 18.6-24.9 normal)
> 
> Enter any key ("q" to quit): a
> Enter weight (in pounds): 180
> Enter height (in inches): -5
> Invalid height.
> Could not calculate health info.
> 
> Enter any key ("q" to quit): a
> Enter weight (in pounds): -2
> Invalid weight.
> Could not calculate health info.
> 
> Enter any key ("q" to quit): q
> ```

A statement like `raise ValueError("Invalid weight.")` creates a new exception of type ValueError with a string argument that details the issue. The programmer could have specified any type of exception in place of ValueError, such as NameError or TypeError, but ValueError most closely describes the exception being handled in this case. The as keyword binds a name to the exception being handled. The statement `except ValueError as excpt` creates a new variable, excpt, that the exception-handling code might inspect for details about the exception instance. Printing the variable excpt prints the string argument passed to the exception when raised.

### PARTICIPATION ACTIVITY: Exceptions.

### CHALLENGE ACTIVITY: Exception handling.

**Level 1:**

What is the output?

```python
try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError("Invalid age")

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f"Avg: {avg_max_heart_rate}")

except ValueError as excpt:
    print(f"Error: {excpt}")
```

*user_age is not less than 0, so an exception is not raised, and the except block is not executed.*

**Level 2:**

What is the output?

```python
try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError("Invalid age")

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f"Avg: {avg_max_heart_rate}")

except ValueError as excpt:
    print(f"Error: {excpt}")
```

*An invalid age (less than 0) raises a `ValueError("Invalid age")` and execution jumps immediately to the end of the try block.

`except ValueError` catches the exception raised and outputs "Error: " followed by the exception's error message "Invalid age".*

**Level 3:**

What is the output?

```python
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
```

*The initial password is not less than eight characters long and therefore is valid. Thus, an exception is not raised and the loop only runs one time.*

**Level 4:**

What is the output?

```python
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
```

*An invalid password raises a `ValueError("Invalid")`.

`except ValueError` catches the exception raised and outputs "Error: " followed by the exception's error message "Invalid". The loop runs until a valid password, eight or more characters long, is entered.*

### CHALLENGE ACTIVITY: Raising exceptions. (2 Levels)

**Level 1:**

**Task:**
Integers [...] and [...] are read from input, representing the [...]. In the try block: Raise a ValueError exception with the message "[...]" if [...] is [...].
Raise a ValueError exception with the message "[...]" if [...] is [...].

**Explanation pattern:**
raise ValueError(msg) raises a ValueError with msg as the error message. In the try block: Integers [...] and [...] are read from input.
If [...] is [...], then a ValueError exception is raised with "[...]" as the message.
If [...] is [...], then a ValueError exception is raised with "[...]" as the message.
If no exception is raised, then [...] is computed and output. After the try block, an except block handles any ValueError exception and outputs the string argument passed to the exception.

**Code structure:**
```python
try:
    ___ = int(input())  
    ___ = int(input())
# Your code goes here
___ = ___ ___ ___

    print(f"___")

except ValueError as excpt:
    print(f"Error: {excpt}")
```

**Level 2:**

**Task:**
[...]. In the try block, integer [...] is read from input[...]. Write an exception handler to: Catch [...]Error exception and bind excpt1 to the exception instance being caught.
Output excpt1[...]

**Explanation pattern:**
In the try block: [...] After the try block, `except [...]Error as excpt1` creates a handler to catch the [...]Error exception as excpt1. In the handler[...]

**Code structure:**
```python
___

try:
    ___
    
    print(f"___")
# Your code goes here
```
'''
####################################################
'''participation activity
10.3.1: Exceptions.
How to use this tool

participation activity
10.3.1: Exceptions.
How to use this tool
except NameError:
try
except:
raise ValueError
except (ValueError, NameError):

Describes a block of code that uses exception handling
An exception handler for NameError exceptions
An exception handler for ValueError and NameError exceptions
A catchall exception handler
Causes a ValueError exception to occur

Reset'''
with "PA_10_3_1.txt":
    """
    1)Describes a block of code that uses exception handling
        Try
    2)An exception handler for NameError exceptions
        except NameError:
    3)An exception handler for ValueError and NameError exceptions
        except (ValueError, NameError):
    4)A catchall exception handler
        except:
    """

with Scratch as a:"PA_10_3_1.py"
    try:
        print(x)
    except NameError:
        print("NameError exception caught.")
        # out: NameError exception caught.
with Scratch as a:"PA_10_3_1.py"
    try:
        print(x)
    except (ValueError, NameError):
        print("ValueError or NameError exception caught.")
        # out: ValueError or NameError exception caught.
with Scratch as a:"PA_10_3_1.py"
    try:
        print(x)
    except:
        print("An exception was caught.")
        # out: An exception was caught.
with Scratch as a:"PA_10_3_1.py"
    try:
        raise ValueError("This is a ValueError.")
    except NameError:
        print("NameError exception caught.")
    except (ValueError, NameError) as excpt:
        print(f"ValueError or NameError exception caught: {excpt}")
        # out: ValueError or NameError exception caught: This is a ValueError.
    except:
        print("An exception was caught.")
1
# val: 1
####################################################

'''
challenge activity
10.3.1: Exception handling.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError("Invalid age")

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f"Avg: {avg_max_heart_rate}")

except ValueError as excpt:
    print(f"Error: {excpt}")
Input
50
Output
1
2
3
4
Check
Next
1
2
3
4

Feedback?'''
setin("60")
# val: None
with Scratch as a:"CA_10_3_1.py"
    try:
        user_age = int(input())

        if user_age < 0:
            raise ValueError("Invalid age")

        # Source: https://www.heart.org/en/healthy-living/fitness
        avg_max_heart_rate = 220 - user_age

        print(f"Avg: {avg_max_heart_rate}")
        # out: Avg: 160
    except ValueError as excpt:
        print(f"Error: {excpt}")
a
# val: Scratch(user_age=60, avg_max_heart_rate=160, out=['Avg: 160'], err=[], outs='Avg: 160')
####################################################
'''challenge activity
10.3.1: Exception handling.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError("Invalid age")

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f"Avg: {avg_max_heart_rate}")

except ValueError as excpt:
    print(f"Error: {excpt}")
Input
-30
Output
1
2
3
4
Check
Next
1
2
3
4'''
setin("-30")
# val: None
with Scratch as a:"CA_10_3_1.py"
    try:
        user_age = int(input())

        if user_age < 0:
            raise ValueError("Invalid age")

        # Source: https://www.heart.org/en/healthy-living/fitness
        avg_max_heart_rate = 220 - user_age

        print(f"Avg: {avg_max_heart_rate}")
    except ValueError as excpt:
        print(f"Error: {excpt}")
        # out: Error: Invalid age
a
# val: Scratch(user_age=-30, out=['Error: Invalid age'], err=[], outs='Error: Invalid age')
####################################################
'''challenge activity
10.3.1: Exception handling.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

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
Input
apples84
Output
'''
setin("apples84")
# val: None

with Scratch as a:"CA_10_3_1.py"
    valid_password = False
    while valid_password == False:
        try:
            password = input()

            if len(password) < 8:
                raise ValueError("Invalid")

            valid_password = True
            print("Accepted")
            # out: Accepted

        except ValueError as excpt:
            print(f"Error: {excpt}")
a.out
# val: ['Accepted']
setin("apple")
# val: None
'''valid_password = False

while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError("Invalid")

        valid_password = True
        print("Accepted")

    except ValueError as excpt:
        print(f"Error: {excpt}")
Input
blue183
magenta46
Output
'''
setin("blue183","magenta46")
# val: None
with Scratch as a:"CA_10_3_1_2.py"
    valid_password = False

    while valid_password == False:
        try:
            password = input()

            if len(password) < 8:
                raise ValueError("Invalid")

            valid_password = True
            print("Accepted")
            # out: Accepted

        except ValueError as excpt:
            print(f"Error: {excpt}")
            # out: Error: Invalid
a.out
# val: ['Error: Invalid', 'Accepted']
####################################################
'''challenge activity
10.3.2: Raising exceptions.
712910.5105864.qx3zqy7

Jump to level 1
Integers total_avocados and avocados_requested are read from input, representing the number of avocados available and the number of avocados a customer wants to buy. In the try block:

Raise a ValueError exception with the message "Number of avocados available must be positive" if total_avocados is less than or equal to 0.
Raise a ValueError exception with the message "Number of avocados requested must be within range" if avocados_requested is less than 0 or is greater than total_avocados.
Click here for example 1 (invalid input - negative)
Ex 1: If the input is:
0
43
then the output is:

Error: Number of avocados available must be positive
Click here for example 2 (invalid input - non-positive or too large)
Ex 2: If the input is:
43
50
then the output is:

Error: Number of avocados requested must be within range
Click here for example 3 (valid input)
Ex 3: If the input is:
43
25
then the output is:

Avocados remaining: 18

'''
setin("0","43")
# val: None
with Scratch as a:"CA_10_3_2.py"
    try:
        total_avocados = int(input())
        avocados_requested = int(input())

        if total_avocados <= 0:
            raise ValueError("Number of avocados available must be positive")

        if avocados_requested < 0 or avocados_requested > total_avocados:
            raise ValueError("Number of avocados requested must be within range")

        avocados_remaining = total_avocados - avocados_requested
        print(f"Avocados remaining: {avocados_remaining}")
    except ValueError as excpt:
        print(f"Error: {excpt}")
        # out: Error: Number of avocados available must be positive
a.out
# val: ['Error: Number of avocados available must be positive']
1
# val: 1
####################################################
'''
My library >
CS 2520: Python for Programmers home >
10.3: Raising exceptions
Casey Wong
10.2 Multiple exception handlers
Students:
Section 10.3 is a part of 1 assignment:
C_13
Activities:
P
Participation
C
Challenge
Due: 05/14/2026, 11:59 PM PDT
10.3 Raising exceptions
Consider the BMI example once again, in which a user enters a weight and height, and that outputs the corresponding body-mass index. The programmer may wish to ensure that a user enters only valid heights and weights (ex.: greater than 0). Thus, the programmer must introduce error-checking code.

A naive approach to adding error-checking code is to intersperse if-else statements throughout the normal code. Of particular concern is the highlighted code, which is new branching logic added to the normal code, making the normal code flow of "get weight, get height, then print BMI" harder to see. Furthermore, the second check for negative values before printing the BMI is redundant and prone to a programming error caused by inconsistency with the earlier checks (e.g., checking for <= here rather than just <).

Figure 10.3.1: BMI example with error-checking code but without using exception-handling constructs.
user_input = ""
while user_input != "q":
    weight = int(input("Enter weight (in pounds): "))
    if weight < 0:
        print("Invalid weight.")
    else:
        height = int(input("Enter height (in inches): "))
        if height <= 0:
            print("Invalid height")
        
    if (weight < 0) or (height <= 0):
        print("Cannot compute info.")
    else:
        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov
        
    user_input = input('Enter any key ("q" to quit): ')

Feedback?
The following program shows the same error checking carried out using exception-handling constructs. The normal code is enclosed in a try block. Code that detects an error can execute a raise statement, which causes immediate exit from the try block and the execution of an exception handler. The exception handler prints the argument passed by the raise statement that brought execution. Notice that the normal code flow is not obscured by new if-else statements. You can clearly see that the flow is "get weight, get height, then print BMI".

Figure 10.3.2: BMI example with error-checking code that raises exceptions.
user_input = ""
while user_input != "q":
    try:
        weight = int(input("Enter weight (in pounds): "))
        if weight < 0:
            raise ValueError("Invalid weight.")

        height = int(input("Enter height (in inches): "))
        if height <= 0:
            raise ValueError("Invalid height.")

        bmi = (float(weight) * 703) / (float(height * height))
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print("Could not calculate health info.\n")

    user_input = input('Enter any key ("q" to quit): ')
Enter weight (in pounds): 166
Enter height (in inches): 55
BMI: 38.57785123966942
(CDC: 18.6-24.9 normal)

Enter any key ("q" to quit): a
Enter weight (in pounds): 180
Enter height (in inches): -5
Invalid height.
Could not calculate health info.

Enter any key ("q" to quit): a
Enter weight (in pounds): -2
Invalid weight.
Could not calculate health info.

Enter any key ("q" to quit): q

Feedback?
A statement like raise ValueError("Invalid weight.") creates a new exception of type ValueError with a string argument that details the issue. The programmer could have specified any type of exception in place of ValueError, such as NameError or TypeError, but ValueError most closely describes the exception being handled in this case. The as keyword binds a name to the exception being handled. The statement except ValueError as excpt creates a new variable, excpt, that the exception-handling code might inspect for details about the exception instance. Printing the variable excpt prints the string argument passed to the exception when raised.

participation activity
10.3.1: Exceptions.
How to use this tool
Mouse: Drag/drop
Keyboard: Grab/release Spacebar (or Enter). Move ↑↓←→. Cancel Esc

except NameError:
try
Describes a block of code that uses exception handling
Correct
except NameError:
except NameError:
An exception handler for NameError exceptions
Correct
except (ValueError, NameError):
An exception handler for ValueError and NameError exceptions
Correct
except:
A catchall exception handler
Correct
raise ValueError
Causes a ValueError exception to occur
Correct

Reset

Feedback?
challenge activity
10.3.1: Exception handling.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

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
Input
blue183
magenta46
Output
Error: Invalid
Accepted

1
2
3
4
Check
Next
Done. Click any level to practice more. Completion is preserved.
Correct An invalid password raises a ValueError("Invalid").

except ValueError catches the exception raised and outputs "Error: " followed by the exception's error message "Invalid". The loop runs until a valid password, eight or more characters long, is entered.
Yours	Error: Invalid
Accepted
Expected	
Error: Invalid
Accepted
 
1
2
3
4

Feedback?
challenge activity
10.3.2: Raising exceptions.
712910.5105864.qx3zqy7

Jump to level 1
Set prizes_available contains three prizes read from input. In the try block, integer prize_picked is read from input and is removed from prizes_available. Write an exception handler to:

Catch a KeyError exception and bind excpt1 to the exception instance being caught.
Output excpt1 followed by " is not available." on one line.
Click here for example 1 (invalid input)
Ex 1: If the input is:
bouquet cash guitar
chalk
then the output is:

'chalk' is not available.
Click here for example 2 (valid input)
Ex 2: If the input is:
bouquet cash guitar
guitar
then the output is:

Picked: guitar
Note: The message in a KeyError is always enclosed in single quotes.
prize1, prize2, prize3 = input().split()
prizes_available = {prize1, prize2, prize3}

try:
    prize_picked = input()
    prizes_available.remove(prize_picked)
    
    print(f"Picked: {prize_picked}")

# Your code goes here
'''
with "CA_10_3_2.py":
    prize1, prize2, prize3 = input().split()
    prizes_available = {prize1, prize2, prize3}

    try:
        prize_picked = input()
        prizes_available.remove(prize_picked)
        
        print(f"Picked: {prize_picked}")

    except KeyError as excpt:
        print(f"{excpt} is not available.")
##############################################################################
'''## 10.4 Exceptions with functions

The power of exceptions becomes even more clear when used within functions. If an exception is raised within a function and is not handled within that function, then the function is immediately exited and the calling function is checked for a handler, and so on up the function call hierarchy. The following program illustrates this. Note the clarity of the normal code, which obviously "gets the weight, gets the height, and prints the BMI" &ndash; the error checking code does not obscure the normal code.

> **BMI example using exception-handling constructs along with functions.**
> ```python
> def get_weight():
>     weight = int(input("Enter weight (in pounds): "))
>     if weight < 0:
>         raise ValueError("Invalid weight.")
>     return weight
> 
> def get_height():
>     height = int(input("Enter height (in inches): "))
>     if height <= 0:
>         raise ValueError("Invalid height.")
>     return height
> 
> user_input = ""
> while user_input != "q":
>     try:
>         weight = get_weight()
>         height = get_height()
> 
>         bmi = (float(weight) / float(height * height)) * 703
>         print(f"BMI: {bmi}")
>         print("(CDC: 18.6-24.9 normal)\n")
>         # Source www.cdc.gov
> 
>     except ValueError as excpt:
>         print(excpt)
>         print("Could not calculate health info.\n")
> 
>     user_input = input('Enter any key ("q" to quit): ')
> ```
> ```
> Enter weight (in pounds): 150
> Enter height (in inches): 66
> BMI: 24.207988980716255
> (CDC: 18.6-24.9 normal)
> 
> Enter any key ("q" to quit): a
> Enter weight (in pounds): -1
> Invalid weight.
> Could not calculate health info.
> 
> Enter any key ("q" to quit): a
> Enter weight (in pounds): 150
> Enter height (in inches): -1
> Invalid height.
> Could not calculate health info.
> 
> Enter any key ("q" to quit): q
> ```

Suppose get_weight() raises an exception of type ValueError. The get_weight() function does not handle exceptions (there is no try block in the function), so it immediately exits. Going up the function call hierarchy returns execution to the global scope script code, where the call to get_weight() was in a try block, so the exception handler for ValueError is executed.

Notice the clarity of the script's code. Without exceptions, the get_weight() function would have had to indicate failure, perhaps through a special return value like -1. The script would have had to check for such failure and would have required additional if-else statements, obscuring the functionality of the code.

### PARTICIPATION ACTIVITY: Exceptions in functions.

**1.** For a function that may contain a raise statement, the function's statements must be placed in a try block within the function.
Answer: **False**
*If no try block appears in the function, the raise statement causes automatic exiting from the function. The calling statement is then checked for an exception handler until the exception is handled or the script is exited.*

**2.** A raise statement executed in a function automatically causes a jump to the last return statement  in the function.
Answer: **False**
*A raise causes immediate exit. Nothing gets returned by the function, which is not a problem because the function call code is not resumed. Instead, the exception-handling process looks through the function call hierarchy for an exception handler that handles the raised exception.*

**3.** A key goal of exception handling is to avoid polluting normal code with distracting error-handling code.
Answer: **True**
*Without try/except functionality, programmers commonly resort to special return values (such as -1), extra mutable parameters, or return values that are containers (containing a success/fail flag variable). Each  approach requires normal code to be modified to check the value.*

### CHALLENGE ACTIVITY: Moving on a chess board.

Organize the code blocks so that:
- get_column() throws a ValueError if column is not between "a" and "h", both inclusive.
- get_row() throws a ValueError if row is not between 1 and 8, both inclusive.
- the try block gets the values of column and row and outputs the move.
- the except block outputs the argument passed by a raise statement.

**Solution:**
```python
def get_column():
    column = input()
  if (column < "a") or (column > "h"):
    raise ValueError("Column must be between a and h")
    return column

def get_row():
    row = int(input())
  if (row < 1) or (row > 8):
    raise ValueError("Row must be between 1 and 8")
    return row

try:
  column = get_column()
row = get_row()

print(f"Move to square {column}{row}")

except ValueError as excpt:
    print(excpt)
```'''
##############################################################################
setin("a","5","a","9","a","0","b","5","q")
# val: None
with "Figure 10.4.1.py":
    def get_weight():
        weight = int(input("Enter weight (in pounds): "))
        if weight < 0:
            raise ValueError("Invalid weight.")
        return weight

    def get_height():
        height = int(input("Enter height (in inches): "))
        if height <= 0:
            raise ValueError("Invalid height.")
        return height

    user_input = ""
    while user_input != "q":
        try:
            weight = get_weight()
            height = get_height()

            bmi = (float(weight) / float(height * height)) * 703
            print(f"BMI: {bmi}")
            print("(CDC: 18.6-24.9 normal)\n")
            # Source www.cdc.gov

        except ValueError as excpt:
            print(excpt)
            print("Could not calculate health info.\n")

        user_input = input('Enter any key ("q" to quit): ')

####################################################
'''participation activity
10.4.1: Exceptions in functions.
1)
For a function that may contain a raise statement, the function's statements must be placed in a try block within the function.
2)
A raise statement executed in a function automatically causes a jump to the last return statement in the function.
3)
A key goal of exception handling is to avoid polluting normal code with distracting error-handling code.
'''
with "PA_10_4_1.txt":
    """
    1)For a function that may contain a raise statement, the function's statements must be placed in a try block within the function.
        False
    2)A raise statement executed in a function automatically causes a jump to the last return statement in the function.
        False
    3)A key goal of exception handling is to avoid polluting normal code with distracting error-handling code.
        True
    """
####################################################
'''challenge activity
10.4.1: Moving on a chess board.

Full screen
712910.5105864.qx3zqy7
Organize the code blocks so that:

get_column() throws a ValueError if column is not between "a" and "h", both inclusive.
get_row() throws a ValueError if row is not between 1 and 8, both inclusive.
the try block gets the values of column and row and outputs the move.
the except block outputs the argument passed by a raise statement.
Click here for example

How to use this tool
Unused
main.py

Load default template...
    

Check'''
with "CA_10_4_1.py":
    def get_column():
        column = input()
        if (column < "a") or (column > "h"):
            raise ValueError("Column must be between a and h")
        return column

    def get_row():
        row = int(input())
        if (row < 1) or (row > 8):
            raise ValueError("Row must be between 1 and 8")
        return row

    try:
        column = get_column()
        row = get_row()

        print(f"Move to square {column}{row}")

    except ValueError as excpt:
        print(excpt)
        
##############################################################################
#changing workflow
##############################################################################
'''## 10.5 Using finally to clean up

A programmer wants to execute code regardless of whether or not an exception has been raised in a try block. Ex: If an exception occurs while reading data from a file, the file should still be closed using the file.close() method, no matter if an exception interrupted the read operation. The finally clause of a try statement allows a programmer to specify *clean-up* actions that are always executed. The following illustration demonstrates.

### PARTICIPATION ACTIVITY: Clean-up actions in a finally clause are always executed.

Static figure:
Begin Python code 1:
try:
    # ...  # No exception occurs
except:
    # Handle exception
finally:
    # Clean up actions always executed
End Python code 1. Monitor 1 is shown with output "In finally block...".

Begin Python code 2:
try:
    # ...  # exception occurs
except:
    # Handle exception
finally:
    # Clean up actions always executed
End Python code 2. Monitor 2 is shown with output:
Exception message...
In finally block...

Step 1: If no exception occurs, then execution continues in the finally clause and proceeds with the program. The program executes the try block, skips the except block, and exectues the finally block. "In finally block..." appears and is output to monitor 1.

Step 2: If a handled exception occurs, then an exception handler executes and the finally clause executes. The program executes the try block where an exception occurs, so the program executes the except block. "Exception message..." appears and is output to monitor 2. The finally block is executed and "In finally block..." appears and is output to monitor 2.

The finally clause is always the last code executed before the try block finishes. 

 - If *no exception* occurs, then execution continues in the finally clause and proceeds with the program.
 - If a *handled exception* occurs, an exception handler executes and then the finally clause.
 - If an *unhandled exception* occurs, then the finally clause executes and the exception is re-raised. 
 - The finally clause also executes if any break, continue, or return statement causes the try block to be exited.

The finally clause can be combined with exception handlers, provided that the finally clause comes last. The following program attempts to read integers from a file. The finally clause is always executed, even if an exception occurs when reading the data (such as if the file contains letters, thus causing int() to raise an exception, or if the file does not exist).

> **Clean-up actions using finally.**
> ```python
> nums = []
> rd_nums = -1
> my_file = input("Enter file name: ")
> 
> try:
>     print("Opening", my_file)
>     rd_nums = open(my_file, "r")  # Might cause IOError
> 
>     for line in rd_nums:
>         nums.append(int(line))  # Might cause ValueError
> except IOError:
>     print(f"Could not find {my_file}")
> except ValueError:
>     print(f"Could not read number from {my_file}")
> finally:
>     print(f"Closing {my_file}")
>     if rd_nums != -1:
>         rd_nums.close()
>     print(f'Numbers found: {" ".join([str(n) for n in nums])}')
> ```
> ```
> Enter file name: myfile.txt
> Opening myfile.txt
> Closing myfile.txt
> Numbers found: 5 423 234
> ...
> Enter file name: myfile.txt
> Opening myfile.txt
> Could not read number from myfile.txt
> Closing myfile.txt
> Numbers found: 
> ...
> Enter file name: invalidfile.txt
> Opening invalidfile.txt
> Could not find invalidfile.txt
> Closing invalidfile.txt
> Numbers found:
> ```

### PARTICIPATION ACTIVITY: Finally.

**1.** What is the output of divide(4, 2)?
- Cannot divide by zero.
Result is -1.
- Cannot divide by zero.
Result is 2.0.
- Result is 2.0. ✓
*The function computes 4 / 2. No exception occurs, and the finally clause is executed as the try block exits.*

**2.** What is the output of divide(4, 0)?
- Cannot divide by zero.
Result is -1. ✓
- Cannot divide by zero.
Result is 2.0.
- Result is 0.0.
*The function computes 4 / 0. Dividing by 0 raises a ZeroDivisionError.*

### CHALLENGE ACTIVITY: Using finally to wrap up before returning a value.

Organize the try, except, and finally blocks so that "Wrap up and return" is output before pick() returns any value.

**Solution:**
```python
def pick():
    items = [7, 2.5, "egg"] # Valid indices: -3 to 2

    # Organize the try, except, and finally blocks in pick()
  try:
    index = int(input())

    print("Item is", items[index])

    if index == 0:
        return "Integer"
    elif index == 1:
        return "Float"
    else:
        return "String"
  except:
    return "Index out of range"
  finally:
    print("Wrap up and return")

result = pick()
print(result)
```'''
####################################################
'''
participation activity
10.5.1: Clean-up actions in a finally clause are always executed.


1

2

If a handled exception occurs, then an exception handler executes and the finally clause executes.
try:
    # ...
except:
    # Handle exception
finally:
    # Clean up actions always executed
# No exception occurs
In finally block...
try:
    # ...
except:
    # Handle exception
finally:
    # Clean up actions always executed
In finally block...
# exception occurs
Exception message...Exception message...In finally block...In finally block...
Static figure: Begin Python code 1: try: # ... # No exception occurs except: # Handle exception finally: # Clean up actions always executed End Python code 1. Monitor 1 is shown with output "In finally block...". Begin Python code 2: try: # ... # exception occurs except: # Handle exception finally: # Clean up actions always executed End Python code 2. Monitor 2 is shown with output: Exception message... In finally block... Step 1: If no exception occurs, then execution continues in the finally clause and proceeds with the program. The program executes the try block, skips the except block, and exectues the finally block. "In finally block..." appears and is output to monitor 1. Step 2: If a handled exception occurs, then an exception handler executes and the finally clause executes. The program executes the try block where an exception occurs, so the program executes the except block. "Exception message..." appears and is output to monitor 2. The finally block is executed and "In finally block..." appears and is output to monitor 2.

Captions
If no exception occurs, then execution continues in the finally clause and proceeds with the program.
If a handled exception occurs, then an exception handler executes and the finally clause executes.
Playing step 2: If a handled exception occurs, then an exception handler executes and the finally clause executes. Step finished playing

'''
with "PA_10_5_1.txt":
    """
    1)If no exception occurs, then execution continues in the finally clause and proceeds with the program.
        If no exception occurs, then execution continues in the finally clause and proceeds with the program.
    2)If a handled exception occurs, then an exception handler executes and the finally clause executes.
        If a handled exception occurs, then an exception handler executes and the finally clause executes.
    """
1
# val: 1
####################################################
'''Figure 10.5.1: Clean-up actions using finally.'''
with "my.py":
    nums = []
    rd_nums = -1
    my_file = input("Enter file name: ")

    try:
        print("Opening", my_file)
        rd_nums = open(my_file, "r")  # Might cause IOError

        for line in rd_nums:
            nums.append(int(line))  # Might cause ValueError
    except IOError:
        print(f"Could not find {my_file}")
    except ValueError:
        print(f"Could not read number from {my_file}")
    finally:
        print(f"Closing {my_file}")
        if rd_nums != -1:
            rd_nums.close()
        print(f'Numbers found: {" ".join([str(n) for n in nums])}')
with "myfile.txt":
    5
    423
    234
with bash:
    python3 my.py < myfile.txt
    # out: 20
    # out: 1692
    # out: 936
    # err: Traceback (most recent call last):
    # err:   File "/workspaces/Python-Copy2/sandbox/files/my.py", line 11, in <module>
    # err:     user_input = input()
    # err: EOFError: EOF when reading a line
    # !err: exit code 1
1
# val: 1
##############################################################################
'''participation activity
10.5.2: Finally.'''
with "PA_10_5_2.txt":
    """
    1)What is the output of divide(4, 2)?
        Result is 2.0.
    2)What is the output of divide(4, 0)?
        Cannot divide by zero.
        Result is -1.
    """
with "main.py":
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            return -1
        finally:
            print("Result is", result)

    print(divide(4, 2))
    print(divide(4, 0))
with bash:
    python3 main.py
    # out: Result is 2.0
    # out: None
    # out: Cannot divide by zero.
    # err: Traceback (most recent call last):
    # err:   File "/workspaces/Python-Copy2/sandbox/files/main.py", line 11, in <module>
    # err:     print(divide(4, 0))
    # err:           ~~~~~~^^^^^^
    # err:   File "/workspaces/Python-Copy2/sandbox/files/main.py", line 8, in divide
    # err:     print("Result is", result)
    # err:                        ^^^^^^
    # err: UnboundLocalError: cannot access local variable 'result' where it is not associated with a value
    # !err: exit code 1

####################################################

'''challenge activity
10.5.1: Using finally to wrap up before returning a value.'''
setin("1")
# val: None
with "CA_10_5_1.py" as Scratch:
    def pick():
        items = [7, 2.5, "egg"] # Valid indices: -3 to 2

        # Organize the try, except, and finally blocks in pick()
        try:
            index = int(input())

            print("Item is", items[index])
            # out: Item is 2.5

            if index == 0:
                return "Integer"
            elif index == 1:
                return "Float"
            else:
                return "String"
        except:
            return "Index out of range"
        finally:
            print("Wrap up and return")
            # out: Wrap up and return

    result = pick()
    print(result)
    # out: Float
1
# val: 1

##############################################################################
'''## 10.6 Custom exception types

When raising an exception, a programmer can use the existing built-in exception types. For example, if an exception should be raised when the value of my_num is less than 0, the programmer might use a ValueError, as in `raise ValueError("my_num < 0")`. Alternatively, a custom exception type can be defined and then raised. The following example shows how a custom exception type LessThanZeroError might be used.

> **Custom exception types.**
> ```python
> # Define a custom exception type
> class LessThanZeroError(Exception):
>     def __init__(self, value):
>         self.value = value
> 
> my_num = int(input("Enter number: "))
> 
> if my_num < 0:
>     raise LessThanZeroError("my_num must be greater than 0")
> else:
>     print(f"my_num: {my_num}")
> ```
> ```
> Enter number: -100
> Traceback (most recent call last):
>   File "test.py", line 11, in <module>
>     raise LessThanZeroError("my_num must be greater than 0")
> __main__.LessThanZeroError
> ```

A programmer creates a custom exception type by creating a class that inherits from the built-in Exception class. The new class can contain a constructor, as shown above, that accepts an argument to be saved as an attribute. Alternatively, the class could have no constructor (and a "pass" statement might be used, since a class definition requires at least one statement). A custom exception class is typically kept bare, adding a minimal amount of functionality to keep track of information that an exception handler might need. Inheritance is discussed in detail elsewhere.

Good practice is to include "Error" at the end of a custom exception type's name, as in LessThanZeroError or MyError. Custom exception types are useful to track and handle the unique exceptions that might occur in a program's code. Many larger third-party and Python standard library modules use custom exception types.

### PARTICIPATION ACTIVITY: Custom exception types.

**1.** A custom exception type is usually defined by inheriting from the Exception class.
Answer: **True**
*Technically, a programmer does not have to inherit from Exception, but inheritance is common practice.*

**2.** The following statement defines a new type of exception: `def MyMultError: pass`
Answer: **False**
*A new class must be defined, not a function.*

**3.** "FileNotOpen" is a good name for a custom exception class.
Answer: **False**
*By convention, exception types usually end with "Error". a better name would be "FileNotOpenError".*
'''
setin("1")
# val: None
with "FIG_10_6_1.py" as Scratch:
    # Define a custom exception type
    class LessThanZeroError(Exception):
        def __init__(self, value):
            self.value = value
    # in: 1
    my_num = int(input("Enter number: "))

    if my_num < 0:
        raise LessThanZeroError("my_num must be greater than 0")
    else:
        print(f"my_num: {my_num}")
        # out: my_num: 1

####################################################
'''PA 10.6.1: Custom exception types.'''
with "PA_10_6_1.txt":
    """
    1)A custom exception type is usually defined by inheriting from the Exception class.
        True
    2)The following statement defines a new type of exception: def MyMultError: pass
        False
    3)"FileNotOpen" is a good name for a custom exception class.
        False
    """
1
# val: 1
with _:
    ###1
    class MyMultError(Exception):
        pass
    ###2
    def MyMultError():
        pass
    ###3
    class FileNotOpen(Exception):
        pass
    with _:
        print(MyMultError)
        # out: <function __sc_33__.<locals>.MyMultError at 0x7a386c0a80e0>
        print(MyMultError())
        # out: None
        print(FileNotOpen)
        # out: <class '__main__.__sc_33__.<locals>.FileNotOpen'>
        print(FileNotOpen())
        # out: 
        #⭐ out: <__main__.__sc_33__.<locals>.FileNotOpen object at 0x7f8c9c1e3e20>   
########################################################################################################
'''## 10.7 LAB: Fat-burning heart rate

### LAB ACTIVITY: LAB: Fat-burning heart rate

Write a program that calculates an adult's fat-burning heart rate, which is 70% of the difference between 220 and the person's age respectively. Complete fat_burning_heart_rate() to calculate the fat burning heart rate.
The adult's age must be between the ages of 18 and 75 inclusive. If the age entered is not in this range, raise a ValueError exception in get_age() with the message "Invalid age." Handle the exception in __main__ and print the ValueError message along with "Could not calculate heart rate info."
Ex: If the input is:

```
35
```
the output is:

```
Fat burning heart rate for a 35 year-old: 129.5 bpm
```
If the input is:

```
17
```
the output is:

```
Invalid age.
Could not calculate heart rate info.
```

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `35` | `Fat burning heart rate for a 35 year-old: 129.5 bpm` | 2 |
| 2 | `17` | `Invalid age.\nCould not calculate heart rate info.` | 2 |
| 3 | `80` | `Invalid age.\nCould not calculate heart rate info.` | 2 |
| 4 | `(none)` | `` | 2 |
| 5 | `(none)` | `` | 2 |
*Total: 10 points*
def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):

    return heart_rate


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    age = get_age()
'''
with "LAB_10_7.py":
    def get_age():
        age = int(input())
        if age < 18 or age > 75:
            raise ValueError("Invalid age.")
        return age


    def fat_burning_heart_rate(age):
        heart_rate = 0.7 * (220 - age)
        return heart_rate


    if __name__ == "__main__":
        try:
            age = get_age()
            heart_rate = fat_burning_heart_rate(age)
            print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
        except ValueError as excpt:
            print(excpt)
            print("Could not calculate heart rate info.")

with "input1.txt":
    35
with "input2.txt":
    17
with bash:
    echo 1
    # out: 1
    date
    # out: Sun May  3 15:32:33 UTC 2026
    python3 LAB_10_7.py < input1.txt
    # out: invalid literal for int() with base 10: 'Lee 18'
    # out: Could not calculate heart rate info.
    python3 LAB_10_7.py < input2.txt
    # out: invalid literal for int() with base 10: 'Lee 18'
    # out: Could not calculate heart rate info.

with bash:
    
1
# val: 1
##############################################################################
with "10.8 Lab.MD":
    '''
    ## 10.8 LAB: Exception handling to detect input string vs. integer

    ### LAB ACTIVITY: LAB: Exception handling to detect input string vs. integer

    The given program reads a list of single-word first names and ages (ending with -1), and outputs that list with the age incremented. The program fails and raises an exception if the second input on a line is a string rather than an integer. At FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for the age.
    Ex: If the input is:

    ```
    Lee 18
    Lua 21
    Mary Beth 19
    Stu 33
    -1
    ```
    then the output is:

    ```
    Lee 19
    Lua 22
    Mary 0
    Stu 34
    ```

    **Test Cases:**
    | # | Input | Expected Output | Points |
    |---|-------|-----------------|--------|
    | 1 | `Lee 18\nLua 21\nMary Beth 19\nStu 33\n-1\n` | `Lee 19\nLua 22\nMary 0\nStu 34` | 1 |
    | 2 | `Laura 63\nVaishnavi 24\nSarah Sims 33\n-1\n` | `Laura 64\nVaishnavi 25\nSarah 0` | 3 |
    | 3 | `Huw 29\nJaspar 49\nMelina Lynn 32\nQuinta 13\nMina Ny 38\nHanna 28\n-1\n` | `Huw 30\nJaspar 50\nMelina 0\nQuinta 14\nMina 0\nHanna 29` | 3 |
    | 4 | `Laura Jean 17\nChristine 55\nFelicia 31\nKofi Drew 39\nMargaux 98\n-1` | `Laura 0\nChristine 56\nFelicia 32\nKofi 0\nMargaux 99` | 3 |
    *Total: 10 points*

    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != "-1":
        # FIXME: The following line will raise ValueError exception.
        #        Insert try/except blocks to catch the exception.
        age = int(parts[1]) + 1
        print(f"{name} {age}")

        # Get next line
        parts = input().split()
        name = parts[0]

    '''
with "LAB_10_8.py":
    parts = input().split()
    name = parts[0]
    while name != "-1":
        try:
            age = int(parts[1]) + 1
        except ValueError:
            age = 0
        print(f"{name} {age}")

        parts = input().split()
        name = parts[0]
with _:
    with "input1.txt":
        Lee 18
        Lua 21
        Mary Beth 19
        Stu 33
        -1
    with bash:
        python3 LAB_10_8.py < input1.txt
        # out: Lee 19
        # out: Lua 22
        # out: Mary 0
        # out: Stu 34
1
# val: 1
##########################test
with _:
    with "delete.py":
        a=input("INP:")
        print(a)
    with "input.txt":
        Hello

    with bash:
        python3 delete.py < input.txt
        # out: INP:Lee 18
    with "input2.txt":
        Lee 18
        Lua 21
        Mary Beth 19
        Stu 33
        -1
    with bash:
        python3 delete.py < input2.txt
        # out: INP:Lee 18
    setin("Lee 18\ncontinue 123")
    # val: None
    input().split()
    # val: ['Lee', '18', 'continue', '123']
    setin("lee 18","lua 21")
    # val: None
    input().split()
    # val: ['lee', '18']
    setin("Lee 18\nLua 21\nMary Beth 19\nStu 33\n-1")
    # val: None
    input().split()
    # val: ['Lee', '18', 'Lua', '21', 'Mary', 'Beth', '19', 'Stu', '33', '-1']
    var='''Lee 18
    Lua 21
    Mary Beth 19
    Stu 33
    -1'''
    
    setin(var)
    # val: None
    input().split()
    # val: ['Lee', '18', 'Lua', '21', 'Mary', 'Beth', '19', 'Stu', '33', '-1']
    #⭐⭐⭐⭐
    with open("input.txt", "w") as f:
        f.write(var)
        # val: 52
    with bash:
        python3 delete.py < input.txt
        # out: INP:Lee 18
        cat input.txt
        # out: Lee 18
        # out:     Lua 21
        # out:     Mary Beth 19
        # out:     Stu 33
        # out:     -1
        python3 LAB_10_8.py < input.txt
        # out: Lee 19
        # out: Lua 22
        # out: Mary 0
        # out: Stu 34
    yes="Lee 18".split()
    yes
    # val: ['Lee', '18']
    print("ok")
    # out: ok
    parts= var.split();parts
    # val: ['Lee', '18', 'Lua', '21', 'Mary', 'Beth', '19', 'Stu', '33', '-1']
    name=parts[0];name
    # val: Lee
    setin(var)
    # val: None
    with _:
        parts = input().split()
        parts
        # val: ['Lee', '18', 'Lua', '21', 'Mary', 'Beth', '19', 'Stu', '33', '-1']
        name = parts[0]
        name
        # val: Lee

        while name != "-1":
            print(f"{name}✅ ")
            # out: Lee✅ 
            try:
                age = int(parts[1]) + 1;age
                # val: 19
            except ValueError:
                age = 0
            print(f"{name} {age}")
            # out: Lee 19
            break
            exit
            parts = input().split()
            name = parts[0]
    print("hi")
    # out: hi
    var
    # val: Lee 18
    # val:     Lua 21
    # val:     Mary Beth 19
    # val:     Stu 33
    # val:     -1
    var="Lee 18\nLua 21\nMary Beth 19\nStu 33\n-1"
    var
    # val: Lee 18
    # val: Lua 21
    # val: Mary Beth 19
    # val: Stu 33
    # val: -1
    parts2=var.split("\n")
    parts2
    # val: ['Lee 18', 'Lua 21', 'Mary Beth 19', 'Stu 33', '-1']
    setin("Lee 18","Lua 21","Mary Beth 19","Stu 33","-1")    
    # val: None
    with _:
        parts = input().split();parts
        # val: ['Lee', '18']
        name = parts[0];name
        # val: Lee
        while name != "-1":
            try:
                age = int(parts[1]) + 1;age
                # val: 19
                # val: 22
                # val: 34
            except ValueError:
                age = 0
            print(f"{name} {age}")
            # out: Lee 19
            # out: Lua 22
            # out: Mary 0
            # out: Stu 34

            parts = input().split();parts
            # val: ['Lua', '21']
            # val: ['Mary', 'Beth', '19']
            # val: ['Stu', '33']
            # val: ['-1']
            name = parts[0];name
            # val: Lua
            # val: Mary
            # val: Stu
            # val: -1
1
# val: 1

##############################################################################
with "10.9 LAB.MD":
    '''
    ## 10.9 LAB: Exceptions with lists

    ### LAB ACTIVITY: LAB: Exceptions with lists

    Given a list of 10 names, complete the program that outputs the name specified by the list index entered by the user. Use a try block to output the name and an except block to catch any IndexError exception as a variable. Output "Exception! " followed by the message from the exception variable. Output also the first element in the list if the invalid index is negative or the last element if the invalid index is positive.
    Note: Python allows using a negative index to access a list, as long as the magnitude of the index is smaller than the size of the list.
    Ex: If the input of the program is:

    ```
    5
    ```
    the program outputs:

    ```
    Name: Jane
    ```
    Ex: If the input of the program is:

    ```
    12
    ```
    the program outputs:

    ```
    Exception! list index out of range
    The closest name is: Johnny
    ```
    Ex: If the input of the program is:

    ```
    -2
    ```
    the program outputs:

    ```
    Name: Tyrese
    ```
    Ex: If the input of the program is:

    ```
    -15
    ```
    the program outputs:

    ```
    Exception! list index out of range
    The closest name is: Ryley
    ```

    **Test Cases:**
    | # | Input | Expected Output | Points |
    |---|-------|-----------------|--------|
    | 1 | `5` | `Name: Jane` | 2 |
    | 2 | `12` | `Exception! list index out of range\nThe closest name is: Johnny` | 2 |
    | 3 | `-2` | `Name: Tyrese` | 1 |
    | 4 | `-15` | `Exception! list index out of range\nThe closest name is: Ryley` | 2 |
    | 5 | `0` | `Name: Ryley` | 1 |
    | 6 | `10` | `Exception! list index out of range\nThe closest name is: Johnny` | 2 |
    *Total: 10 points* 

    ```python
    names = [
        "Ryley",
        "Edan",
        "Reagan",
        "Henry",
        "Caius",
        "Jane",
        "Guto",
        "Sonya",
        "Tyrese",
        "Johnny",
    ]
    index = int(input())

    # Type your code here.
    ```
    '''
with "LAB_10_9.py":
    names = [
        "Ryley",
        "Edan",
        "Reagan",
        "Henry",
        "Caius",
        "Jane",
        "Guto",
        "Sonya",
        "Tyrese",
        "Johnny",
    ]
    index = int(input())

    try:
        print(f"Name: {names[index]}")
    except IndexError as excpt:
        print(f"Exception! {excpt}")
        if index < 0:
            print(f"The closest name is: {names[0]}")
        else:
            print(f"The closest name is: {names[-1]}")



def yes():
    names = [
        "Ryley",
        "Edan",
        "Reagan",
        "Henry",
        "Caius",
        "Jane",
        "Guto",
        "Sonya",
        "Tyrese",
        "Johnny",
    ]
    index = int(input())

    try:
        print(f"Name: {names[index]}")
        # out: Name: Jane
        # out: Name: Tyrese
        # out: Name: Ryley
    except IndexError as excpt:
        print(f"Exception! {excpt}")
        # out: Exception! list index out of range
        # out: Exception! list index out of range
        # out: Exception! list index out of range
        if index < 0:
            print(f"The closest name is: {names[0]}")
            # out: The closest name is: Ryley
        else:
            print(f"The closest name is: {names[-1]}")
            # out: The closest name is: Johnny
            # out: The closest name is: Johnny
setin("5","12","-2","-15","0","10")
# val: None
for count in range(0,6):
    yes()
    # val: None
    # val: None
    # val: None
    # val: None
    # val: None
    # val: None

with "LAB_10_9.py" as Scratch:
    print(1)
    # out: 1
setin("5","12","-2","-15","0","10")
# val: None
with "LAB_10_9.py" as Scratch:
    names = [
        "Ryley",
        "Edan",
        "Reagan",
        "Henry",
        "Caius",
        "Jane",
        "Guto",
        "Sonya",
        "Tyrese",
        "Johnny",
    ]
    index = int(input())

    try:
        print(f"Name: {names[index]}")
        # out: Name: Jane
    except IndexError as excpt:
        print(f"Exception! {excpt}")
        if index < 0:
            print(f"The closest name is: {names[0]}")
        else:
            print(f"The closest name is: {names[-1]}")


with "temp.txt":
    5
    12
    -2
    -15
with bash:
    python3 LAB_10_9.py < temp.txt
    # out: Name: Jane

####################################################
1
# val: 1
2
# val: 2
##############################################################################
'''## 10.10 LAB: Simple integer division - multiple exception handlers

### LAB ACTIVITY: LAB: Simple integer division - multiple exception handlers

Write a program that reads integers user_num and div_num as input, and output the integer quotient (user_num divided by div_num). Use a try block to perform all the statements. Use an except block to catch any ZeroDivisionError as a variable and output "Zero Division Exception: " followed by the exception message from the variable. Use another except block to catch any ValueError caused by invalid input as a variable and output "Input Exception: " followed by the exception message from the variable.
Note: ZeroDivisionError is raised when a division by zero happens. ValueError is raised when a user enters a value of different data type than what is defined in the program. Do not include code to raise any exception in the program.
Ex: If the input of the program is:

```
15
3
```
the output of the program is:

```
5
```
Ex: If the input of the program is:

```
10
0
```
the output of the program is:

```
Zero Division Exception: integer division or modulo by zero
```
Ex: If the input of the program is:

```
15.5
5
```
the output of the program is:

```
Input Exception: invalid literal for int() with base 10: '15.5'
```

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `15\n3` | `5` | 2 |
| 2 | `15\n0` | `Zero Division Exception: integer division or modulo by zero` | 2 |
| 3 | `15.5\n5` | `Input Exception: invalid literal for int() with base 10: '15.5'` | 2 |
| 4 | `25\n0.5` | `Input Exception: invalid literal for int() with base 10: '0.5'` | 1 |
| 5 | `twenty\n5` | `Input Exception: invalid literal for int() with base 10: 'twenty'` | 1 |
| 6 | `0\n4` | `0` | 1 |
| 7 | `15\n0` | `Zero Division Exception: integer division or modulo by zero` | 1 |
*Total: 10 points*
# Type your code here.
'''


setin("15","3","15","0","15.5","5","25","0.5","twenty","5","0","4","15","0")
# val: None
with "LAB_10_10.py" as Scratch:
    try:
        user_num = int(input())
        div_num = int(input())
        print(user_num // div_num)
        # out: 5
    except ZeroDivisionError as excpt:
        print(f"Zero Division Exception: {excpt}")
    except ValueError as excpt:
        print(f"Input Exception: {excpt}")
##############################################################################
'''## 10.11 LAB: Step counter - exceptions 

### LAB ACTIVITY: LAB: Step counter - exceptions 

A pedometer treats walking 2,000 steps as walking 1 mile. Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. The steps_to_miles() function raises a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the steps_to_miles() function. Use a try-except block to catch any ValueError object raised by the steps_to_miles() function and output the exception message.
Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
`print(f'{your_value:.2f}')`
Ex: If the input of the program is:

```
5345
```
the output of the program is:

```
2.67
```
Ex: If the input of the program is:

```
-3850
```
the output of the program is:

```
Exception: Negative step count entered.
```

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `5345` | `2.67` | 2 |
| 2 | `-3850` | `Exception: Negative step count entered.` | 2 |
| 3 | `(none)` | `` | 3 |
| 4 | `(none)` | `` | 3 |
*Total: 10 points*
```python
# Define your method here


if __name__ == "__main__":
    # Type your code here.
```'''
setin("5345","-3850")
# val: None
with "LAB_10_11.py" as Scratch:
    def steps_to_miles(steps):
        if steps < 0:
            raise ValueError("Exception: Negative step count entered.")
        miles = steps / 2000
        return miles


    if __name__ == "__main__":
        try:
            steps = int(input())
            miles = steps_to_miles(steps)
            print(f'{miles:.2f}')
            # out: 2.67
        except ValueError as excpt:
            print(excpt)
setin("5345","-3850")
# val: None
##############################################################################
'''## 10.12 LAB: Student info not found - custom exception types

### LAB ACTIVITY: LAB: Student info not found - custom exception types

Given a main program that searches for the ID or the name of a student from a dictionary, complete the find_ID() and the find_name() functions that return the corresponding information of a student. Then, insert a try/except statement in main() to catch any exceptions raised by find_ID() or find_name(), and output the exception message. Each entry of the dictionary contains the name (key) and the ID (value) of a student.
Function find_ID() takes two parameters, a student's name and a dictionary. Function find_ID() returns the ID associated with the student's name if the name is in the dictionary. Otherwise, the function raises a custom exception type, StudentInfoError, with the message "Student ID not found for *studentName*", where *studentName* is the name of the student.
Function find_name() takes two parameters, a student's ID and a dictionary. Function find_name() returns the name associated with the student's ID if the ID is in the dictionary. Otherwise, the function raises a custom exception type, StudentInfoError, with the message "Student name not found for *studentID*", where *studentID* is the ID of the student.
The main program takes two inputs from a user: a user choice of finding the ID or the name of a student (int), and the ID or the name of a student (string). If the user choice is 0, find_ID() is invoked with the student's name as one of the arguments. If the user choice is 1, find_name() is invoked with the student's ID as one of the arguments. The main program finally outputs the result of the search or a message if an exception is caught.
Note: StudentInfoError is defined in the program as a custom exception type. StudentInfoError has an attribute to store an exception message.
Ex: If the input of the program is:

```
0
Reagan
```
and the contents of dictionary are:

```
'Reagan' : 'rebradshaw835',
'Ryley' : 'rbarber894',
'Peyton' : 'pstott885',
'Tyrese' : 'tmayo945',
'Caius' : 'ccharlton329'
```
the output of the program is:

```
rebradshaw835
```
Ex: If the input of the program is:

```
0
Mcauley
```
the program outputs an exception message:

```
Student ID not found for Mcauley
```
Ex: If the input of the program is:

```
1
rebradshaw835
```
the output of the program is:

```
Reagan
```
Ex: If the input of the program is:

```
1
mpreston272
```
the program outputs an exception message:

```
Student name not found for mpreston272
```

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `0\nReagan` | `rebradshaw835` | 1 |
| 2 | `0\nMcauley` | `Student ID not found for Mcauley` | 1 |
| 3 | `1\nrebradshaw835` | `Reagan` | 1 |
| 4 | `1\nmpreston272` | `Student name not found for mpreston272` | 1 |
| 5 | `(none)` | `` | 2 |
| 6 | `(none)` | `` | 2 |
| 7 | `(none)` | `` | 1 |
| 8 | `(none)` | `` | 1 |
*Total: 10 points*

```python# Define custom exception
class StudentInfoError(Exception):

    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    # Type your code here.
    
    
def find_name(ID, info):
    # Type your code here.


if __name__ == "__main__":
    # Dictionary of student names and IDs
    student_info = {
        "Reagan": "rebradshaw835",
        "Ryley": "rbarber894",
        "Peyton": "pstott885",
        "Tyrese": "tmayo945",
        "Caius": "ccharlton329",
    }

    userChoice = (
        input())  # Read search option from user. 0: find_ID(), 1: find_name()

    # FIXME: find_ID() and find_name() may raise an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    if userChoice == "0":
        name = input()
        result = find_ID(name, student_info)
    else:
        ID = input()
        result = find_name(ID, student_info)
    print(result)

      ```
    '''
setin("0","Reagan","0","Mcauley","1","rebradshaw835","1","mpreston272")
# val: None
with "LAB_10_12.py" as Scratch:
    class StudentInfoError(Exception):

        def __init__(self, message):
            self.message = message


    def find_ID(name, info):
        if name in info:
            return info[name]
        else:
            raise StudentInfoError(f"Student ID not found for {name}")


    def find_name(ID, info):
        for name, id in info.items():
            if id == ID:
                return name
        raise StudentInfoError(f"Student name not found for {ID}")


    if __name__ == "__main__":
        student_info = {
            "Reagan": "rebradshaw835",
            "Ryley": "rbarber894",
            "Peyton": "pstott885",
            "Tyrese": "tmayo945",
            "Caius": "ccharlton329",
        }

        userChoice = input()

        try:
            if userChoice == "0":
                name = input()
                result = find_ID(name, student_info)
            else:
                ID = input()
                result = find_name(ID, student_info)
            print(result)
            # out: rebradshaw835
        except StudentInfoError as excpt:
            print(excpt.message)
