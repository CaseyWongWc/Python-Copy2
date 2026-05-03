
with '''README.MD''':
  # zyBooks Chapter 10 (Sections 10.1–10.12)
  ---

  ## Checklist + scores

  | Section | Earned | Possible | Status | Notes |
  | --- | --- | --- | --- | --- |
  | --- | ---: | ---: | --- | --- |
  | 10.1 | 3 | 10 | ⏳ In progress | Participation: 10.1.1 (1/1), 10.1.2 (2/2). Challenges: 10.1.1 (0/4), 10.1.2 (0/3). |
  | 10.2 | 0 | 9 | ⬜ Not started | Participation: 10.2.1 (0/1), 10.2.2 (0/3). Challenges: 10.2.1 (0/3), 10.2.2 (0/2). |
  | 10.3 | 0 | 7 | ⬜ Not started | Participation: 10.3.1 (0/1). Challenges: 10.3.1 (0/4), 10.3.2 (0/2). |
  | 10.4 | 0 | 4 | ⬜ Not started | Participation: 10.4.1 (0/3). Challenge: 10.4.1 (0/1). |
  | 10.5 | 0 | 4 | ⬜ Not started | Participation: 10.5.1 (0/1), 10.5.2 (0/2). Challenge: 10.5.1 (0/1). |
  | 10.6 | 0 | 3 | ⬜ Not started | Participation: 10.6.1 (0/3). |
  | 10.7 | 0 | 10 | ⬜ Not started | Lab: 10.7.1 (0/10). |
  | 10.8 | 0 | 10 | ⬜ Not started | Lab: 10.8.1 (0/10). |
  | 10.9 | 0 | 10 | ⬜ Not started | Lab: 10.9.1 (0/10). |
  | 10.10 | 0 | 10 | ⬜ Not started | Lab: 10.10.1 (0/10). |
  | 10.11 | 0 | 10 | ⬜ Not started | Lab: 10.11.1 (0/10). |
  | 10.12 | 0 | 10 | ⬜ Not started | Lab: 10.12.1 (0/10). |

  ---

  ## Links

  - [Section 10.1](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/1)
  - [Section 10.2](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/2)
  - [Section 10.3](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/3)
  - [Section 10.4](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/4)
  - [Section 10.5](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/5)
  - [Section 10.6](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/6)
  - [Section 10.7](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/7)
  - [Section 10.8](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/8)
  - [Section 10.9](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/9)
  - [Section 10.10](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/10)
  - [Section 10.11](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/11)
  - [Section 10.12](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/12)
##############################################################################
with "S10_1/Section 10.1.MD":
    ## 10.1 Handling exceptions using try and except

  Error-checking code is code that a programmer introduces to detect and handle errors that occur while the program executes. Python has special constructs known as exception-handling constructs because they handle *exceptional circumstances*, or errors, during execution.

  Consider the following program in which a programmer enters weight and height. The program then outputs the corresponding body-mass index (BMI is one measure used to determine normal weight for a given height).

  > **BMI example without exception handling.**
  > ```python
  > user_input = ""
  > while user_input != "q":
  >     weight = int(input("Enter weight (in pounds): "))
  >     height = int(input("Enter height (in inches): "))
  > 
  >     bmi = (float(weight) / float(height * height)) * 703
  >     print(f"BMI: {bmi}")
  >     print("(CDC: 18.6-24.9 normal)\n")
  >     # Source www.cdc.gov
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
  > Traceback (most recent call last):
  >   File "test.py", line 3, in <module>
  >     weight = int(input("Enter weight (in pounds): "))
  > ValueError: invalid literal for int() with base 10: "One-hundred fifty"
  > ```

  Above, the user entered a weight by writing out "One-hundred fifty" instead of giving a number such as "150", which caused the int() function to produce an exception of type ValueError. The exception causes the program to terminate.

  A program should gracefully handle an exception and continue executing, instead of printing an error message and stopping completely. Code that potentially may produce an exception is placed in a try block. If the code in the try block causes an exception, then the code placed in a following except block is executed. Consider the program below, which modifies the BMI program to handle bad user input.

  > **BMI example with exception handling using try/except.**
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
  >     except:
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
  > Enter weight (in pounds): One-hundred fifty
  > Could not calculate health info.
  > 
  > Enter any key ("q" to quit): a
  > Enter weight (in pounds): 200
  > Enter height (in inches): 62
  > BMI: 36.57648283038502
  > (CDC: 18.6-24.9 normal)
  > 
  > Enter any key ("q" to quit): q
  > ```

  The try and except constructs are used together to implement exception handling, the process of responding to unexpected or unwanted events and errors during execution (handling exceptional conditions). A programmer could add additional code to do their own exception handling, such as checking if every character in the user input string is a digit, but such code would make the original program difficult to read.

  > **Basic exception-handling constructs.**

  ### PARTICIPATION ACTIVITY: How try and except blocks handle exceptions.

  Static figure:
  Begin Python code:
  try:
      ...
      x = int("Ten")  # Causes ValueError
      ...
  except:
      # Handle exception, e.g., print message
  ...
  End Python code. A monitor is shown with output "Error message...".

  Step 1: When a try is reached, the statements in the try block are executed. The program executes the try block until the line causing an exception is reached.

  Step 2: Any statements in the try block not executed before the exception occurred are skipped. The program executes the except block. "Error message..." appears and is shown on the monitor, then the program continues execution after the try and except block.

  When a try is reached, the statements in the try block are executed. If no exception occurs, the except block is skipped and the program continues. If an exception does occur, the except block is executed, and the program continues *after* the except block. Any statements in the try block not executed before the exception occurred are skipped.

  ### PARTICIPATION ACTIVITY: Exception basics.

  **1.** Execution jumps to an except block only if an error occurs in the preceding try block.
  Answer: **True**
  *Code that might produce an error, such as conversion of user input or container indexing operations, should often use exception-handling code.*

  **2.** After an error occurs in a try block, and the following except block has executed, execution resumes after the error in the try block.
  Answer: **False**
  *Execution proceeds to the code that follows the except block; the code in the try block after the error  is skipped.*

  > **Common exception types.**
  > | Type | Reason exception is raised |
  > | --- | --- |
  > | EOFError | input() hits an end-of-file condition (EOF) without reading any input. |
  > | KeyError | A dictionary key is not found in the set of keys. |
  > | ZeroDivisionError | Divide by zero error |
  > | ValueError | Invalid value (Ex: Input mismatch) |
  > | IndexError | Index is out of bounds. |
  > Source: Python: Built-in Exceptions

  ### CHALLENGE ACTIVITY: Handling exceptions using try and except.

  **Level 1:**

  What is the output?

  ```python
  try:
      number1 = int(input())
      print(number1 * [multiplier])

      number2 = int(input())
      print(number2 * [multiplier])
  except:
      print("x")
  print("e")
  ```

  *[explanation]*

  **Level 2:**

  What is the output?

  ```python
  user_input = input()
  while user_input != "q":
      try:
          number = int(user_input)
          print(number * [multiplier])
      except:
          print("x")
      user_input = input()
  print("e")
  ```

  *[explanation]*

  **Level 3:**

  What is the output?

  ```python
  user_input = input()
  while user_input != "q":
      try:
          number = int(user_input)
          print(number * [multiplier])
      except:
          print("x")
      user_input = input()
  print("e")
  ```

  *[explanation]*

  **Level 4:**

  What is the output?

  ```python
  user_input = input()
  try:
      while user_input != "q":
          number = int(user_input)
          print(number * [multiplier])
          user_input = input()
  except:
      print("x")
  print("e")
  ```

  *[explanation]*

  ### CHALLENGE ACTIVITY: Handling exceptions. (3 Levels)

  **Level 1:**

  **Task:**
  Add a try block that:
  - Reads [...] from input.
  - Outputs [...]

  **Explanation pattern:**
  In the try block:
  - input() reads in the next string from input. Then, int() converts the string into an integer. [...] is assigned with the integer returned by int(). An exception is produced by int() if the string returned by input() cannot be converted to an integer.
  - [...]

  **Code structure:**
  ```python
  # Your code goes here
  except:
      print(___)
  ```

  **Level 2:**

  **Task:**
  Add an except block to handle an exception and output [...].

  **Explanation pattern:**
  If the input is _not_ [...], the try block produces an exception. The except block handles the exception and outputs [...].

  **Code structure:**
  ```python
  try:
      ___ = int(input())
      ___
  # Your code goes here
  ```

  **Level 3:**

  **Task:**
  The while loop reads values from input until [...] read. Add an except block in the while loop to handle an exception and output [...].

  **Explanation pattern:**
  In the while loop: The try block reads the next value from input using input() and converts the value read to an integer using int(). If the value read can be converted to an integer, then:
  [...] Otherwise, if the input value cannot be converted to an integer, int() produces an exception. The except block handles the exception and outputs [...]. The while loop terminates after [...] read[...]

  **Code structure:**
  ```python
  ___

  while ___:
      try:
          ___ = int(input())
          ___
  # Your code goes here
  ```
##############################################################################
'''10.1 Handling exceptions using try and except
Error-checking code is code that a programmer introduces to detect and handle errors that occur while the program executes. Python has special constructs known as exception-handling constructs because they handle exceptional circumstances, or errors, during execution.

Consider the following program in which a programmer enters weight and height. The program then outputs the corresponding body-mass index (BMI is one measure used to determine normal weight for a given height).

Figure 10.1.1: BMI example without exception handling.
user_input = ""
while user_input != "q":
    weight = int(input("Enter weight (in pounds): "))
    height = int(input("Enter height (in inches): "))

    bmi = (float(weight) / float(height * height)) * 703
    print(f"BMI: {bmi}")
    print("(CDC: 18.6-24.9 normal)\n")
    # Source www.cdc.gov

    user_input = input('Enter any key ("q" to quit): ')
Enter weight (in pounds): 150
Enter height (in inches): 66
BMI: 24.207988980716255
(CDC: 18.6-24.9 normal)

Enter any key ("q" to quit): a
Enter weight (in pounds): One-hundred fifty
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    weight = int(input("Enter weight (in pounds): "))
ValueError: invalid literal for int() with base 10: "One-hundred fifty"

Feedback?
Above, the user entered a weight by writing out "One-hundred fifty" instead of giving a number such as "150", which caused the int() function to produce an exception of type ValueError. The exception causes the program to terminate.

A program should gracefully handle an exception and continue executing, instead of printing an error message and stopping completely. Code that potentially may produce an exception is placed in a try block. If the code in the try block causes an exception, then the code placed in a following except block is executed. Consider the program below, which modifies the BMI program to handle bad user input.

Figure 10.1.2: BMI example with exception handling using try/except.
user_input = ""
while user_input != "q":
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov
    except:
        print("Could not calculate health info.\n")

    user_input = input('Enter any key ("q" to quit): ')
Enter weight (in pounds): 150
Enter height (in inches): 66
BMI: 24.207988980716255
(CDC: 18.6-24.9 normal)

Enter any key ("q" to quit): a
Enter weight (in pounds): One-hundred fifty
Could not calculate health info.

Enter any key ("q" to quit): a
Enter weight (in pounds): 200
Enter height (in inches): 62
BMI: 36.57648283038502
(CDC: 18.6-24.9 normal)

Enter any key ("q" to quit): q

Feedback?
The try and except constructs are used together to implement exception handling, the process of responding to unexpected or unwanted events and errors during execution (handling exceptional conditions). A programmer could add additional code to do their own exception handling, such as checking if every character in the user input string is a digit, but such code would make the original program difficult to read.

Construct 10.1.1: Basic exception-handling constructs.
try:
    # ... Normal code that might produce errors
except: # Go here if *any* error occurs in try block
    # ... Exception handling code

Feedback?'''
####################################################
'''participation activity
10.1.2: Exception basics.
1)
Execution jumps to an except block only if an error occurs in the preceding try block.
2)
After an error occurs in a try block, and the following except block has executed, execution resumes after the error in the try block.

Feedback?'''
with "myfile.txt":
    1) Execution jumps to an except block only if an error occurs in the preceding try block.
        True
        Code that might produce an error, such as conversion of user input or container indexing operations, should often use exception-handling code.
    2) After an error occurs in a try block, and the following except block has executed, execution resumes after the error in the try block.
        False
        Execution proceeds to the code that follows the except block; the code in the try block after the error is skipped.
with Scratch as a:
    '''10.1.3: Handling exceptions using try and except.
    Level 1:
    What is the output?

    try:
        number1 = int(input())
        print(number1 * [multiplier])

        number2 = int(input())
        print(number2 * [multiplier])
    except:
        print("x")
    print("e")

    explanation

    Level 2:
    What is the output?

    user_input = input()
    while user_input != "q":
        try:
            number = int(user_input)
            print(number * [multiplier])
        except:
            print("x")
        user_input = input()
    print("e")

    explanation

    Level 3:
    What is the output?

    user_input = input()
    while user_input != "q":
        try:
            number = int(user_input)
            print(number * [multiplier])
        except:
            print("x")
        user_input = input()
    print("e")

    explanation

    Level 4:
    What is the output?

    user_input = input()
    try:
        while user_input != "q":
            number = int(user_input)
            print(number * [multiplier])
            user_input = input()
    except:
        print("x")
    print("e")

    explanation
    '''
    ####################################################
    '''challenge activity
10.1.1: Handling exceptions using try and except.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

try:
    number1 = int(input())
    print(number1 * 2)

    number2 = int(input())
    print(number2 * 2)
except:
    print("x")
print("e")
Input
3
G
Output
1
2
3
4'''
with Scratch as a:
    # in: 3
    # in: G
    try:
        number1 = int(input())
        # out: 3
        print(number1 * 2)
        # out: 6

        number2 = int(input())
        # out: G
        print(number2 * 2)
    except:
        print("x")
        # out: x
    print("e")    
    # out: e
a
# val: Scratch(number1=3)
3
# val: 3
with Scratch:
    # in: 3
    # in: G
    try:
        number1 = int(input())
        # out: 3
        print(number1 * 2)
        # out: 6

        number2 = int(input())
        # out: G
        print(number2 * 2)
    except:
        print("x")
        # out: x
    print("e")
    # out: e

####################################################
'''challenge activity
10.1.1: Handling exceptions using try and except.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

try:
    number1 = int(input())
    print(number1 * 3)

    number2 = int(input())
    print(number2 * 3)
except:
    print("x")
print("e")
Input
j
1
Output
1
2
3
4'''
with Scratch:
    # in: j
    # in: 1
    try:
        number1 = int(input())
        # out: j
        print(number1 * 3)

        number2 = int(input())
        print(number2 * 3)
    except:
        print("x")
        # out: x
    print("e")
    # out: e
####################################################
'''challenge activity
10.1.1: Handling exceptions using try and except.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

try:
    number1 = int(input())
    print(number1 * 3)

    number2 = int(input())
    print(number2 * 3)
except:
    print("x")
print("e")
Input
j
1
Output'''
# help
1
# val: 1
2
# val: 2
