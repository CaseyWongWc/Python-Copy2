from Helpers.helpings import *

# Set True only when you explicitly want to test child-process behavior.
RUN_CHILD_MAIN = False

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
        1) How many times is count_down() called if the script calls count_down(5)?
        # ⭐ val: 6
        2) How many times is count_down() called if the script calls count_down(0)?
        # ⭐ val: 1
        3) Is there a difference in how we define the parameters of a recursive versus non-recursive function? Answer yes or no.
        # ⭐ val: no
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
        1) If a sorted list has elements numbered 0 to 50 and the item being searched for happens to be at location 6, how many times will the find() function be called?
        # ⭐ val: 3
        2) If an alphabetically sorted list (ascending) has elements numbered 0 to 50, and the item at element 0 is "Bananas", how many recursive calls to find() will be made during the failed search for "Apples"?
        # ⭐ val: 7
        3) A list of 5 elements is: A B D E F. A is element 0 and F is element 4. find(lst,"C",0,4) is called to search for item C. Write the last call to find() that would occur when searching for item C.
        # ⭐ val: find(lst, "C",2,2)
 
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
    # val: Scratch(a=['A', 'B', 'D', 'E', 'F'], find=<function __sc_14__.<locals>.__sc_13__.<locals>.find at 0x7c310231b380>, out=['Searching range from index 0 to 4', 'Searching range from index 0 to 2', 'Searching range from index 2 to 2', 'C is not in the list'], err=[], outs='Searching range from index 0 to 4\nSearching range from index 0 to 2\nSearching range from index 2 to 2\nC is not in the list')
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
    
########################################################################################################
INFO()
# val: /workspaces/Python-Copy2/sandbox/files
# val: Sun May  3 22:56:08 UTC 2026
# val: ./test.py
# val: ./_.txt
# val: ./main.py
# val: ./temp.py
# val: ./
# val:     count_down(5)
# val:     
# val: ./C_14_MD/        # ⭐ val: 6        count_down(5)        # ⭐ val: None        # ⭐f.out: 5        # ⭐f.out: 4        # ⭐f.out: 3        # ⭐f.out: 2        # ⭐f.out: 1        # ⭐f.out: Go!        
# val: ./C_14_MD/README
# val: ./
# val:         # ⭐ val: 6
# val:         count_down(5)
# val:         # ⭐ val: None
# val:         # ⭐f.out: 5
# val:         # ⭐f.out: 4
# val:         # ⭐f.out: 3
# val:         # ⭐f.out: 2
# val:         # ⭐f.out: 1
# val:         # ⭐f.out: Go!
# val:         

ret_file("./C_14_MD/README")
# val: # CS 2520 — ZyBooks C_14 Tracker
# val: ## Overview
# val: 
# val: - **Assignment:** C_14 (ZyBooks)
# val: - **Total:** 0 / 76 points
# val: - **Due:** May 14, 2026, 11:59 PM PDT
# val: 
# val: ## Quick Links (by section)
# val: 
# val: - [14.1](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/1)
# val: - [14.2](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/2)
# val: - [14.3](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/3)
# val: - [14.4](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/4)
# val: - [14.5](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/5)
# val: - [14.6](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/6)
# val: - [14.7 (Lab)](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/7)
# val: - [14.8 (Lab)](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/8)
# val: - [14.9](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/9)
# val: - [14.10 (Lab)](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/14/section/10)
# val: 
# val: ## Sections Breakdown (points)
# val: 
# val: | Section | Points | What it contains |
# val: | --- | --- | --- |
# val: | 14.1 | 0 / 6 | P: 1 + 3 pts • C: 2 pts |
# val: | 14.2 | 0 / 9 | P: 1 + 3 pts • C: 3 + 1 + 1 pts |
# val: | 14.3 | 0 / 3 | P: 3 pts |
# val: | 14.4 | 0 / 8 | P: 1 + 3 pts • C: 1 + 3 pts |
# val: | 14.5 | 0 / 4 | P: 2 pts • C: 2 pts |
# val: | 14.6 | 0 / 6 | P: 1 + 2 pts • C: 2 + 1 pts |
# val: | 14.7 | 0 / 10 | Lab: 10 pts |
# val: | 14.8 | 0 / 10 | Lab: 10 pts |
# val: | 14.9 | 0 / 10 | (Not itemized in scrape) |
# val: | 14.10 | 0 / 10 | Lab: 10 pts |
# val: 
# val: ## Checklist Tracker (do in order)
# val: 
# val: ### 14.1 — 0 / 6
# val: 
# val: - [ ]  14.1.1 Participation (1 pt)
# val: - [ ]  14.1.2 Participation (3 pts)
# val: - [ ]  14.1.1 Challenge (2 pts)
# val: 
# val: ### 14.2 — 0 / 9
# val: 
# val: - [ ]  14.2.1 Participation (1 pt)
# val: - [ ]  14.2.2 Participation (3 pts)
# val: - [ ]  14.2.1 Challenge (3 pts)
# val: - [ ]  14.2.2 Challenge (1 pt)
# val: - [ ]  14.2.3 Challenge (1 pt)
# val: 
# val: ### 14.3 — 0 / 3
# val: 
# val: - [ ]  14.3.1 Participation (3 pts)
# val: 
# val: ### 14.4 — 0 / 8
# val: 
# val: - [ ]  14.4.1 Participation (1 pt)
# val: - [ ]  14.4.2 Participation (3 pts)
# val: - [ ]  14.4.1 Challenge (1 pt)
# val: - [ ]  14.4.2 Challenge (3 pts)
# val: 
# val: ### 14.5 — 0 / 4
# val: 
# val: - [ ]  14.5.1 Participation (2 pts)
# val: - [ ]  14.5.1 Challenge (2 pts)
# val: 
# val: ### 14.6 — 0 / 6
# val: 
# val: - [ ]  14.6.1 Participation (1 pt)
# val: - [ ]  14.6.2 Participation (2 pts)
# val: - [ ]  14.6.1 Challenge (2 pts)
# val: - [ ]  14.6.2 Challenge (1 pt)
# val: 
# val: ### 14.7 — Lab — 0 / 10
# val: 
# val: - [ ]  14.7.1 Lab (10 pts)
# val: 
# val: ### 14.8 — Lab — 0 / 10
# val: 
# val: - [ ]  14.8.1 Lab (10 pts)
# val: 
# val: ### 14.9 — 0 / 10
# val: 
# val: - [ ]  Complete section 14.9 (10 pts)
# val: 
# val: ### 14.10 — Lab — 0 / 10
# val: 
# val: - [ ]  14.10.1 Lab (10 pts)
# val: 
# val: ## Next Steps
# val: 
# val: 1. Do **14.1** (fast points).
# val: 2. Then **14.2**.
# val: 3. Save labs (14.7, 14.8, 14.10) for a focused coding block.

# in: 1
with "test.py" as Scratch:
    #input test
    def count_down(count):
        count
        # val: 1
        # val: 0
        if count == 0:
            count            
            # val: 0
            print('Go!')                  
            # out: Go!
        else:
            count                        
            # val: 1
            print(count)             
            # out: 1
                
            count_down(count-1)
            # val: None
            count        
            # val: 1
    ins=input("test:")
    # out: test:1
    count_down(int(ins))
    # val: None

remove_path("./test.py")
# val: PosixPath('/workspaces/Python-Copy2/sandbox/files/test.py')
