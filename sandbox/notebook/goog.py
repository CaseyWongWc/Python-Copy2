from py_compile import main

from Helpers.helpings import *

# Set True only when you explicitly want to test child-process behavior.
RUN_CHILD_MAIN = False


class _NotebookFallbackContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


# Keep editor/static analysis calm when the notebook preprocessor symbols
# are not available yet. The runner still rewrites these `with` blocks.
_ = _NotebookFallbackContext()
Scratch = _NotebookFallbackContext()

##############################################################################
'''## 14.1 Recursive functions

A function may call other functions, including calling itself. A function that calls itself is known as a recursive function. The following program illustrates.

### PARTICIPATION ACTIVITY: A recursive function example.

Static figure:
Begin Python code:
def count_down(count):
    if count == 0:
        print('Go')
    else:
        print(count)
        count_down(count-1)

count_down(2)
End Python code.
A box for the program's output is also shown.
Step 1: count_down is called and count = 2. At the bottom of the file, the function call count_down(2) is highlighted. The Python interpreter locates count_down's function definition, which reads def count_down(count):. The Python interpreter enters the function. First it reads the if statement, if count == 0:. Since count == 0 is false, the interpreter proceeds to the else branch. The interpreter reads the print statement, print(count), and prints 2 in the output box.
Step 2: count_down is recursively called and count = 1. The interpreter reads the second line in the else branch, containing the function call count_down(count-1). The value of count for this function call is 1. The interpreter goes back to the function definition. The interpreter reads the if statement, if count == 0:. Since count == 0 is false, the interpreter proceeds to the else branch and reads the print statement print(count). The interpreter prints 1 in the output box.
Step 3: count_down is recursively called and count = 0. In the else branch, the interpreter reads the function call count_down(count-1). The value of count for this function call is 0. The interpreter returns to the function definition and then to the if statement reading if count == 0:. This time, the condition count == 0 is true. The interpreter enters the if branch and reads the line print('Go!'). Go! is printed in the output box. The interpreter is done reading this program. A summary of the function calls is displayed. First, count_down() was called with count = 2 and 2 was printed. Then count_down() was called with count = 1 and 1 was printed. Finally, count_down() was called with count = 0 and Go! was printed.

This function is mostly useful for demonstrating recursion; counting down is easily done instead using a loop. Each call to count_down creates a new namespace for the local scope of the function. The script makes the first call to count_down(), creating a namespace with the count argument bound to the integer value 2. That first function call prints 2, and calls count_down() with an argument of 1. A new namespace is created again for the local variables in count_down()'s local scope with the count argument bound to the integer value 1. That second function call prints 1, and calls count_down() with an argument of 0. That third function call prints GO!, and then because count == 0 is true, returns. The second function call is then done so it returns. The first function call is then done so it returns. Finally, the script finishes.

### PARTICIPATION ACTIVITY: Recursive functions.

**1.** How many times is count_down() called if the script calls count_down(5)?
Answer: 6
*Hint: The calls will be with arguments 5, then 4, 3, 2, 1, and finally 0.*
*The first call count_down(5) is called in the script. Then count_down() calls itself with 4, then with 3, 2, 1, and finally 0. That last instance does not call again, but instead returns.*

**2.** How many times is count_down() called if the script calls count_down(0)?
Answer: 1
*Hint: After the first call, are there are additional calls?*
*Upon being called that first time, count_down() just prints "GO!" and returns.*

**3.** Is there a difference in how we define the parameters of a recursive versus non-recursive function? Answer yes or no.
Answer: no
*Hint: The recursion comes from the statements within the function.*
*Recursion occurs when a function's statements include a call to the function itself. There is no particular difference in how the parameters are defined.*

### CHALLENGE ACTIVITY: Calling a recursive function.

Write a statement that calls the recursive function backwards_alphabet() with input starting_letter. 

Sample output with input: "f"

```
f
e
d
c
b
a
```

**Given code:**
```python
def backwards_alphabet(curr_letter):
    if curr_letter == "a":
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = input()
```
'''
####################################################
'''participation activity
14.1.1: A recursive function example.'''
with _:
    with "main.py" as f:
        def count_down(count):
            if count == 0:            
                print('Go!')                  
                # out: Go!
            else:                        
                print(count)             
                # out: 2
                # out: 1
                count_down(count-1)        
                # val: None
                # val: None
                    
        count_down(2)    
        # val: None
        # f.out: 2
        # f.out: 1
        # f.out: Go!
    f.out
    # val: ['2', '1', 'Go!']

    with Scratch as f:
        '''
        # ⭐ val: 6
        count_down(5)
        # ⭐ val: None
        # ⭐f.out: 5
        # ⭐f.out: 4
        # ⭐f.out: 3
        # ⭐f.out: 2
        # ⭐f.out: 1
        # ⭐f.out: Go!
        '''     
        # in: 6
        if RUN_CHILD_MAIN:
            cmd("python","main.py")
    with Scratch as f:
        def count_down(count):
            if count == 0:            
                print('Go!')                  
                # out: Go!
                # out: Go!
                # out: Go!
            else:                        
                print(count)             
                # out: 5
                # out: 4
                # out: 3
                # out: 2
                # out: 1
                # out: 4
                # out: 3
                # out: 2
                # out: 1
                # out: 3
                # out: 2
                # out: 1
                count_down(count-1)        
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
        count_down(5),count_down(4),count_down(3)
        # val: (None, None, None)
        # f.out: 5
        # f.out: 4
        # f.out: 3
        # f.out: 2
        # f.out: 1
        # f.out: Go!
        # f.out: 4
        # f.out: 3
        # f.out: 2
        # f.out: 1
        # f.out: Go!
        # f.out: 3
        # f.out: 2
        # f.out: 1
        # f.out: Go!
####################################################
'''participation activity
14.1.2: Recursive functions.'''
with _:
    with "_.txt":
        '''
        1) How many times is count_down() called if the script calls count_down(5)?
        # ⭐ val: 6
        2) How many times is count_down() called if the script calls count_down(0)?
        # ⭐ val: 1
        3) Is there a difference in how we define the parameters of a recursive versus non-recursive function? Answer yes or no.
        # ⭐ val: no
        '''
    with Scratch as f:
        
        def count_down(count):
            count
            # val: 5
            # val: 4
            # val: 3
            # val: 2
            # val: 1
            # val: 0
            if count == 0:
                count            
                # val: 0
                print('Go!')                  
                # out: Go!
            else:
                count                        
                # out: 3
                # out: 250
                # out: Enter n: 4
                # out: 12
                # out: 4
                # out: 2
                # val: 5
                # val: 4
                # val: 3
                # val: 2
                # val: 1
                print(count)             
                # out: 5
                # out: 4
                # out: 3
                # out: 2
                # out: 1
                
                count_down(count-1)
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
                count        
                # val: 1
                # val: 2
                # val: 3
                # val: 4
                # val: 5
                    
        count_down(5)    
        # val: None
        # f.out: 5
        # f.out: 4
        # f.out: 3
        # f.out: 2
        # f.out: 1
        # f.out: Go!
####################################################
'''challenge activity
14.1.1: Calling a recursive function.
Write a statement that calls the recursive function backwards_alphabet() with input starting_letter.

Sample output with input: "f"
f
e
d
c
b
a
def backwards_alphabet(curr_letter):
    if curr_letter == "a":
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = input()

""" Your solution goes here """

'''

with _:
    with "main.py":

        def backwards_alphabet(curr_letter):
            if curr_letter == "a":
                print(curr_letter)
            else:
                print(curr_letter)
                prev_letter = chr(ord(curr_letter) - 1)
                backwards_alphabet(prev_letter)

        starting_letter = input()
        backwards_alphabet(starting_letter)

    with Scratch as f:
        # in: f
        def backwards_alphabet(curr_letter):
            curr_letter
            # val: f
            # val: e
            # val: d
            # val: c
            # val: b
            # val: a
            if curr_letter == "a":
                print(curr_letter)
                # out: a
            else:
                print(curr_letter)
                # out: f
                # out: e
                # out: d
                # out: c
                # out: b
                prev_letter = chr(ord(curr_letter) - 1)
                prev_letter
                # val: e
                # val: d
                # val: c
                # val: b
                # val: a
                backwards_alphabet(prev_letter)
                # val: None
                # val: None
                # val: None
                # val: None
                # val: None
        # in: f
        starting_letter = input()
        # out: f
        backwards_alphabet(starting_letter)
        # val: None
        # f.out: f
        # f.out: e
        # f.out: d
        # f.out: c
        # f.out: b
        # f.out: a
##############################################################################
'''## 14.2 Recursive algorithm: Search

An algorithm is a sequence of steps for solving a problem. For example, an algorithm for making lemonade is:

   - Make lemonade
      
      Add sugar to pitcher
      - Add lemon juice
      - Add water
      - Stir

Each step is distinct. Alternatively, an algorithm, for mowing the lawn is:

   - *Mow* the lawn
   
      *Mow* the frontyard
      
         *Mow* the left front
         - *Mow* the right front
      
      
      - *Mow* the backyard
      
         *Mow* the left back
         - *Mow* the right back
      
      
   
   

The mowing algorithm is defined *recursively*, i.e., the mowing algorithm's steps themselves consist of mowing, but of a smaller region.

Consider a guessing game program where a friend thinks of a number from 0-100 and you try to guess the number, with the friend telling you to guess higher or lower until you guess correctly. What algorithm would you use to minimize the number of guesses? An algorithm that simply guesses in increments of 1 -- Is it 0? Is it 1? Is it 2? -- requires too many guesses (50 on average). An algorithm that guesses by 10s and then by 1s -- Is it 10? Higher: Is it 20? Higher: Is it 30? Lower: Is it 21? 22? 23? -- does better but still requires about 10 guesses on average (5 to find the correct tens digit and 5 to guess the correct ones digit). An even better algorithm uses a binary search approach, guessing the midpoint of the range and halving the range after each guess -- Is it 50 (the middle of 0-100)? Lower: Is it 25 (the middle of 0-50)? Higher: Is it 38 (the middle of 26-50)? Lower: Is it 32 (the middle of 26-38). After each guess, the binary search algorithm is applied again, just on a smaller range, i.e., the algorithm is recursive. The following animation illustrates.

### PARTICIPATION ACTIVITY: Binary search: A well-known recursive algorithm.

Static figure: As asked above: Given numbers 0-100, find the number 32. Four number lines are shown, each with the midpoint marked.
Step 1: The midpoint of 0 and 100 is 50.  A number line from 0 to 100 is shown, with 50 marked in the middle. 
Step 2: 32 is lower than 50, so the window is halved and the midpoint of 0 and 50 is found. When the window is halved, a new number line shows the lower half of the previous number line, only the values from 0 to 50. The midpoint of 0 and 50 is 25.
Step 3: 32 is greater than 25, so the window is halved and the midpoint of 26 and 50 is found. When the window is halved, a new number line shows the upper half of the previous number line, with only the values from 26 to 50. The midpoint of 26 and 50 is 38, which is marked on the updated number line.
Step 4: 32 is less than 38, so the window is halved and the midpoint of 26 and 38, which is 32, is found. When the window is halved, a new number line shows the lower half of the previous number line, with only the values from 26 to 38. The midpoint of 26 and 38 is 32, the value being searched for.

A recursive function is a natural match for the recursive binary search algorithm. We can define a function find(low, high) whose parameters indicate the low and high sides of the guessing range. The function guesses at the midpoint of the range. If the user says lower, the function calls find(low, mid). If the user says higher, the function calls find(mid+1, high)Note_mid. The following program illustrates.

> **A recursive function find() carrying out a binary search algorithm.**
> ```python
> def find(low, high):
>     mid = (high + low) // 2  # Midpoint of low..high
>     answer  = input(f"Is it {mid}? (l/h/y): ")
> 
>     if (answer != "l") and (answer != "h"):  # Base case
>         print("Got it!")
>     else:
>         if answer == "l":
>             find(low, mid)
>         else:
>             find(mid+1, high)
> 
> print("Choose a number from 0 to 100.")
> print("Answer with:")
> print("   l (your num is lower)")
> print("   h (your num is higher)")
> print(" any other key (guess is right).")
> 
> find(0, 100)
> ```
> ```
> Choose a number from 0 to 100.
> Answer with:
>    l (your num is lower)
>    h (your num is higher)
>  any other key (guess is right).
> Is it 50? (l/h/y): l
> Is it 25? (l/h/y): h
> Is it 38? (l/h/y): h
> Is it 44? (l/h/y): l
> Is it 41? (l/h/y): y
> Got it!
> ```

The recursive function has an if-else statement, where the if branch is the end of the recursion, known as the base case. The else part has the recursive calls. Such an if-else pattern is quite common in recursive functions.

Consider the following program, in which a recursive algorithm is used to find an item in a sorted list. This example is for demonstration purposes only, a programmer would be better off using the list.index() or "in" operator to find a specific list element. Consider having a list of attendees at a conference, whose names have been stored in alphabetical order in a list. The following program determines whether a particular person is in attendance.

> **Recursively searching a sorted list.**
> ```python
> def find(lst, item, low, high):
>     """
>     Finds index of string in list of strings, else -1.
>     Searches only the index range low to high
>     Note: Upper/Lower case characters matter
>     """
>     range_size = (high - low) + 1
>     mid = (high + low) // 2
> 
>     if item == lst[mid]:  # Base case 1: Found at mid
>         pos = mid
>     elif range_size == 1:  # Base case 2: Not found
>         pos = -1
>     else:  # Recursive search: Search lower or upper half
>         if item < lst[mid]:  # Search lower half
>             pos = find(lst, item, low, mid)
>         else:  # Search upper half
>             pos = find(lst, item, mid+1, high)
> 
>     return pos
> 
> attendees = []
> 
> attendees.append("Adams, Mary")
> attendees.append("Carver, Michael")
> attendees.append("Domer, Hugo")
> attendees.append("Fredericks, Carlo")
> attendees.append("Li, Jie")
> 
> name = input("Enter person's name: Last, First: ")
> pos = find(attendees, name, 0, len(attendees)-1)
> 
> if pos >= 0:
>     print(f"Found at position {pos}.")
> else:
>     print("Not found.")
> ```
> ```
> Enter person's name: Last, First: Simpson, Homer
> Not found.
> ...
> Enter person's name: Last, First: Domer, Hugo
> Found at position 2.
> ```

The find() function restricts its search to elements within the range "low" to "high". The script passes a range encompassing the entire list, namely 0 to (list length - 1). find() compares to the middle element, returning that element's position if matching. If not matching, then find() checks if the window's size is just one element, returning -1 in that case to indicate the item was not found because there is nothing left to search in the window. If neither of those two base cases are satisfied, then find() uses recursive binary search, recursively searching either the lower or upper half of the range as appropriate. Use the below tool to step through execution of the above program.

**PythonTutor: Recursively searching a sorted list for Carver, Michael.**

```python
def find(lst, item, low, high):
    """
    Finds index of string in list of strings, else -1.
    Searches only the index range low to high
    Note: Upper/Lower case characters matter
    """
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]:  # Base case 1: Found at mid
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        pos = -1
    else:  # Recursive search: Search lower or upper half
        if item < lst[mid]:  # Search lower half
            pos = find(lst, item, low, mid)
        else:  # Search upper half
            pos = find(lst, item, mid+1, high)

    return pos

attendees = []

attendees.append("Adams, Mary")
attendees.append("Carver, Michael")
attendees.append("Domer, Hugo")
attendees.append("Fredericks, Carlo")
attendees.append("Li, Jie")

pos = find(attendees, "Carver, Michael", 0, len(attendees)-1)

if pos >= 0:
    print(f"Found at position {pos}.")
else:
    print("Not found.")
```

A function that recursively searches a sorted list.

In general, any recursive solution can also be done using loops. However, in some cases using a recursive algorithm may make a solution more clear, concise, and understandable. Candidates for recursion are problems that can be reduced into smaller and identical problems, and then solved. Above, the binary search algorithms iteratively reduced the problem by half, eventually reached a base case where the problem could be solved (i.e., the desired element was located).

### PARTICIPATION ACTIVITY: Recursive search algorithm.

**1.** If a sorted list has elements numbered 0 to 50 and the item being searched for happens to be at location 6, how many times will the find() function be called?
Answer: 3
*Hint: Calls include find(lst,item,0,25) and find(lst,item,0,12).*
*The first call is find(lst,item,0,50), which checks element (0+50)//2 = 25. The second is find(lst,item,0,25), which checks elements 12 (0+25)//2 = 12 (the fraction is truncated when using //). The third is find(lst,item,0,12), which checks element 6 and thus finds the element.*

**2.** If an alphabetically sorted list (ascending) has elements numbered 0 to 50, and the item at element 0 is "Bananas", how many recursive calls to find() will be made during the failed search for "Apples"?
Answer: 7
*Hint: Calls include find(lst,"Apples",0,50), find(lst,"Apples",0,25), find(lst,"Apples",0,12), find(lst,"Apples",0,6), find(lst,"Apples",0,3), find(lst,"Apples",0,1), and find(lst,"Apples",0,0)*
*The first call is find(lst,"Apples",0,50). The next calls are find(lst,"Apples",0,25), find(lst,"Apples",0,12), find(lst,"Apples",0,6), find(lst,"Apples",0,3), and find(lst,"Apples",0,1) whose mid is 0. Because Apples is less than the item at element 0 ("Bananas"), the next call is find (0,0). Because the range is now 1, the second base case is reached and the function returns -1.*

**3.** A list of 5 elements is: A B D E F. A is element 0 and F is element 4. find(lst,"C",0,4) is called to search for item C. Write the last call to find() that would occur when searching for item C.
Answer: find(lst, "C",2,2)
*Hint: The first call is find(lst,"C",0,4) and the second call is find(lst,"C",0,2). Then what?*
*find(lst,"C",0,4) checks lst[2]. D != C so the search proceeds left to find(lst,"C",0,2).

find(lst,"C",0,2) checks lst[1]. B != C so the search proceeds right to find(lst,"C",1+1, 2) or find(lst,"C",2,2).

Because D != C and the range is 1, find() concludes the item is not found and returns -1.*

### CHALLENGE ACTIVITY: Enter the output of binary search.

**Level 1:**

What is the output?

```python
def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("[equal char]")
    else:
        if number < mid_val:    # First recursive case
            print("[lower char]")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("[higher char]")
            find_number(number, mid_val + 1, high_val)

number = int(input())
find_number(number, 0, [maximum range])
```

*For input `0`, the program follows the first recursive case since 0 is less than mid_val. "[lower char]" is printed and the lower half is searched from low_val to mid_val.

When number equals mid_val, the base case is reached and "[equal char]" is printed.

Recursive function call outputs:
[output trace explanation]*

**Level 2:**

What is the output?

```python
def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("[equal char]")
    else:
        if number < mid_val:    # First recursive case
            print("[lower char]")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("[higher char]")
            find_number(number, mid_val + 1, high_val)

number = int(input())
find_number(number, 0, [maximum range])
```

*For input `[input value]`, the program follows the second recursive case since [input value] is greater than mid_val. "[higher char]" is printed and the upper half is searched from mid_val + 1 to high_val.

When number equals mid_val, the base case is reached and "[equal char]" is printed.

Recursive function call outputs:
[output trace explanation]*

**Level 3:**

What is the output?

```python
def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("[equal char]")
    else:
        if number < mid_val:    # First recursive case
            print("[lower char]")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("[higher char]")
            find_number(number, mid_val + 1, high_val)

number = int(input())
find_number(number, 0, [maximum range])
```

*For input `[input value]`, the program alternates between the recursive cases until the base case is reached.

Recursive function call outputs:
[output trace explanation]*

### CHALLENGE ACTIVITY: Searching for a letter.

Organize the lines of code to complete the recursive search() function.

Base case 1: If match_char is equal to mid_char, then output the value of match_char, " is found at index ", and the value of mid_index.
Base case 2: If range_size is equal to 1, then output the value of match_char, followed by " is not in the list".
Recursive case:

If match_char  is True, then search for match_char between lower_index and mid_index.
Otherwise, search for match_char between mid_index + 1 and upper_index.

**Solution:**
```python
def search(char_list, match_char, lower_index, upper_index):
    # Outputs the search range
    print("Searching range from index ", end="")
    print(f"{lower_index} to {upper_index}")

    range_size = (upper_index - lower_index) + 1
    mid_index = (lower_index + upper_index) // 2
    mid_char = char_list[mid_index]

    # Base case 1: match_char is equal to mid_char
    if match_char == mid_char:
    print(f"{match_char} is found at index {mid_index}")

    # Base case 2: range_size is equal to 1
    elif range_size == 1:
    print(f"{match_char} is not in the list")

    # Recursive case: Search lower or upper half
    else:
        if match_char < mid_char:
      search(char_list, match_char, lower_index, mid_index)
        else:
      search(char_list, match_char, mid_index + 1, upper_index)

match = input()
data_input = input().split()
search(data_input, match, 0, len(data_input) - 1)
```

### CHALLENGE ACTIVITY: Recursive algorithm: Search.

**Task:**
[...] and a list of alphabetically-sorted [...]s are read from input. [...]() is a recursive search function that finds the index of a target [...] within a list. Complete the [...]() function: If [...] evaluates to True, then recursively call [...]() to find [...] in the range from [...] to [...].
Otherwise, recursively call [...]() to find [...] in the range from [...] + 1 to [...].

**Explanation pattern:**
If the expression [...] evaluates to True, then [...]() is called with [...], [...], [...], and [...] as the arguments to look for [...] in the range between [...] and [...]. Otherwise, [...]() is called with [...], [...], [...] + 1, and [...] as the arguments to look for [...] in the range between [...] + 1 and [...].

**Code structure:**
```python
def ___(___, ___, ___, ___):
    range_size = (___ - ___) + 1
    ___ = (___ + ___) // 2
    ___ = ___[___]

    print(f"Searching range from index {___} to {___}")

    if ___ == ___:
        print(f"{___} is found at index {___}")
    elif range_size == 1:
        print(f"{___} is not in the list")
    else:
if ___ < ___:

            """ Your code goes here """

        else:

            """ Your code goes here """
___ = input()
data_list = input().split()
___(data_list, ___, 0, len(data_list) - 1)
```

(*Note_mid) Because mid has already been checked, it need not be part of the new window, so mid+1 rather than mid can be used for the window's new low side, or mid-1 for the window's new high side. But the mid-1 can have the drawback of a non-intuitive base case (i.e., mid < low, because if the current window is say 4..5, mid is 4, so the new window would be 4..4-1, or 4..3). We believe range==1 is more intuitive, and thus use mid rather than mid-1. However, we still have to use mid+1 when searching higher, due to integer rounding. In particular, for window 99..100, mid is 99 ((99+100)/2=99.5, rounded to 99 due to truncation of the fraction). So the next window would again be 99..100, and the algorithm would repeat with this window forever. mid+1 prevents the problem, and doesn't miss any numbers because mid was checked and thus need not be part of the window.
'''
####################################################
'''participation activity
14.2.1: Binary search: A well-known recursive algorithm.

'''
with _:
    with "main.py" as f:
        # in: l
        # in: h
        # in: h
        # in: l
        # in: y
        def find(low, high):
            mid = (high + low) // 2  # Midpoint of low..high
            mid
            # val: 50
            # val: 25
            # val: 38
            # val: 44
            # val: 41
            answer  = input(f"Is it {mid}? (l/h/y): ")
            # out: Is it 50? (l/h/y): l
            # out: Is it 25? (l/h/y): h
            # out: Is it 38? (l/h/y): h
            # out: Is it 44? (l/h/y): l
            # out: Is it 41? (l/h/y): y

            if (answer != "l") and (answer != "h"):  # Base case
                print("Got it!")
                # out: Got it!
            else:
                if answer == "l":
                    answer
                    # val: l
                    # val: l
                    (low, mid)
                    # val: (0, 50)
                    # val: (39, 44)
                    find(low, mid)
                    # val: None
                    # val: None
                    (low, mid)
                    # val: (39, 44)
                    # val: (0, 50)

                else:
                    answer
                    # val: h
                    # val: h
                    (mid+1, high)
                    # val: (26, 50)
                    # val: (39, 50)
                    find(mid+1, high)
                    # val: None
                    # val: None
                    (mid+1, high)
                    # val: (39, 50)
                    # val: (26, 50)


        print("Choose a number from 0 to 100.")
        # out: Choose a number from 0 to 100.
        print("Answer with:")
        # out: Answer with:
        print("   l (your num is lower)")
        # out:    l (your num is lower)
        print("   h (your num is higher)")
        # out:    h (your num is higher)
        print(" any other key (guess is right).")
        # out:  any other key (guess is right).

        find(0, 100)
        # val: None
        # f.out: Choose a number from 0 to 100.
        # f.out: Answer with:
        # f.out:    l (your num is lower)
        # f.out:    h (your num is higher)
        # f.out:  any other key (guess is right).
        # f.out: Got it!
####################################################
'''participation activity
14.2.2: Recursive search algorithm.'''
with _:
    with "_.txt":
        '''
        1) If a sorted list has elements numbered 0 to 50 and the item being searched for happens to be at location 6, how many times will the find() function be called?
        # ⭐ val: 3
        2) If an alphabetically sorted list (ascending) has elements numbered 0 to 50, and the item at element 0 is "Bananas", how many recursive calls to find() will be made during the failed search for "Apples"?
        # ⭐ val: 7
        3) A list of 5 elements is: A B D E F. A is element 0 and F is element 4. find(lst,"C",0,4) is called to search for item C. Write the last call to find() that would occur when searching for item C.
        # ⭐ val: find(lst, "C",2,2)
        '''
 
    with "main.py" as f:
            a=list(range(51))
            a
            # val: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
            def find(low, high):
                mid = (high + low) // 2  # Midpoint of low..high
                print(f"Searching range from index {low} to {high}")
                # out: Searching range from index 0 to 50
                # out: Searching range from index 0 to 25
                # out: Searching range from index 0 to 12
                if a[mid] == 6:
                    print(f"{6} is found at index {mid}")
                    # out: 6 is found at index 6
                elif (high - low) + 1 == 1:
                    print(f"{6} is not in the list")
                else:
                    if 6 < a[mid]:
                        find(low, mid)
                        # val: None
                        # val: None
                    else:
                        find(mid+1, high)
            find(0,50)
            # val: None
            # f.out: Searching range from index 0 to 50
            # f.out: Searching range from index 0 to 25
            # f.out: Searching range from index 0 to 12
            # f.out: 6 is found at index 6

    with "main.py" as f:
        a=list(map(str, range(51)))
        a[0] = "Bananas"
        a[1] = "Apples"
        a
        # val: ['Bananas', 'Apples', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
        #list map
        def find(low, high):
            mid = (high + low) // 2  # Midpoint of low..high
            print(f"Searching range from index {low} to {high}")
            # out: Searching range from index 0 to 50
            # out: Searching range from index 26 to 50
            # out: Searching range from index 39 to 50
            # out: Searching range from index 45 to 50
            # out: Searching range from index 48 to 50
            # out: Searching range from index 50 to 50
            if a[mid] == "Apples":
                print(f"{'Apples'} is found at index {mid}")
            elif (high - low) + 1 == 1:
                print(f"{'Apples'} is not in the list")
                # out: Apples is not in the list
            else:
                if "Apples" < a[mid]:
                    find(low, mid)
                else:
                    find(mid+1, high)
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
        find(0,50)
        # val: None
        # f.out: Searching range from index 0 to 50
        # f.out: Searching range from index 26 to 50
        # f.out: Searching range from index 39 to 50
        # f.out: Searching range from index 45 to 50
        # f.out: Searching range from index 48 to 50
        # f.out: Searching range from index 50 to 50
        # f.out: Apples is not in the list
    print(50/2,25,12,6,3,1)
    # out: 25.0 25 12 6 3 1
    with "main.py" as f:
        a=["A", "B", "D", "E", "F"]
        a
        # val: ['A', 'B', 'D', 'E', 'F']
        def find(lst, item, low, high):
            mid = (high + low) // 2  # Midpoint of low..high
            print(f"Searching range from index {low} to {high}")
            # out: Searching range from index 0 to 4
            # out: Searching range from index 0 to 2
            # out: Searching range from index 2 to 2
            if lst[mid] == item:
                print(f"{item} is found at index {mid}")
            elif (high - low) + 1 == 1:
                print(f"{item} is not in the list")
                # out: C is not in the list
            else:
                if item < lst[mid]:
                    find(lst, item, low, mid)
                    # val: None
                else:
                    find(lst, item, mid+1, high)
                    # val: None
            (lst, item, low, high)
            # val: (['A', 'B', 'D', 'E', 'F'], 'C', 2, 2)
            # val: (['A', 'B', 'D', 'E', 'F'], 'C', 0, 2)
            # val: (['A', 'B', 'D', 'E', 'F'], 'C', 0, 4)
        find(a, "C", 0, 4)
        # val: None
        # f.out: Searching range from index 0 to 4
        # f.out: Searching range from index 0 to 2
        # f.out: Searching range from index 2 to 2
        # f.out: C is not in the list
    f
    # val: Scratch(a=['A', 'B', 'D', 'E', 'F'], find=<function __sc_14__.<locals>.__sc_13__.<locals>.find at 0x7fa5c1206a20>, out=['Searching range from index 0 to 4', 'Searching range from index 0 to 2', 'Searching range from index 2 to 2', 'C is not in the list'], err=[], outs='Searching range from index 0 to 4\nSearching range from index 0 to 2\nSearching range from index 2 to 2\nC is not in the list')
####################################################
'''Figure 14.2.2: Recursively searching a sorted list.'''
with _:
    with "main.py" as f:
        # in: Carver, Michael
        def find(lst, item, low, high):
            """
            Finds index of string in list of strings, else -1.
            Searches only the index range low to high
            Note: Upper/Lower case characters matter
            """
            range_size = (high - low) + 1
            mid = (high + low) // 2
            mid_item = lst[mid]

            if item == mid_item:  # Base case 1: Found at mid
                pos = mid
            elif range_size == 1:  # Base case 2: Not found
                pos = -1
            else:  # Recursive search: Search lower or upper half
                if item < mid_item:  # Search lower half
                    pos = find(lst, item, low, mid)
                else:  # Search upper half
                    pos = find(lst, item, mid+1, high)

            return pos

        attendees = []

        attendees.append("Adams, Mary")
        # val: None
        attendees.append("Carver, Michael")
        # val: None
        attendees.append("Domer, Hugo")
        # val: None
        attendees.append("Fredericks, Carlo")
        # val: None
        attendees.append("Li, Jie")
        # val: None

        name = input("Enter person's name: Last, First: ")
        # out: Enter person's name: Last, First: Carver, Michael
        pos = find(attendees, name, 0, len(attendees)-1)
        if pos >= 0:
            print(f"Found at position {pos}.")
            # out: Found at position 1.
        else:
            print("Not found.")
            # f.out: Found at position 1.
##############################################################################

'''challenge activity
14.2.1: Enter the output of binary search.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("a")
    else:
        if number < mid_val:    # First recursive case
            print("b")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("c")
            find_number(number, mid_val + 1, high_val)


number = int(input())
find_number(number, 0, 10)
Input
1
Output

'''

with _:
    
    with "_.txt":
        '''
        Level 1: What is the output?
        # ⭐ val: 1 5 c1 0 b1 0 a
        Level 2: What is the output?
        # ⭐ val: [input value] [mid_val] [higher char/lower char] [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [equal char]
        Level 3: What is the output?
        # ⭐ val: [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [equal char]
        '''
    with "scratch.txt":
        '''
        1 5 b
        1 2 b
        1 1 a
        '''
    # in: 1
    with "main.py":

        def find_number(number, low_val, high_val):
            mid_val = (high_val + low_val) // 2
            print(f"{number} {mid_val}", end=" ")

            if number == mid_val:       # Base case
                print("g")
            else:
                if number < mid_val:    # First recursive case
                    print("h")
                    find_number(number, low_val, mid_val)
                else:                   # Second recursive case
                    print("i")
                    find_number(number, mid_val + 1, high_val)


        number = int(input())
        find_number(number, 0, 12)
    f.out
    with open("1.txt", "w") as f1:
        f1.write(f"{f.out}")
        # !err: NameError: name 'f' is not defined
        # !err:   at line 798: a=list(range(51))

####################################################

'''challenge activity
14.2.1: Enter the output of binary search.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("m")
    else:
        if number < mid_val:    # First recursive case
            print("n")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("p")
            find_number(number, mid_val + 1, high_val)


number = int(input())
find_number(number, 0, 12)
Input
11
Outputchallenge activity
14.2.1: Enter the output of binary search.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("m")
    else:
        if number < mid_val:    # First recursive case
            print("n")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("p")
            find_number(number, mid_val + 1, high_val)


number = int(input())
find_number(number, 0, 12)
Input
11
Output'''
with _:
    with "_.txt":
        '''
        Level 1: What is the output?
        # ⭐ val: 11 6 p11 9 p11 11 m
        Level 2: What is the output?
        # ⭐ val: [input value] [mid_val] [higher char/lower char] [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [equal char]
        '''
    with "scratch.txt":
        '''
        11 6 p
        11 9 p
        11 11 m
        '''
    # in: 11
    with "main.py" as f:
        def find_number(number, low_val, high_val):
            mid_val = (high_val + low_val) // 2
            print(f"{number} {mid_val}", end=" ")
            # out: 11 6 
            # out: 11 9 
            # out: 11 11 

            if number == mid_val:       # Base case
                print("m")
                # out: m
            else:
                if number < mid_val:    # First recursive case
                    print("n")
                    find_number(number, low_val, mid_val)
                else:                   # Second recursive case
                    print("p")
                    # out: p
                    # out: p
                    find_number(number, mid_val + 1, high_val)
                    # val: None
                    # val: None

        number = int(input())
        # out: 11
        find_number(number, 0, 12)
        # val: None
        # f.out: 11 6 
        # f.out: p
        # f.out: 11 9 
        # f.out: p
        # f.out: 11 11 
        # f.out: m
    f.out
    # val: ['11 6 ', 'p', '11 9 ', 'p', '11 11 ', 'm']
    with open("1.txt", "w") as f1:
        f1.write(f"{f.out}")
        # val: 43
####################################################

'''challenge activity
14.2.1: Enter the output of binary search.
712910.5105864.qx3zqy7
Jump to level 1
Type the program's output

def find_number(number, low_val, high_val):
    mid_val = (high_val + low_val) // 2
    print(f"{number} {mid_val}", end=" ")

    if number == mid_val:       # Base case
        print("g")
    else:
        if number < mid_val:    # First recursive case
            print("h")
            find_number(number, low_val, mid_val)
        else:                   # Second recursive case
            print("i")
            find_number(number, mid_val + 1, high_val)


number = int(input())
find_number(number, 0, 12)
Input
5
Output
5 6 h
5 3 i
5 5 g


'''
with _:
    with "_.txt":
        '''
        Level 1: What is the output?
        # ⭐ val: 5 6 h5 3 i5 5 g
        Level 2: What is the output?
        # ⭐ val: [input value] [mid_val] [higher char/lower char] [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [equal char]
        Level 3: What is the output?
        # ⭐ val: [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [higher char/lower char] ... [input value] [mid_val] [equal char]
        '''
    with "scratch.txt":
       ''' 
        5 6 h
        5 3 i
        5 5 g
        '''
    # in: 5
    with "main.py" as f:
        def find_number(number, low_val, high_val):
            mid_val = (high_val + low_val) // 2
            print(f"{number} {mid_val}", end=" ")
            # out: 5 6 
            # out: 5 3 
            # out: 5 5 

            if number == mid_val:       # Base case
                print("g")
                # out: g
            else:
                if number < mid_val:    # First recursive case
                    print("h")
                    # out: h
                    find_number(number, low_val, mid_val)
                    # val: None
                else:                   # Second recursive case
                    print("i")
                    # out: i
                    find_number(number, mid_val + 1, high_val)
                    # val: None


        number = int(input())
        # out: 5
        find_number(number, 0, 12)
        # val: None
        number = int(input())
        # out: c
        find_number(number, 0, 10)
        # f.out: 5 6 
        # f.out: h
        # f.out: 5 3 
        # f.out: i
        # f.out: 5 5 
        # f.out: g
        # !err: ValueError: invalid literal for int() with base 10: 'c'
        # !err:   at line 959: def find_number(number, low_val, high_val):
    f.out
    # val: ['5 6 ', 'h', '5 3 ', 'i', '5 5 ', 'g']
    with open("1.txt", "w") as f1:
        f1.write(f"{f.out}")
        # val: 39
####################################################
'''challenge activity

## 

14.2.2: Searching for a letter.

_fullscreen_

Full screen

712910.5105864.qx3zqy7

Organize the lines of code to complete the recursive search() function.

-   Base case 1: If match\_char is equal to mid\_char, then output the value of match\_char, " is found at index ", and the value of mid\_index.
-   Base case 2: If range\_size is equal to 1, then output the value of match\_char, followed by " is not in the list".
-   Recursive case:
    -   If `match_char < mid_char` is True, then search for match\_char between lower\_index and mid\_index.
    -   Otherwise, search for match\_char between mid\_index + 1 and upper\_index.

**Click here for descriptions of variables in search()**

-   char\_list is the list of characters being searched.
-   match\_char is the character being searched for.
-   lower\_index and upper\_index are the current lower and upper bounds of the search range.
-   mid\_index is the middle index between lower\_index and upper\_index.
-   range\_size is the number of elements in the search range.
-   mid\_char is the element at index mid\_index of char\_list.

**Click here for example**

Ex: If the input is:  
`c`  
`c h o p s`  

then the output is:  

`Searching range from index 0 to 4`  
`Searching range from index 0 to 2`  
`Searching range from index 0 to 1`  
`c is found at index 0`

_keyboard\_arrow\_down_.

'''
with bash:
    cat main2.py
with _:
    #in: c
    #in: c h o p s
    with "main.py" as f:
        def search(char_list, match_char, lower_index, upper_index):
            range_size = (upper_index - lower_index) + 1
            mid_index = (lower_index + upper_index) // 2
            mid_char = char_list[mid_index]

            print(f"Searching range from index {lower_index} to {upper_index}")
            # out: Searching range from index 0 to 0
            print(f"{lower_index} to {upper_index}")
            # out: 0 to 0
            if match_char == mid_char:
                print(f"{match_char} is found at index {mid_index}")
            elif range_size == 1:
                print(f"{match_char} is not in the list")
                # out: c h o p s is not in the list
            else:
                if match_char < mid_char:
                    search(char_list, match_char, lower_index, mid_index)
                else:
                    search(char_list, match_char, mid_index + 1, upper_index)

        match = input()
        # out: c h o p s
        data_input = input().split()
        # out: c
        search(data_input, match, 0, len(data_input) - 1)
        # val: None
        # f.out: Searching range from index 0 to 0
        # f.out: 0 to 0
        # f.out: c h o p s is not in the list
    #in: c
    #in: c h o p s
    with "main2.py" as f:
        def search(char_list, match_char, lower_index, upper_index):  
            # Outputs the search range
            print("Searching range from index ", end="")
            # out: Searching range from index 
            print(f"{lower_index} to {upper_index}")
            # out: 0 to 0
                    
            range_size = (upper_index - lower_index) + 1
            mid_index = (lower_index + upper_index) // 2
            mid_char = char_list[mid_index]

            # Base case 1: match_char is equal to mid_char
            if match_char == mid_char:
                print(f"{match_char} is found at index {mid_index}")

            # Base case 2: range_size is equal to 1
            elif range_size == 1:
                print(f"{match_char} is not in the list")
                # out: c h o p s is not in the list

            # Recursive case: Search lower or upper half
            else:
                if match_char < mid_char:
                    search(char_list, match_char, lower_index, mid_index)
                else:
                    search(char_list, match_char, mid_index + 1, upper_index)


        match = input()
        # out: c h o p s
        data_input = input().split()
        # out: ARM
        search(data_input, match, 0, len(data_input) - 1)
        # val: None
        # f.out: Searching range from index 
        # f.out: 0 to 0
        # f.out: c h o p s is not in the list

##########################
#make_file("main2.py")
#⏳ val: PosixPath('/workspaces/Python-Copy2/sandbox/files/main2.py')
##########################
####################################################
'''challenge activity
14.2.3: Recursive algorithm: Search.
712910.5105864.qx3zqy7

Generate new problem
String inquired_item and a list of alphabetically-sorted strings are read from input. search() is a recursive search function that finds the index of a target string within a list. Complete the search() function:

If inquired_item < mid_value evaluates to True, then recursively call search() to find inquired_item in the range from start_index to mid_index.
Otherwise, recursively call search() to find inquired_item in the range from mid_index + 1 to end_index.
Click here for example
Ex: If the input is:
ARM
ARM BFA CHN MLI VEN VNM
then the output is:

Searching range from index 0 to 5
Searching range from index 0 to 2
Searching range from index 0 to 1
ARM is found at index 0
def search(nations_list, inquired_item, start_index, end_index):
    range_size = (end_index - start_index) + 1
    mid_index = (start_index + end_index) // 2
    mid_value = nations_list[mid_index]

    print(f"Searching range from index {start_index} to {end_index}")

    if inquired_item == mid_value:
        print(f"{inquired_item} is found at index {mid_index}")
    elif range_size == 1:
        print(f"{inquired_item} is not in the list")
    else:

        if inquired_item < mid_value:

            """ Your code goes here """

        else:

            """ Your code goes here """


inquired_item = input()
data_list = input().split()
search(data_list, inquired_item, 0, len(data_list) - 1)
'''

with Scratch:
    # in: ARM
    # in: ARM BFA CHN MLI VEN VNM
    with "main.py" as f:
        def search(nations_list, inquired_item, start_index, end_index):
            range_size = (end_index - start_index) + 1
            mid_index = (start_index + end_index) // 2
            mid_value = nations_list[mid_index]

            print(f"Searching range from index {start_index} to {end_index}")
            # out: Searching range from index 0 to 0

            if inquired_item == mid_value:
                print(f"{inquired_item} is found at index {mid_index}")
            elif range_size == 1:
                print(f"{inquired_item} is not in the list")
                # out: ARM BFA CHN MLI VEN VNM is not in the list
            else:

                if inquired_item < mid_value:

                    search(nations_list, inquired_item, start_index, mid_index)

                else:

                    search(nations_list, inquired_item, mid_index + 1, end_index)


        inquired_item = input()
        # out: ARM BFA CHN MLI VEN VNM
        data_list = input().split()
        # out: ARM
        search(data_list, inquired_item, 0, len(data_list) - 1)
        # val: None
        # f.out: Searching range from index 0 to 0
        # f.out: ARM BFA CHN MLI VEN VNM is not in the list
    # in: ARM
    # in: ARM BFA CHN MLI VEN VNM
    with "my turn to copy you.py":
            def search(nations_list, inquired_item, start_index, end_index):
                range_size = (end_index - start_index) + 1
                mid_index = (start_index + end_index) // 2
                mid_value = nations_list[mid_index]
                
                print(f"Searching range from index {start_index} to {end_index}")

                if inquired_item == mid_value:
                    print(f"{inquired_item} is found at index {mid_index}")
                elif range_size == 1:
                    print(f"{inquired_item} is not in the list")
                else:
                    
                    if inquired_item < mid_value:

                        search(nations_list, inquired_item, start_index, mid_index)

                    else:

                        search(nations_list, inquired_item, mid_index + 1, end_index)
            inquired_item = input()
            data_list = input().split()
            search(data_list, inquired_item, 0, len(data_list) - 1)
remove_path("my turn to copy you.py")
# val: PosixPath('/home/runner/workspace/sandbox/files/my turn to copy you.py')
##############################################################################
'''## 14.3 Adding output statements for debugging

Recursive functions can be particularly challenging to debug. Adding output statements can be helpful. Furthermore, an additional trick is to indent the print statements to show the current depth of recursion. The following program adds a parameter indent to a find() function that searches a sorted list for an item. All of the find() function's print statements start with "print indent, ...". The indent variable is typically some number of spaces. The script sets indent to three spaces "   ". Each recursive call *adds* three more spaces. Note how the output now clearly shows the recursion depth.
### Figure 14.3.1: Output statements can help debug recursive functions, especially if indented based on recursion depth.
> **Output statements can help debug recursive functions, especially if indented based on recursion depth.**
> ```python
> def find(lst, item, low, high, indent):
>     """
>     Finds index of string in list of strings, else -1.
>     Searches only the index range low to high
>     Note: Upper/Lower case characters matter
>     """
>     print(f"{indent} find() range {low} {high}")
>     range_size = (high - low) + 1
>     mid = (high + low) // 2
> 
>     if item == lst[mid]:  # Base case 1: Found at mid
>         print(f"{indent} Found person.")
>         pos = mid
>     elif range_size == 1:  # Base case 2: Not found
>         print(f"{indent} Person not found.")
>         pos = -1
>     else:  # Recursive search: Search lower or upper half
>         if item < lst[mid]:  # Search lower half
>             print(f"{indent} Searching lower half.")
>             pos = find(lst, item, low, mid, indent + '   ')
>         else:  # Search upper half
>             print(f"{indent} Searching upper half.")
>             pos = find(lst, item, mid+1, high, indent + "   ")
> 
>     print(f"{indent} Returning pos = {pos}.")
>     return pos
> 
> attendees = []
> 
> attendees.append("Adams, Mary")
> attendees.append("Carver, Michael")
> attendees.append("Domer, Hugo")
> attendees.append("Fredericks, Carlo")
> attendees.append("Li, Jie")
> 
> name = input("Enter person's name: Last, First: ")
> pos = find(attendees, name, 0, len(attendees)-1, "   ")
> 
> if pos >= 0:
>     print(f"Found at position {pos}.")
> else:
>     print("Not found.")
> ```
> ```
> Enter person's name: Last, First: Meeks, Stan
>     find() range 0 4
>     Searching upper half.
>        find() range 3 4
>        Searching upper half.
>           find() range 4 4
>           Person not found.
>           Returning pos = -1.
>        Returning pos = -1.
>     Returning pos = -1.
> Not found.
> ...
> Enter person's name: Last, First: Adams, Mary
>     find() range 0 4
>     Searching lower half.
>        find() range 0 2
>        Searching lower half.
>           find() range 0 1
>           Found person.
>           Returning pos = 0.
>        Returning pos = 0.
>     Returning pos = 0.
> Found at position 0.
> ```

Some programmers like to leave the output statements in the code, commenting them out with "#" when not in use. The statements actually serve as a form of comment. More advanced techniques for handling debug output exist too, such as the *logging* Python standard library (beyond this section's scope).

### LAB ACTIVITY: Output statements in a recursive function.
#### Try 14.3.1: Output statements in a recursive function.
Run the recursive find program having the output statements for debugging, searching for "Aaron, Joe", and observe the correct output indicating the person is not found. Next, introduce an error in the algorithm by changing "pos = -1" to "pos = 0" in the base case where the person is not found. Run the program again and notice how the indented print statements helps you isolate the error; in particular, note how the "Person not found" output is followed by "Returning pos = 0", which may lead one to realize the wrong value is being returned. Try instead introducing different errors and seeing how the indented print statements might help.

### PARTICIPATION ACTIVITY: Recursive function debug statements.
participation activity
14.3.1: Recursive function debug statements.
**1.** The above debug approach requires an extra parameter be passed to indicate the amount of indentation.
Answer: **True**
*Each recursive call adds a few spaces to the indent amount.*

**2.** Each recursive call should add a few spaces to the indent parameter.
Answer: **True**
*Those extra spaces cause the additional indenting.*

**3.** The function should remove a few spaces from the indent parameter before returning.
Answer: **False**
*The calling function added spaces to a new string object (since strings are immutable), so no removal of spaces is needed upon returning because the calling function still has the original indent string.*'''
####################################################
'''Figure 14.3.1: Output statements can help debug recursive functions, especially if indented based on recursion depth.'''
with _:
    # in: Meeks, Stan
    with "main.py" as f:
        def find(lst, item, low, high, indent):
            print(f"{indent} find() range {low} {high}")
            # out:     find() range 0 4
            # out:        find() range 3 4
            # out:           find() range 4 4
            range_size = (high - low) + 1
            mid = (high + low) // 2

            if item == lst[mid]:  # Base case 1: Found at mid
                print(f"{indent} Found person.")
                pos = mid
            elif range_size == 1:  # Base case 2: Not found
                print(f"{indent} Person not found.")
                # out:           Person not found.
                pos = -1
            else:  # Recursive search: Search lower or upper half
                if item < lst[mid]:  # Search lower half
                    print(f"{indent} Searching lower half.")
                    pos = find(lst, item, low, mid, indent + '   ')
                else:  # Search upper half
                    print(f"{indent} Searching upper half.")
                    # out:     Searching upper half.
                    # out:        Searching upper half.
                    pos = find(lst, item, mid+1, high, indent + "   ")

            print(f"{indent} Returning pos = {pos}.")
            # out:           Returning pos = -1.
            # out:        Returning pos = -1.
            # out:     Returning pos = -1.
            return pos

        attendees = []

        attendees.append("Adams, Mary")
        # val: None
        attendees.append("Carver, Michael")
        # val: None
        attendees.append("Domer, Hugo")
        # val: None
        attendees.append("Fredericks, Carlo")
        # val: None
        attendees.append("Li, Jie")
        # val: None

        name = input("Enter person's name: Last, First: ")
        # out: Enter person's name: Last, First: Meeks, Stan
        pos = find(attendees, name, 0, len(attendees)-1, "   ")

        if pos >= 0:
            print(f"Found at position {pos}.")
        else:
            print("Not found.")
            # out: Not found.
            # f.out:     find() range 0 4
            # f.out:     Searching upper half.
            # f.out:        find() range 3 4
            # f.out:        Searching upper half.
            # f.out:           find() range 4 4
            # f.out:           Person not found.
            # f.out:           Returning pos = -1.
            # f.out:        Returning pos = -1.
            # f.out:     Returning pos = -1.
            # f.out: Not found.
    # in: Adams, Mary
    with Scratch as f:
        #f
        #temporary = f.copy()
        #temporary.attendees = ['Adams, Mary', '_Carver, Michael', 'Domer, Hugo', '_Fredericks, Carlo', 'Li, Jie']
        #temporary.name = 'Adams, Mary'
        #temporary.pos = 0
        #temporary.find = find
        #f = temporary
        #f

        for hidden in range(len(f.out)):
            print(f"{hidden} {f.out[hidden]}")
            # out: 0     find() range 0 4
            # out: 1     Searching upper half.
            # out: 2        find() range 3 4
            # out: 3        Searching upper half.
            # out: 4           find() range 4 4
            # out: 5           Person not found.
            # out: 6           Returning pos = -1.
            # out: 7        Returning pos = -1.
            # out: 8     Returning pos = -1.
            # out: 9 Not found.
        from enum import Enum, auto 
        auto_enum = Enum('auto_enum', ' '.join([f"val{num}" for num in range(len(f.out))]))
        #for hidden in range(len(f.out)):
        #    print(f"{auto_enum(f'val{hidden}')} {f.out[hidden]}")
        for hidden in range(len(f.out)):
            Auto = Enum("Auto", [f"VAL{i}" for i in range(len(f.out))])
            print(Auto[f"VAL{hidden}"], f.out[hidden])
            # out: Auto.VAL0     find() range 0 4
            # out: Auto.VAL1     Searching upper half.
            # out: Auto.VAL2        find() range 3 4
            # out: Auto.VAL3        Searching upper half.
            # out: Auto.VAL4           find() range 4 4
            # out: Auto.VAL5           Person not found.
            # out: Auto.VAL6           Returning pos = -1.
            # out: Auto.VAL7        Returning pos = -1.
            # out: Auto.VAL8     Returning pos = -1.
            # out: Auto.VAL9 Not found.
        
        def find(lst, item, low, high, indent):
            print(f"{indent} find() range {low} {high}")
            # out:     find() range 0 4
            # out:        find() range 0 2
            # out:           find() range 0 1
            range_size = (high - low) + 1
            mid = (high + low) // 2
        

            if item == lst[mid]:  # Base case 1: Found at mid
                print(f"{indent} Found person.")
                # out:           Found person.
                pos = mid
            elif range_size == 1:  # Base case 2: Not found
                print(f"{indent} Person not found.")
                pos = -1
            else:  # Recursive search: Search lower or upper half
                if item < lst[mid]:  # Search lower half
                    print(f"{indent} Searching lower half.")
                    # out:     Searching lower half.
                    # out:        Searching lower half.
                    pos = find(lst, item, low, mid, indent + '   ')
                else:  # Search upper half
                    print(f"{indent} Searching upper half.")
                    pos = find(lst, item, mid+1, high, indent + "   ")

            print(f"{indent} Returning pos = {pos}.")
            # out:           Returning pos = 0.
            # out:        Returning pos = 0.
            # out:     Returning pos = 0.
            return pos

        attendees = []

        attendees.append("Adams, Mary")
        # val: None
        attendees.append("Carver, Michael")
        # val: None
        attendees.append("Domer, Hugo")
        # val: None
        attendees.append("Fredericks, Carlo")
        # val: None
        attendees.append("Li, Jie")
        # val: None

        name = "Adams, Mary"
        pos = find(attendees, name, 0, len(attendees)-1, "   ")

        if pos >= 0:
            print(f"Found at position {pos}.")
            # out: Found at position 0.
        else:
            print("Not found.")
            # f.out: 0     find() range 0 4
            # f.out: 1     Searching upper half.
            # f.out: 2        find() range 3 4
            # f.out: 3        Searching upper half.
            # f.out: 4           find() range 4 4
            # f.out: 5           Person not found.
            # f.out: 6           Returning pos = -1.
            # f.out: 7        Returning pos = -1.
            # f.out: 8     Returning pos = -1.
            # f.out: 9 Not found.
            # f.out: Auto.VAL0     find() range 0 4
            # f.out: Auto.VAL1     Searching upper half.
            # f.out: Auto.VAL2        find() range 3 4
            # f.out: Auto.VAL3        Searching upper half.
            # f.out: Auto.VAL4           find() range 4 4
            # f.out: Auto.VAL5           Person not found.
            # f.out: Auto.VAL6           Returning pos = -1.
            # f.out: Auto.VAL7        Returning pos = -1.
            # f.out: Auto.VAL8     Returning pos = -1.
            # f.out: Auto.VAL9 Not found.
            # f.out:     find() range 0 4
            # f.out:     Searching lower half.
            # f.out:        find() range 0 2
            # f.out:        Searching lower half.
            # f.out:           find() range 0 1
            # f.out:           Found person.
            # f.out:           Returning pos = 0.
            # f.out:        Returning pos = 0.
            # f.out:     Returning pos = 0.
            # f.out: Found at position 0.
    #print(f)
    #how to enum?

####################################################
'''participation activity
14.3.1: Recursive function debug statements.'''
with _:
    # in: ARM
    with "main.py" as f:
        def find(lst, item, low, high, indent):
            print(f"{indent} find() range {low} {high}")
            # out:     find() range 0 4
            # out:        find() range 0 2
            # out:           find() range 0 1
            # out:              find() range 0 0
            range_size = (high - low) + 1
            mid = (high + low) // 2

            if item == lst[mid]:  # Base case 1: Found at mid
                print(f"{indent} Found person.")
                pos = mid
            elif range_size == 1:  # Base case 2: Not found
                print(f"{indent} Person not found.")
                # out:              Person not found.
                pos = -1
            else:  # Recursive search: Search lower or upper half
                if item < lst[mid]:  # Search lower half
                    print(f"{indent} Searching lower half.")
                    # out:     Searching lower half.
                    # out:        Searching lower half.
                    # out:           Searching lower half.
                    pos = find(lst, item, low, mid, indent + '   ')
                else:  # Search upper half
                    print(f"{indent} Searching upper half.")
                    pos = find(lst, item, mid+1, high, indent + "   ")

            print(f"{indent} Returning pos = {pos}.")
            # out:              Returning pos = -1.
            # out:           Returning pos = -1.
            # out:        Returning pos = -1.
            # out:     Returning pos = -1.
            return pos

        attendees = []

        attendees.append("Adams, Mary")
        # val: None
        attendees.append("Carver, Michael")
        # val: None
        attendees.append("Domer, Hugo")
        # val: None
        attendees.append("Fredericks, Carlo")
        # val: None
        attendees.append("Li, Jie")
        # val: None

        name = input("Enter person's name: Last, First: ")
        # out: Enter person's name: Last, First: ARM
        pos = find(attendees, name, 0, len(attendees)-1, "   ")

        if pos >= 0:
            print(f"Found at position {pos}.")
        else:
            print("Not found.")
            # out: Not found.
            # f.out:     find() range 0 4
            # f.out:     Searching lower half.
            # f.out:        find() range 0 2
            # f.out:        Searching lower half.
            # f.out:           find() range 0 1
            # f.out:           Searching lower half.
            # f.out:              find() range 0 0
            # f.out:              Person not found.
            # f.out:              Returning pos = -1.
            # f.out:           Returning pos = -1.
            # f.out:        Returning pos = -1.
            # f.out:     Returning pos = -1.
            # f.out: Not found.
    with "_.txt":
        '''
        1) The above debug approach requires an extra parameter be passed to indicate the amount of indentation.
        Answer: True
        Each recursive call adds a few spaces to the indent amount.
        2) Each recursive call should add a few spaces to the indent parameter.
        Answer: True
        Those extra spaces cause the additional indenting.
        3) The function should remove a few spaces from the indent parameter before returning.
        Answer: False
        The calling function added spaces to a new string object (since strings are immutable), so no removal of spaces is needed upon returning because the calling function still has the original indent string.
     '''
##############################################################################
'''Skip to main content

zyBooks
My library >
CS 2520: Python for Programmers home >
14.4: Creating recursion
Casey Wong
14.3 Adding output statements for debugging
Students:
Section 14.4 is a part of 1 assignment:
C_14
Activities:
P
Participation
C
Challenge
Due: 05/14/2026, 11:59 PM PDT
14.4 Creating a recursive function
Creating a recursive function can be accomplished in two steps.

Write base case -- Every recursive function must have a case that returns a value without performing a recursive call. That case is called the base case. A programmer may write that part of the function first, and then test. There may be multiple base cases.
Write recursive case -- The programmer then adds the recursive case to the function.
The following illustrates for a simple function that computes the factorial of N (N!). The base case is n=1 or 1!, which evaluates to 1. The recursive case is n*nfact(n-1), which is written and tested. Note: Factorial is not necessarily a good candidate for a recursive function, because a non-recursive version using a loop is so simple; however, factorial makes a simple example for demonstrating recursion. Actually useful cases for recursion are rarer in Python than for other programming languages, since Python programmers tend to prefer more natural iterative loop structures. Typically, recursion is useful when dealing with data structures of unknown size and connectivity, properties most commonly associated with tree-shaped data structures.

participation activity
14.4.1: Writing a recursive function for factorial: First writing the base case, then adding the recursive case.


1

2

The base case (non-recursive case) has to be written and tested.
def nfact(n):
    fact = 0
    if n == 1 or n == 0:  # Base case
        fact = 1
    # Fixme: Finish
    return fact
 
# Get n from user, print nfact(n)
def nfact(n):
    fact = 0
    if n == 1 or n == 0:  # Base case
        fact = 1
    else:       # Recursive case
        fact = n * nfact(n-1)
    return fact
 
# Get n from user, print nfact(n)
Enter N: 1N! is: 1Enter N: 6N! is: 720Enter N: 1N! is: 1
Static figure: Two versions of a program are shown. Two output boxes are also shown, one for each version of the program. The first version of the program shows only the base case. Begin Python code: def nfact(n): fact = 0 # Base case if n == 1 or n == 0: fact = 1 # Fixme: Finish return fact # Get n from user, print nfact(n) End Python code. The second version of the program shows the base case and the recursive case. Begin Python code: def nfact(n): fact = 0 # Base case if n == 1 or n == 0: fact = 1 # Recursive case else: fact = n * nfact(n-1) return fact # Get n from user, print nfact(n) End Python code. Step 1: The base case (non-recursive case) has to be written and tested. In the first version of the program, the if branch is highlighted. In the accompanying output box, example output is printed. Begin output: Enter N: 1 N! is: 1 End output. Step 2: The recursive case has to be added and tested. The second version of the program, which includes both the base case and the recursive case, is tested. In the accompanying output box, example output is printed. Begin output: Enter N: 1 N! is: 1 Enter N: 6 N! is: 720 End output.

Captions
Playing step 1: The base case (non-recursive case) has to be written and tested. Step finished playing

Feedback?
Before writing a recursive function, a programmer should determine: (1) Whether the problem has a naturally recursive solution, and (2) whether that solution is better than a non-recursive solution. For example, computing E = M*C*C doesn't seem to have a natural recursive solution. Computing n! (n factorial) does have a natural recursive solution, but a recursive solution is not better than a non-recursive solution that simply uses a loop, as in for i in range(n, 0, -1): result *= ifactorial Binary search has a natural recursive solution, and that solution may be easier to understand than a non-recursive solution.

A common error is to not cover all possible base cases in a recursive function. Another common error is to write a recursive function that doesn't always reach a base case. Both errors may lead to infinite recursion, causing the program to fail.

Commonly, programmers will use two functions for recursion. An "outer" function is intended to be called from other parts of the program, like the function "factorial(n)". An "inner" function is intended only to be called from that outer function, like the function " _factorial(n)" (note the "_"). The outer function may check for a valid input value, e.g., ensuring n is not negative, and then calling the inner function. Commonly, the inner function has parameters that are mainly of use as part of the recursion, and need not be part of the outer function, thus keeping the outer function more intuitive.

participation activity
14.4.2: Creating a recursive function.
1)
A recursive function with parameter n counts up from any negative number to 0. An appropriate base case would be n==0.
2)
A recursive function can have two base cases, such as n==0 returning 0, and n==1 returning 1.
3)
n factorial (n!) is commonly implemented as a recursive function due to being easier to understand and executing faster than a loop implementation.

Feedback?
challenge activity
14.4.1: Output smileys.

Full screen
712910.5105864.qx3zqy7
A smiley is a colon combined with a parenthesis to represent a smiling face. Ex: Both :) and (: are smileys. Organize the code statements to complete the recursive print_smiley() function. The function outputs n smileys on both sides of the word "happy".

Ex: If the input is 4, then the output is:

(:(:(:(: happy :):):):)


How to use this tool
Unused
main.py

Load default template...
    
    

Check

Feedback?
challenge activity
14.4.2: Creating a recursive function.
712910.5105864.qx3zqy7

Start
Write compute_powers()'s base case so that if in_val is equal to 0:

Output "6 to the power of 0 is 1".
Return 1.
Click here for example

1

2

3

Check

Next level
1
2
3

Feedback?
(*factorial) In this discussion, we ignore the fact that the math module has a very convenient math.factorial(n) function.

How was this section?

|


Provide section feedback
Activity summary for assignment: C_14
18 / 76 points
Due: 05/14/2026, 11:59 PM PDT

Completion details
14.5 Recursive math functions
'''
####################################################
GO="main.py"
####################################################
'''participation activity
14.4.1: Writing a recursive function for factorial: First writing the base case, then adding the recursive case.


1

2

The recursive case has to be added and tested.'''
with _:
    # in: 1
    with "main.py" as f:
        def nfact(n):
            fact = 0
            if n == 1 or n == 0:  # Base case
                fact = 1
            else:       # Recursive case
                fact = n * nfact(n-1)
            return fact
        nfact(1)
        # val: 1
        # Get n from user, print nfact(n)
        ins = input("Enter N: ")
        # out: Enter N: 1
        print(f"{ins}! is: {nfact(int(ins))}")
        # out: 1! is: 1
        # f.out: 1! is: 1
    f
    # val: Scratch(ins='1', nfact=<function __sc_34__.<locals>.__sc_32__.<locals>.nfact at 0x7fa5c124c7c0>, out=['1! is: 1'], err=[], outs='1! is: 1')
    # in: 6
    with "main2.py" as f1:
        def nfact(n):
            fact = 0
            if n == 1 or n == 0:  # Base case
                fact = 1
            else:       # Recursive case
                fact = n * nfact(n-1)
            return fact
        nfact(6)
        # val: 720
        # Get n from user, print nfact(n)
        ins = input("Enter N: ")
        # out: Enter N: 6
        print(f"{ins}! is: {nfact(int(ins))}")
        # out: 6! is: 720
        # f1.out: 6! is: 720
    f1
    # val: Scratch(ins='6', nfact=<function __sc_34__.<locals>.__sc_33__.<locals>.nfact at 0x7fa5c124c900>, out=['6! is: 720'], err=[], outs='6! is: 720')
####################################################
'''participation activity
14.4.2: Creating a recursive function.
1)
A recursive function with parameter n counts up from any negative number to 0. An appropriate base case would be n==0.
2)
A recursive function can have two base cases, such as n==0 returning 0, and n==1 returning 1.
3)
n factorial (n!) is commonly implemented as a recursive function due to being easier to understand and executing faster than a loop implementation.

'''
with "_.txt":
    '''
    1) A recursive function with parameter n counts up from any negative number to 0. An appropriate base case would be n==0.
        # True
            - **Base case:** n == 0, return 0
            - **Recursive case:** n < 0, return count_up(n+1)
    2) A recursive function can have two base cases, such as n==0 returning 0, and n==1 returning 1.
        # True
            - **Base case 1:** n == 0, return 0
            - **Base case 2:** n == 1, return 1
            - **Recursive case:** n > 1, return count_up(n-1)
    3) n factorial (n!) is commonly implemented as a recursive function due to being easier to understand and executing faster than a loop implementation.
        # False
            - While n factorial (n!) is commonly implemented as a recursive function due to being easier to understand, it does not execute faster than a loop implementation. In fact, the recursive implementation of n factorial can be less efficient than the loop implementation due to the overhead of multiple function calls and the potential for stack overflow with large values of n. The loop implementation typically has a linear time complexity O(n), while the recursive implementation can have a time complexity of O(n) but with additional overhead from function calls. Therefore, it is not accurate to say that n factorial is commonly implemented as a recursive function due to executing faster than a loop implementation.
     '''
with "main.py" as f:
    def rec_neg(n):
        n
        # val: -3
        # val: -2
        # val: -1
        # val: 0
        if n == 0:
            n
            # val: 0
            return 0
        elif n < 0:
            n
            # val: -3
            # val: -2
            # val: -1
            return rec_neg(n+1)
        else:
            return "Input must be negative or zero."
    rec_neg(-3)
    # val: 0
f
# val: Scratch(rec_neg=<function __sc_35__.<locals>.rec_neg at 0x7fa5c124c680>, out=[], err=[], outs='')

####################################################
'''challenge activity

## 

14.4.1: Output smileys.

_fullscreen_

Full screen

712910.5105864.qx3zqy7

A smiley is a colon combined with a parenthesis to represent a smiling face. Ex: Both `:)` and `(:` are smileys. Organize the code statements to complete the recursive print\_smiley() function. The function outputs n smileys on both sides of the word "happy".

Ex: If the input is `4`, then the output is:

`(:(:(:(: happy :):):):)`

_keyboard\_arrow\_down_

How to use this tool

#### Unused

print\_smiley(n - 1)

else:

print(" happy ", end="")

if n == 0:

print("(:", end="")

print(":)", end="")

#### main.py

Load default template...

def print\_smiley(n):

num\_smiles = int(input()) print\_smiley(num\_smiles)

Check

Feedback?

14.4.2: Creating a recursive function.
SOLUTION:
```python
def print_smiley(n):
  if n == 0:
    print(" happy ", end="")
  else:
    print("(:", end="")
    print_smiley(n - 1)
    print(":)", end="")

num_smiles = int(input())
print_smiley(num_smiles)
```
'''
with "main.py" as f:
    def print_smiley(n):
        if n == 0:
            return "happy"
        else:
            return "(: " + print_smiley(n-1) + " :)"
    print_smiley(4)
    # val: (: (: (: (: happy :) :) :) :)
f
# val: Scratch(print_smiley=<function __sc_36__.<locals>.print_smiley at 0x7fa5c124ca40>, out=[], err=[], outs='')
#in: 4
with "main2.py" as f:
    def print_smiley(n):
        if n == 0:
            print(" happy ", end="")
            # out:  happy 
        else:
            print("(:", end="")
            # out: (:
            # out: (:
            # out: (:
            # out: (:
            print_smiley(n - 1)
            # val: None
            # val: None
            # val: None
            # val: None
            print(":)", end="")
            # out: :)
            # out: :)
            # out: :)
            # out: :)

    num_smiles = int(input())
    # out: 4
    print_smiley(num_smiles)
    # val: None
    # f.out: (:
    # f.out: (:
    # f.out: (:
    # f.out: (:
    # f.out:  happy 
    # f.out: :)
    # f.out: :)
    # f.out: :)
    # f.out: :)
####################################################
'''challenge activity
14.4.2: Creating a recursive function.
712910.5105864.qx3zqy7

Jump to level 1
Write compute_powers()'s base case so that if in_val is equal to 0:

Output "6 to the power of 0 is 1".
Return 1.
Click here for example
###FINISHED
def compute_powers(in_val):
    if in_val == 0:
        print("6 to the power of 0 is 1")
        return 1
    else:
        product = 6 * compute_powers(in_val - 1)
        print(f"6 to the power of {in_val} is {product}")
        return product

in_val = int(input())
compute_powers(in_val)'''
# in: 3
with "main.py" as f:
        def compute_powers(in_val):

            #
            if in_val == 0:
                print("6 to the power of 0 is 1")
                # out: 6 to the power of 0 is 1
                return 1
            #
            else:
                product = 6 * compute_powers(in_val - 1)
                print(f"6 to the power of {in_val} is {product}")
                # out: 6 to the power of 1 is 6
                # out: 6 to the power of 2 is 36
                # out: 6 to the power of 3 is 216
                return product

        in_val = int(input())
        # out: 3
        compute_powers(in_val)
        # val: 216
        # f.out: 6 to the power of 0 is 1
        # f.out: 6 to the power of 1 is 6
        # f.out: 6 to the power of 2 is 36
        # f.out: 6 to the power of 3 is 216
####################################################
'''challenge activity
14.4.2: Creating a recursive function.
712910.5105864.qx3zqy7

Jump to level 1
Write find_growth()'s recursive case to recursively call find_growth() with week + 1 and count multiplied by 3.

Click here for example
Ex: If the input is 200, then the output is:
week: 1, count: 200
week: 2, count: 600
week: 3, count: 1800
Bacteria population is at least 1800 in week 3.
Note: Assume input is non-negative.
def find_growth(week, count):
    print(f"week: {week}, count: {count}")

    if count >= 1800:
        print(f"Bacteria population is at least 1800 in week {week}.")

    """ Your code goes here """

count = int(input())
find_growth(1, count)
'''
# in: 200
with "main2.py" as f:
    def find_growth(week, count):
        print(f"week: {week}, count: {count}")
        # out: week: 1, count: 200
        # out: week: 2, count: 600
        # out: week: 3, count: 1800
        if count >= 1800:
            print(f"Bacteria population is at least 1800 in week {week}.")
            # out: Bacteria population is at least 1800 in week 3.
        else:
            return find_growth(week + 1, count * 3)

    count = int(input())
    # out: 200
    find_growth(1, count)
    # val: None
    # f.out: week: 1, count: 200
    # f.out: week: 2, count: 600
    # f.out: week: 3, count: 1800
    # f.out: Bacteria population is at least 1800 in week 3.
##########################
'''challenge activity
14.4.2: Creating a recursive function.
712910.5105864.qx3zqy7

Jump to level 1
Integers total_months and inventory are read from input. Complete purchases()'s recursive case:

If month is even, call purchases() to compute the next month's inventory as the current month's inventory minus 18.
Otherwise, call purchases() to compute the next month's inventory as the current month's inventory minus 4.
Click here for example
Ex: If the input is:
3
250
then the output is:

Month: 3, inventory: 228
Note: x % 2 == 0 is True if x is even.

def purchases(total_months, month, inventory):
    if month == total_months:
        print(f"Month: {total_months}, inventory: {inventory}")
    else:

        """ Your code goes here """

total_months = int(input())
inventory = int(input())
purchases(total_months, 1, inventory)




'''
# in: 3, 250
setin("3","250")
# val: None
with "main.py" as f:
    def purchases(total_months, month, inventory):
        if month == total_months:
            print(f"Month: {total_months}, inventory: {inventory}")
            # out: Month: 3, inventory: 228
        else:
            if month % 2 == 0:
                return purchases(total_months, month + 1, inventory - 18)
            else:
                return purchases(total_months, month + 1, inventory - 4)

    total_months = int(input())
    inventory = int(input())
    purchases(total_months, 1, inventory)
    # val: None
    # f.out: Month: 3, inventory: 228

##############################################################################
'''Activity summary for assignment: C_14
26 / 76 points
Due: 05/14/2026, 11:59 PM PDT

Completion details
Section 14.1
6 / 6 points

Section 14.2
9 / 9 points

Section 14.3
3 / 3 points

Section 14.4
8 / 8 points

Section 14.5
0 / 4 points

P
Participation activities
14.5.1
0 / 2 points
C
Challenge activities
14.5.1
0 / 2 points
Next section
Section 14.6
0 / 6 points

P
Participation activities
14.6.1
0 / 1 point
14.6.2
0 / 2 points
C
Challenge activities
14.6.1
0 / 2 points
14.6.2
0 / 1 point
Section 14.7
0 / 10 points

L
Lab activities
14.7.1
0 / 10 points
Section 14.8
0 / 10 points

L
Lab activities
14.8.1
0 / 10 points
Section 14.9
0 / 10 points

L
Lab activities
14.9.1
0 / 10 points
Section 14.10
0 / 10 points

L
Lab activities
14.10.1
0 / 10 points'''

'''
14.5 Recursive math functions
Recursive functions can be used to solve certain math problems, such as computing the Fibonacci sequence. The Fibonacci sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc. The pattern is to compute the next number by adding the previous two numbers. The sequence starts with 0 and 1.

Below is a program that outputs the Fibonacci sequence step-by-step for a user-entered number of steps. The program starts after the first 0 and 1 of the Fibonacci sequence. The base case is that the program has output the requested number of steps. The recursive case computes the next step.

Figure 14.5.1: Fibonacci sequence step-by-step.
"""
Output the Fibonacci sequence step-by-step.
Fibonacci sequence starts as:
0 1 1 2 3 5 8 13 21 ... in which the first
two numbers are 0 and 1 and each additional
number is the sum of the previous two numbers
"""
def fibonacci(v1, v2, run_cnt):
    print(f"{v1} + {v2} = {v1+v2}")

    if run_cnt <= 1:  # Base case:
                      # Ran for user's number of steps
        pass  # Do nothing
    else:             # Recursive case
        fibonacci(v2, v1+v2, run_cnt-1)


print ("This program outputs the\n"
       "Fibonacci sequence step-by-step,\n"
       "starting after the first 0 and 1.\n")

run_for = int(input("How many steps would you like?"))

fibonacci(0, 1, run_for)
This program outputs the
Fibonacci sequence step-by-step,
starting after the first 0 and 1.

How many steps would you like?10
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21
13 + 21 = 34
21 + 34 = 55
34 + 55 = 89

Feedback?
Try 14.5.1: Recursive Fibonacci.

Full screen
Write a program that outputs the nth Fibonacci number, where n is a user-entered number. So if the user enters 4, the program should output 3 (without outputting the intermediate steps). Use a recursive function compute_nth_fib that takes n as a parameter and returns the Fibonacci number. The function has two base cases: input 0 returns 0, and input 1 returns 1.


Model Solution

Feedback?
Recursion can be used to solve the greatest common divisor (GCD) problem. The GCD is the largest number that divides evenly into two numbers, e.g. GCD(12, 8) = 4. A simple algorithm to compute the GCD subtracts the smaller number from the larger number until both numbers are equal. For example, GCD(12, 8) = GCD(12-8=4, 8) = GCD(4, 8-4=4). The equal numbers are the GCD. Euclid described this algorithm around 300 BC.

The below program recursively computes the GCD of two numbers. The base case is that the two numbers are equal, so that number is returned. The recursive case subtracts the smaller number from the larger number and then calls GCD with the new pair of numbers.

Figure 14.5.2: Calculate greatest common divisor of two numbers.
"""
Determine the greatest common divisor
of two numbers, e.g., GCD(8, 12) = 4
"""


def gcd(n1, n2):
    if n1 == n2:   # Base case          
        return n1
    elif n1 < n2:  # Recursive case
      return gcd(n1, n2 - n1)
    else:
      return gcd(n1 - n2, n2)

print ("This program outputs the greatest "
       "common divisor of two numbers.\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (num1 < 1) or (num2 < 1):
    print("Note: Neither value can be below 1.")
else:
    my_gcd = gcd(num1, num2)
    print(f"Greatest common divisor = {my_gcd}")
This program outputs the greatest common divisor of two numbers.

Enter first number:12
Enter second number:8
Greatest common divisor = 4
...
This program outputs the greatest common divisor of two numbers.

Enter first number:456
Enter second number:784
Greatest common divisor = 8

Feedback?
The depth of recursion is a measure of how many recursive calls of a function have been made, but have not yet returned. Each recursive call requires the Python interpreter to allocate more memory, and eventually all of the system memory could be used. Thus, a recursion depth limit exists, accessible using the function sys.getrecursionlimit(). The default recursion depth limit is typically 1000. The limit can be changed using sys.setrecursionlimit(). Exceeding the depth limit causes a RuntimeError to occur. Ex: The following program causes 1000 recursive calls.

Figure 14.5.3: Limit on recursion depth.
def rec_func(n):
    if n == 0:
        return 1
    return rec_func(n - 1)


num = int(input("Enter the number: "))
print(rec_func(num))
Enter the number: 1000

Traceback (most recent call last):
  File "main.py", line 8, in <module>
    print(rec_func(num))
  File "main.py", line 4, in rec_func
    return rec_func(n - 1)
  File "main.py", line 4, in rec_func
    return rec_func(n - 1)
  File "main.py", line 4, in rec_func
    return rec_func(n - 1)
  [Previous line repeated 995 more times]
  File "main.py", line 2, in rec_func
    if n == 0:
RecursionError: maximum recursion depth exceeded in comparison

Feedback?
participation activity
14.5.1: Recursive GCD.
1)
How many calls are made to the gcd function for gcd(12, 8)?

Check

Show answer
2)
How many calls are made to the gcd function for gcd(5, 3)?

Check

Show answer

Feedback?
Exploring further:
More on the Fibonacci sequence from wikipedia.org
More on the GCD algorithm from wikipedia.org
challenge activity
14.5.1: Writing a recursive math function.
Write code to complete raise_to_power(). Note: This example is for practicing recursion; a non-recursive function, or using the built-in function math.pow(), would be more common.

Sample output with inputs: 4 2
4^2 = 16


Learn how our autograder works

712910.5105864.qx3zqy7
1 test passed
All tests passed

Run

Feedback?
How was this section?

|


Provide section feedback
Activity summary for assignment: C_14
26 / 76 points
Due: 05/14/2026, 11:59 PM PDT
'''

####################################################
# in: 26
with "main.py" as f:
        """
        Output the Fibonacci sequence step-by-step.
        Fibonacci sequence starts as:
        0 1 1 2 3 5 8 13 21 ... in which the first
        two numbers are 0 and 1 and each additional
        number is the sum of the previous two numbers
        """
        def fibonacci(v1, v2, run_cnt):
            print(f"{v1} + {v2} = {v1+v2}")

            if run_cnt <= 1:  # Base case:
                            # Ran for user's number of steps
                pass  # Do nothing
            else:             # Recursive case
                fibonacci(v2, v1+v2, run_cnt-1)


        print ("This program outputs the\n"
        # out: This program outputs the
        # out: Fibonacci sequence step-by-step,
        # out: starting after the first 0 and 1.
            "Fibonacci sequence step-by-step,\n"
            "starting after the first 0 and 1.\n")

        run_for = int(input("How many steps would you like?"))

        fibonacci(0, 1, run_for)
        # f.out: This program outputs the
        # f.out: Fibonacci sequence step-by-step,
        # f.out: starting after the first 0 and 1.
        # !err: EOFError: No more inputs for testing
        # !err:   at line 2131: def print_smiley(n):
##################################################################
'''Try 14.5.1: Recursive Fibonacci.

Full screen
Write a program that outputs the nth Fibonacci number, where n is a user-entered number. So if the user enters 4, the program should output 3 (without outputting the intermediate steps). Use a recursive function compute_nth_fib that takes n as a parameter and returns the Fibonacci number. The function has two base cases: input 0 returns 0, and input 1 returns 1.
def compute_nth_fib(num):
    # if base case ...
        # Return base case value ...
    # else ...
        # Recursively call compute_nth_fib() ...

# User input and print statements'''
setin("4")
# val: None
with "main.py" as f:
    def compute_nth_fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return compute_nth_fib(num - 1) + compute_nth_fib(num - 2)

    n = int(input("Enter n: "))
    print(f"The {n}th Fibonacci number is: {compute_nth_fib(n)}")
    # out: The 4th Fibonacci number is: 3
    # f.out: The 4th Fibonacci number is: 3
    # ✅ in: 4
    # ✅ out: Enter n: 4
    # ✅ out: The 4th Fibonacci number is: 3
    # ✅ f.out: Enter n: 4
    # ✅ f.out: The 4th Fibonacci number is: 3
####################################################

'''participation activity
14.5.1: Recursive GCD.
1)
How many calls are made to the gcd function for gcd(12, 8)?

Check

Show answer
2)
How many calls are made to the gcd function for gcd(5, 3)?

Check

Show answer'''
with "_.txt":
    '''
    1) How many calls are made to the gcd function for gcd(12, 8)?
        # 3 calls
            - gcd(12, 8)
            - gcd(4, 8)
            - gcd(4, 4)
    2) How many calls are made to the gcd function for gcd(5, 3)?
        # 4 calls
            - gcd(5, 3)
            - gcd(2, 3)
            - gcd(2, 1)
            - gcd(1, 1)
     '''
setin("12","8")
# val: None
with "main.py" as f:
    def gcd(n1, n2):
        if n1 == n2:   # Base case          
            return n1
        elif n1 < n2:  # Recursive case
            return gcd(n1, n2 - n1)
        else:
            return gcd(n1 - n2, n2)

    print(gcd(12, 8))
    # out: 4
    # f.out: 4
#########################################################
'''challenge activity
14.5.1: Writing a recursive math function.
Write code to complete raise_to_power(). Note: This example is for practicing recursion; a non-recursive function, or using the built-in function math.pow(), would be more common.

Sample output with inputs: 4 2
4^2 = 16
'''
# setin("4","2")
with "main2.py" as f2:
        def compute_nth_fib(num):
            # base cases
            if num == 0:
                return 0
            elif num == 1:
                return 1
            # recursive case
            else:
                return compute_nth_fib(num - 1) + compute_nth_fib(num - 2)

        # User input and print
        n = int(input())
        print(compute_nth_fib(n))
        # out: 144
        # f2.out: 144
setin("4","2")
# val: None
with "main.py" as f:
    def raise_to_power(base_val, exponent_val):
        if exponent_val == 0:
            result_val = 1
        else:
            result_val = base_val * raise_to_power(base_val, exponent_val - 1)
    
        return result_val
    
    user_base = int(input())
    user_exponent = int(input())
    print(f"{user_base}^{user_exponent} = {raise_to_power(user_base, user_exponent)}")
    # out: 4^2 = 16
    # f.out: 4^2 = 16
##############################################################################
'''## 14.6 Recursive exploration of all possibilities

Recursion is a powerful tool for exploring all possibilities, such as all possible reorderings of a word's letters, all possible subsets of items, all possible paths between cities, etc. This section provides several examples of using recursion for such exploration.

Consider the problem of printing all possible combinations (or "scramblings") of a word's letters. For example, the letters of "abc" can be scrambled in 6 ways: abc, acb, bac, bca, cab, cba. Those possibilities can be obtained by thinking of three choices: Choosing the first letter ("a", "b", or "c"), then choosing the second letter (if "a" was the first choice, then second possible choices are "b" or "c"; if "b" was the first choice, then second possible choices are "a" and "c"; etc.), then choosing the third letter. The choices can be depicted using a tree. Each level represents a choice. Each node in the tree shows the unchosen letters on the left, and the chosen letters on the right, as in the animation figure below.

Such a tree forms the basis for a recursive exploration function to generate all possible combinations of a string's letters. The function will take two parameters, one for the unchosen letters, and one for the already chosen letters. The base case will be when no letters exist in the unchosen letters, in which case the chosen letters are printed. The recursive case will call the function once for each letter in the unchosen letters. The following animation depicts how such a recursive algorithm would traverse the tree. The leaves of the tree (the bottommost nodes) represent the base case.

### PARTICIPATION ACTIVITY: Exploring all possibilities viewed as a tree of choices.

Static figure: A tree of choices shown has 4 levels and 16 nodes. Each node's value contains the letters a, b, and c, as well as a slash. A legend explains the format for node values: remaining-letters / chosen-letters. The root node has the value a b c /, meaning all letters are remaining and none are chosen. Following are a description and table representation of the tree. The root node has 3 children which form the second level. The second level has the label "Choose 1st letter", and from left to right, the second level's nodes have the values b c / a, a c / b,  and a b / c, respectively. Each of the 3 nodes on the second level has 2 children, so the third level has 6 nodes. The third level is labeled "Choose 2nd letter," and from left to right, the third level's nodes have the values  c / a b, b / a c, c / b a, a / b c, b / c a, and a / c b, respectively. Each of the 6 nodes on the third level has 1 child, so the fourth level also has 6 nodes. The fourth level is labeled "Choose 3rd letter," and from left to right, the nodes have the values / a b c, / a c b, / b a c, / b c a, / c a b, and / c b a, respectively. The following table shows the relationships between the nodes at different levels. While values are repeated in the table to show the parent node for each child node, values are not repeated in the tree.

RootChoose 1st letterChoose 2nd letterChoose 3rd letter
a b c slashb c slash ac slash a bslash a b c
a b c slashb c slash ab slash a cslash a c b
a b c slasha c slash bc slash b aslash b a c
a b c slasha c slash ba slash b cslash b c a
a b c slasha b slash cb slash c aslash c a b
a b c slasha b slash ca slash c bslash c b a

Step 1: "a" is chosen from "abc", then "b" is chosen from "bc". Finally, "c" is chosen from "c". This step refers to the first row in the table.
Step 2: "b" has already been chosen from "bc". "c" can also be chosen. "acb" is chosen from "b". This step refers to columns 3 and 4 in the second row in the table.
Step 3: "b" is chosen from "abc". This step refers to the third and fourth rows in the table.
Step 4: "c" is chosen from "abc". This step refers to the fifth and sixth rows in the table.

The program below receives a word from the user then jumbles all of its letters in to every possible ordering. The base case is that all letters have been used. In the recursive case, a remaining letter is moved to the scrambled letters, recursively explored, then put back. This is done for each remaining letter.

> **Scramble a word's letters in every possible way.**
> ```python
> def scramble(r_letters, s_letters):
>     """
>     Output every possible combination of a word.
>     Each recursive call moves a letter from
>     r_letters (remaining letters) to
>     s_letters (scrambled letters)
>     """
>     if len(r_letters) == 0:
>         # Base case: All letters used
>         print(s_letters)
>     else:
>         # Recursive case: For each call to scramble()
>         # move a letter from remaining to scrambled
>         for i in range(len(r_letters)):
>             # The letter at index i will be scrambled
>             scramble_letter = r_letters[i]
>             
>             # Remove letter to scramble from remaining letters list
>             remaining_letters = r_letters[:i] + r_letters[i+1:]
>             
>             # Scramble letter
>             scramble(remaining_letters, s_letters + scramble_letter)
> 
> word = input("Enter a word to be scrambled: ")
> scramble(word, "")
> ```
> ```
> Enter a word to be scrambled: cat
> cat
> cta
> act
> atc
> tca
> tac
> ```

Recursion is useful for finding all possible subsets of a set of items. The following example is a shopping spree in which you may select a 3-item subset from a larger set of items. The program should print all possible 3-item subsets given the larger set. The program also happens to print the total price value of those items.

The shopping_bag_combinations() function has a parameter for the current bag contents, and a parameter for the remaining items from which to choose. The base case is that the current bag already has 3 items. The recursive case is to move one of the remaining items to the bag, recursively call the function, then move the item back from the bag to the remaining items.

> **Shopping spree in which you can fit 3 items in your shopping bag.**
> ```python
> max_items_in_bag = 3
> 
> def shopping_bag_combinations(curr_bag, remaining_items):
>     """
>     Output every combination of items that fit
>     in a shopping bag. Each recursive call moves
>     one item into the shopping bag.
>     """
>     if len(curr_bag) == max_items_in_bag:
>         # Base case: Shopping bag full
>         bag_value = 0
>         for item in curr_bag:
>             bag_value += item["price"]
>             print(f'{item["name"]}  ', end=" ")
>         print(f"= {bag_value}")
>     else:
>         # Recursive case: Move one of the remaining items
>         # to the shopping bag.
>         for index, item in enumerate(remaining_items):
>             # Move item into bag
>             curr_bag.append(item)
>             remaining_items.pop(index)
> 
>             shopping_bag_combinations(curr_bag, remaining_items)
> 
>             # Take item out of bag
>             remaining_items.insert(index, item)
>             curr_bag.pop()
> 
> items = [
>     {
>         "name": "Milk",
>         "price": 1.25
>     },
>     {
>         "name": "Belt",
>         "price": 23.55
>     },
>     {
>         "name": "Toys",
>         "price": 19.05
>     },
>     {
>         "name": "Cups",
>         "price": 11.85
>     }
> ]
> 
> bag = []
> shopping_bag_combinations(bag, items)
> ```
> ```
> Milk   Belt   Toys   = 43.85
> Milk   Belt   Cups   = 36.65
> Milk   Toys   Belt   = 43.85
> Milk   Toys   Cups   = 32.15
> Milk   Cups   Belt   = 36.65
> Milk   Cups   Toys   = 32.15
> Belt   Milk   Toys   = 43.85
> Belt   Milk   Cups   = 36.65
> Belt   Toys   Milk   = 43.85
> Belt   Toys   Cups   = 54.45
> Belt   Cups   Milk   = 36.65
> Belt   Cups   Toys   = 54.45
> Toys   Milk   Belt   = 43.85
> Toys   Milk   Cups   = 32.15
> Toys   Belt   Milk   = 43.85
> Toys   Belt   Cups   = 54.45
> Toys   Cups   Milk   = 32.15
> Toys   Cups   Belt   = 54.45
> Cups   Milk   Belt   = 36.65
> Cups   Milk   Toys   = 32.15
> Cups   Belt   Milk   = 36.65
> Cups   Belt   Toys   = 54.45
> Cups   Toys   Milk   = 32.15
> Cups   Toys   Belt   = 54.45
> ```

Recursion is useful for finding all possible paths. In the following example, a salesman must travel to 3 cities: Boston, Chicago, and Los Angeles. The salesman wants to know all possible paths among those three cities, starting from any city. A recursive exploration of all travel paths can be used. The base case is that the salesman has traveled to all cities. The recursive case is to travel to a new city, explore possibilities, then return to the previous city.

> **Find distance of traveling to 3 cities.**
> ```python
> num_cities = 3
> city_names = []
> distances = []
> 
> def travel_paths(curr_path, need_to_visit):
>     if len(curr_path) == num_cities:  # Base case: Visited all cities
>         total_distance = 0
>         for i in range(len(curr_path)):
>             print(f"{city_names[curr_path[i]]}   ", end=" ")
> 
>             if i > 0:
>                 total_distance += distances[curr_path[i-1]][curr_path[i]]
> 
>         print(f"= {total_distance}")
>     else:  # Recursive case: Travel to each city
>         for i in range(len(need_to_visit)):
>             # Visit city
>             city = need_to_visit[i]
>             need_to_visit.pop(i)
>             curr_path.append(city)
> 
>             travel_paths(curr_path, need_to_visit)
> 
>             need_to_visit.insert(i, city)
>             curr_path.pop()
> 
> distances.append([0])
> distances[0].append(960)  # Boston-Chicago
> distances[0].append(2960) # Boston-Los Angeles
> distances.append([960])   # Chicago-Boston
> distances[1].append(0)
> distances[1].append(2011) # Chicago-Los Angeles
> distances.append([2960])  # Los Angeles-Boston
> distances[2].append(2011) # Los Angeles-Chicago
> distances[2].append(0)
> 
> city_names = ["Boston", "Chicago", "Los Angeles"]
> 
> path = []
> need_to_visit = [0, 1, 2] # (Need to visit all 3 cities)
> travel_paths(path, need_to_visit)
> ```
> ```
> Boston    Chicago    Los Angeles    = 2971
> Boston    Los Angeles    Chicago    = 4971
> Chicago    Boston    Los Angeles    = 3920
> Chicago    Los Angeles    Boston    = 4971
> Los Angeles    Boston    Chicago    = 3920
> Los Angeles    Chicago    Boston    = 2971
> ```

### PARTICIPATION ACTIVITY: Recursive exploration.

**1.** What is the output of: scramble("xy", "")? Determine your answer by manually tracing the code, not by running the program.
Answer: xy yx
*Hint: The first recursive call selects the first letter as "x".*
*The first call selects x, then makes a recursive call with y remaining, yielding xy. That first call then selects y, then makes a recursive call with x remaining, yielding yx.*

**2.** You wish to generate all possible 3-letter subsets from the letters in an N-letter word (N>3). Which of the above recursive functions is the closest (just enter the function's name)?
Answer: shopping_bag_combinations
*Hint: Not just reordering, but choosing items from a larger set.*
*shopping_bag_combinations consists of generating all possible subsets from a list of items. The N letters are like the list of items.*

### CHALLENGE ACTIVITY: Enter the output of recursive exploration.

**Level 1:**

What is the output?

```python
def reorder_nums(remain_nums, reordered_nums):
    if len(remain_nums) == 0:
        print(reordered_nums[0], reordered_nums[1], reordered_nums[2], sep='')
    else:
        for i in range(len(remain_nums)):
            tmp_remain_nums = remain_nums[:] # Make a copy.
            tmp_removed_num = tmp_remain_nums[i] 
            tmp_remain_nums.pop(i) # Remove element at i
            reordered_nums.append(tmp_removed_num)
            reorder_nums(tmp_remain_nums, reordered_nums)
            reordered_nums.pop() # Remove last element

nums_to_reorder = []
result_nums = []

nums_to_reorder.append(${numbers[0]})
nums_to_reorder.append(${numbers[1]})
nums_to_reorder.append(${numbers[2]})

reorder_nums(nums_to_reorder, result_nums)
```

*The code recursively generates and outputs all combinations of nums_to_reorder values: ${numbers[0]}, ${numbers[1]}, and ${numbers[2]}.

For each value in nums_to_reorder:

  - 
  The first output is the current value, followed by the remaining two values of nums_to_reorder in order.
    
      
        Ex: If the current value is ${numbers[0]}, the output is `${numbers[0]}${numbers[1]}${numbers[2]}`.
      
    
  
  - 
    The second output is the current value, followed by the remaining two values of nums_to_reorder, but in reverse order.
    
      
        Ex: If the current value is ${numbers[0]}, the output is `${numbers[0]}${numbers[2]}${numbers[1]}`.
      
    
  

Thus, the output is:

```
${numbers[0]}${numbers[1]}${numbers[2]}
${numbers[0]}${numbers[2]}${numbers[1]}
${numbers[1]}${numbers[0]}${numbers[2]}
${numbers[1]}${numbers[2]}${numbers[0]}
${numbers[2]}${numbers[0]}${numbers[1]}
${numbers[2]}${numbers[1]}${numbers[0]}
```*

**Level 2:**

What is the output?

```python
def reorder_nums(remain_nums, reordered_nums):
    if len(remain_nums) == 0:
        print(reordered_nums[0], reordered_nums[1], reordered_nums[2], sep='')
    else:
        for i in reversed(range(len(remain_nums))): # New: This line changed
            tmp_remain_nums = remain_nums[:] # Make a copy.
            tmp_removed_num = tmp_remain_nums[i] 
            tmp_remain_nums.pop(i) # Remove element at i
            reordered_nums.append(tmp_removed_num)
            reorder_nums(tmp_remain_nums, reordered_nums)
            reordered_nums.pop() # Remove last element

nums_to_reorder = []
result_nums = []

nums_to_reorder.append(${numbers[0]})
nums_to_reorder.append(${numbers[1]})
nums_to_reorder.append(${numbers[2]})

reorder_nums(nums_to_reorder, result_nums)
```

*The code recursively generates and outputs all combinations of nums_to_reorder values: ${numbers[0]}, ${numbers[1]}, and ${numbers[2]}.

For each value in the reversed order of nums_to_reorder:

  - 
  The first output is the current value, followed by the remaining two values of nums_to_reorder in reverse order.
    
      
        Ex: If the current value is ${numbers[2]}, the output is `${numbers[2]}${numbers[1]}${numbers[0]}`.
      
    
  
  - 
    The second output is the current value, followed by the remaining two values of nums_to_reorder, but in order.
    
      
        Ex: If the current value is ${numbers[2]}, the output is `${numbers[2]}${numbers[0]}${numbers[1]}`.
      
    
  

Thus, the output is:

```
${numbers[2]}${numbers[1]}${numbers[0]}
${numbers[2]}${numbers[0]}${numbers[1]}
${numbers[1]}${numbers[2]}${numbers[0]}
${numbers[1]}${numbers[0]}${numbers[2]}
${numbers[0]}${numbers[2]}${numbers[1]}
${numbers[0]}${numbers[1]}${numbers[2]}
```*

### CHALLENGE ACTIVITY: Recursive exploration.

Organize the code statements to complete explore()'s recursive case. The recursive explore() function outputs all possible reorderings of a list's elements.

Base case: When all elements are picked, all the elements are output in the current ordering.

Recursive case: For each element that is not picked yet:

Create new_remain as a copy of remain_vals excluding the element.
Create new_picked as a copy of picked_vals with the element appended.
Call explore() recursively with new_remain and new_picked as the arguments.

**Solution:**
```python
def explore(remain_vals, picked_vals):
    # Base case: All values are picked
    if len(remain_vals) == 0:
        for val in picked_vals:
            print(val, end=" ")
        print()

    # Recursive case
    else:
    for i, val in enumerate(remain_vals):
      new_remain = remain_vals[:i] + remain_vals[i+1:]
      new_picked = picked_vals + [val]
      explore(new_remain, new_picked)

vals_to_pick = []
picks = []

for token in input().split():
    vals_to_pick.append(int(token))

print(f"All possible ways to order a list of size {len(vals_to_pick)}:")

explore(vals_to_pick, picks)
```

Exploring further:
 
 - More on recursion trees from Wikipedia.org.'''
####################################################
'''participation activity
14.6.1: Exploring all possibilities viewed as a tree of choices.'''


with "main.py" as f:
    
    

with "main2.py" as f1:
    

####################################################
with "main.py" as f:
    def fibonacci(n):
        if n <= 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
    # !err: EOFError: No more inputs for testing
    # !err:   at line 2638: def compute_nth_fib(num):
##############################################################################

1
# val: 1
2
# val: 2
with bash:
    #date
    #cat main.py
    #cat C_14_MD/README

#INFO()

#ret_file("./C_14_MD/README")

# in: 1
with "test.py":
    #input test
    def count_down(count):
        count
        if count == 0:
            count            
            print('Go!')                  
        else:
            count                        
            print(count)             
                
            count_down(count-1)
            count        
    ins=input("test:")
    count_down(int(ins))
#ret_file("⠀⠀⠀")
1
# val: 1


############################################################################
'''## 14.6 Recursive exploration of all possibilities

Recursion is a powerful tool for exploring all possibilities, such as all possible reorderings of a word's letters, all possible subsets of items, all possible paths between cities, etc.

### PARTICIPATION ACTIVITY 14.6.2: Recursive exploration.
1. scramble("xy", "") -> Answer: xy yx
2. Closest function for 3-letter subsets from N letters -> Answer: shopping_bag_combinations

### CHALLENGE 14.6.3 Level 1 [a,b,c]:
   abc / acb / bac / bca / cab / cba

### CHALLENGE 14.6.3 Level 2 (reversed range):
   cba / cab / bca / bac / acb / abc

### CHALLENGE 14.6.4 explore() recursive case order:
    for i, val in enumerate(remain_vals):
        new_remain = remain_vals[:i] + remain_vals[i+1:]
        new_picked = picked_vals + [val]
        explore(new_remain, new_picked)
'''


############################################################################
'''## 14.7 LAB: Fibonacci sequence (recursion)

The Fibonacci sequence is a famous numeric sequence in which the next number is the sum of the previous two numbers. The first few numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Write a recursive function called fibonacci() that takes a parameter, n, and returns the nth Fibonacci number.

Ex: If the input is: 7
the output is: fibonacci(7) is 21

Note: Use recursion and DO NOT use any loops.
'''
# --- 14.7 SOLUTION (paste into zyBooks LAB editor) ---
def fibonacci(n):
    if n <= 1:
        return n if n == 0 else 1
    # Wait -- zyBooks indexes 1,1,2,3,5,8,13,21 so fib(1)=1, fib(2)=1
    # Cleaner version below:
    return fibonacci(n - 1) + fibonacci(n - 2)

# Cleaner canonical version for zyBooks (1-indexed: fib(1)=1, fib(2)=1, fib(7)=21):
def fibonacci_zb(n):
    if n <= 2:
        return 1
    return fibonacci_zb(n - 1) + fibonacci_zb(n - 2)

start_num = int(input())
print(f'fibonacci({start_num}) is {fibonacci_zb(start_num)}')
# expected for input 7 -> fibonacci(7) is 21


############################################################################
'''## 14.8 LAB: All permutations of names

Write a recursive function called print_all_permutations() that, given a list of names and an empty list, will print all possible orderings of the names.

Ex: If the input is:
Julia Lucas Mia -1

then the output is:
Julia Lucas Mia
Julia Mia Lucas
Lucas Julia Mia
Lucas Mia Julia
Mia Julia Lucas
Mia Lucas Julia
'''
# 14.8 ready-to-paste solution below
with "main.py" as f:
    def print_all_permutations(permList, nameList):
        if len(nameList) == 0:
            print(' '.join(permList))
        else:
            for i in range(len(nameList)):
                new_perm = permList + [nameList[i]]
                new_remain = nameList[:i] + nameList[i+1:]
                print_all_permutations(new_perm, new_remain)

    name_list = []
    name = input()
    while name != '-1':
        name_list.append(name)
        name = input()
    perm_list = []
    print_all_permutations(perm_list, name_list)
# in: Julia
# in: Lucas
# in: Mia
# in: -1
# expected:
# Julia Lucas Mia / Julia Mia Lucas / Lucas Julia Mia / Lucas Mia Julia / Mia Julia Lucas / Mia Lucas Julia
# status: ready, awaiting Casey check


############################################################################
'''## 14.9 LAB: Number pattern (zyBooks 14.9.1)

Write a recursive function called print_num_pattern() that outputs the following number pattern.

Given a positive integer as input (Ex: 12), subtract another positive integer (Ex: 3) continually until a negative value is reached, and then continually add the second integer until the first integer is again reached. For this lab, do not end output with a newline.

Do not modify the given main program.

Ex: input 12 / 3 -> 12 9 6 3 0 -3 0 3 6 9 12

**Test Cases (verified):**
  12 / 3  -> 12 9 6 3 0 -3 0 3 6 9 12   ✅
  17 / 5  -> 17 12 7 2 -3 2 7 12 17     ✅
  6 / 4   -> 6 2 -2 2 6                  ✅
  8 / 2   -> 8 6 4 2 0 -2 0 2 4 6 8     ✅
'''
# 14.9 ready-to-paste solution below
with "main.py" as f:
    def print_num_pattern(num1, num2):
        # ✅ <-
        print(num1, end=' ')
        if num1 < 0:
            return
        print_num_pattern(num1 - num2, num2)
        print(num1, end=' ')
        # ✅ <-

    if __name__ == "__main__":
        user_num1 = int(input())
        user_num2 = int(input())
        print_num_pattern(user_num1, user_num2)
# in: 12
# in: 3
# expected: 12 9 6 3 0 -3 0 3 6 9 12
# status: ready, awaiting submission

############################################################################
'''## 14.10 LAB: Count the digits (zyBooks 14.10.1)

Write a recursive function called digit_count() that takes a non-negative integer as a parameter and returns the number of digits in the integer.

Hint: The digit count increases by 1 whenever the input number is divided by 10.

Ex: input 345 -> 3

**Edge cases (verified):**
  0          -> 1   ✅
  5          -> 1   ✅
  10         -> 2   ✅
  99         -> 2   ✅
  345        -> 3   ✅
  1000000    -> 7   ✅
  9999999999 -> 10  ✅
'''
# 14.10 ready-to-paste solution below
with "main.py" as f:
    def digit_count(num):
        # ✅ <-
        if num < 10:
            return 1
        return 1 + digit_count(num // 10)
        # ✅ <-

    if __name__ == "__main__":
        num = int(input())
        digit = digit_count(num)
        print(digit)
# in: 345
# expected: 3
# status: ready, awaiting submission
# !err: --- ERROR ---
# !err: Traceback (most recent call last):
# !err:   File "/home/runner/workspace/sandbox/notebook/Helpers/helpings.py", line 150, in mock_input
# !err:     value = next(input_iter)
# !err:             ^^^^^^^^^^^^^^^^
# !err: StopIteration
# !err: 
# !err: During handling of the above exception, another exception occurred:
# !err: 
# !err: Traceback (most recent call last):
# !err:   File "<string>", line 224, in <module>
# !err:   File "/home/runner/workspace/sandbox/notebook/goog.py", line 2722, in <module>
# !err:     # out: 144
# !err:             ^^^
# !err:   File "/home/runner/workspace/sandbox/notebook/Helpers/helpings.py", line 154, in mock_input
# !err:     raise EOFError("No more inputs for testing")
# !err: EOFError: No more inputs for testing
