## 10.1 Handling exceptions using try and except

Error-checking code is code that a programmer introduces to detect and handle errors that occur while the program executes. Python has special constructs known as exception-handling constructs because they handle exceptional circumstances, or errors, during execution.

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
> ```text
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
> ```text
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

When a try is reached, the statements in the try block are executed. If no exception occurs, the except block is skipped and the program continues. If an exception does occur, the except block is executed, and the program continues after the except block. Any statements in the try block not executed before the exception occurred are skipped.

### PARTICIPATION ACTIVITY: Exception basics.

**1.** Execution jumps to an except block only if an error occurs in the preceding try block.
Answer: **True**
Code that might produce an error, such as conversion of user input or container indexing operations, should often use exception-handling code.

**2.** After an error occurs in a try block, and the following except block has executed, execution resumes after the error in the try block.
Answer: **False**
Execution proceeds to the code that follows the except block; the code in the try block after the error is skipped.

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

[explanation]

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

[explanation]

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

[explanation]

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

[explanation]

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
If the input is not [...], the try block produces an exception. The except block handles the exception and outputs [...].

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
