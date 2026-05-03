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
    # out: Because he's the hero Gotham deserves,
    # out: but not the one it needs right now.
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
    # out: Enter age ('q' to quit): 6
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
        # out: Because he's the hero Gotham deserves,
        # out: but not the one it needs right now.
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
    # val: Because he's the hero Gotham deserves,
    # val: but not the one it needs right now.

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
        # out: Because he's the hero Gotham deserves,
        # out: but not the one it needs right now.
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
        # out: Because he's the hero Gotham deserves,
        # out: but not the one it needs right now.
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
# val: ['Ana', 'Discarded the invalid expiration month entered', 'Ben', 'Discarded the invalid expiration month entered', '5', 'Expiration month is 5', 'Processed one valid input value']
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
prompt = "Enter age ("q" to quit): "
user_input = input(prompt)
while user_input != "q":
      try:
            ages.append(int(user_input))
            user_input = input(prompt)
      

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
with Scratch as a:"test.py"
    print("1")
    # out: 1
1
# val: 1
2
# val: 2
   
# in: 5
# in: q
with Scratch as a:"CA_10_2_2_1.py"
    #in: 6
    #in: 3
    #in: 1
    #in: j
    #in: q
    ages = []
    prompt = "Enter age ('q' to quit): "
    user_input = input(prompt)
    while user_input != "q":
        try:
            ages.append(int(user_input))
            # val: None
            user_input = input(prompt)
        except:
            print("Unable to add age.")
            # out: Unable to add age.
            user_input = input(prompt)
    print(ages)
1
with Scratch as a:"CA_10_2_2_2.py"
    import my_lib
    try:
        result = my_lib.magic()
    except AttributeError:
        print("No magic() function in my_lib.")

with Scratch as a:"CA_10_2_2_3.py"
    import my_lib

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
