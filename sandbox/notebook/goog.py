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
