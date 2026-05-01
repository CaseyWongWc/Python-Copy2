########################################################################################################
'''Activity summary for assignment: C_12
1 / 70 points
Due: 05/07/2026, 11:59 PM PDT

Completion details
Section 12.1
1 / 8 points
P
Participation activities
12.1.1
1 / 1 point
12.1.2
0 / 3 points
C
Challenge activities
12.1.1
0 / 4 points

Section 12.2
0 / 11 points
P
Participation activities
12.2.1
0 / 3 points
12.2.2
0 / 1 point
12.2.3
0 / 3 points
C
Challenge activities
12.2.1
0 / 4 points

Section 12.3
0 / 7 points
P
Participation activities
12.3.1
0 / 1 point
12.3.2
0 / 3 points
12.3.3
0 / 3 points

Section 12.4
0 / 6 points
P
Participation activities
12.4.1
0 / 4 points
12.4.2
0 / 2 points

Section 12.5
0 / 2 points
P
Participation activities
12.5.1
0 / 2 points

Section 12.6
0 / 4 points
P
Participation activities
12.6.1
0 / 2 points
C
Challenge activities
12.6.1
0 / 2 points

Section 12.7
0 / 2 points
P
Participation activities
12.7.1
0 / 2 points

Section 12.8
0 / 10 points
L
Lab activities
12.8.1
0 / 10 points

Section 12.9
0 / 10 points
L
Lab activities
12.9.1
0 / 10 points

Section 12.12
0 / 10 points
L
Lab activities
12.12.1
0 / 10 points
'''
##################################################################################################################################
'''## 12.1 Reading files

### Reading from a file

A common programming task is to retrieve input from a file using the built-in open() function instead of using keyboard entry.

### PARTICIPATION ACTIVITY: Reading text from a file.

Static Figure: Begin Python code:
myjournal = open("journal.txt")

contents = myjournal.read()

# print contents ....
End Python code. The variable myjournal is a file object for the file journal.txt. The variable contents is a string that contains the content of the file.
Step 1: The open function creates a file object. The read function saves the content of the file as a string. The line of code myjournal = open("journal.txt") is highlighted. The variable myjournal is created for the file journal.txt. The line of code contents = myjournal.read() is highlighted. The file journal.txt is scanned and the content of the file is stored in the variable contents as a string. The line of code # print contents .... is highlighted. The string "Dear journal, Today I learned Python.... " is printed.

Assume a text file exists named "myfile.txt" with the contents shown (created, for example, using Notepad on a Windows computer or using TextEdit on a Mac computer).

> **Creating a file object and reading text.**
> ```python
> print("Opening file myfile.txt.")
> f = open("myfile.txt")  # create file object
> 
> print("Reading file myfile.txt.")
> contents = f.read()  # read file text into a string
> 
> print("Closing file myfile.txt.")
> f.close()  # close the file
> 
> print("\nContents of myfile.txt:")
> print(contents)
> ```
> ```
> Because he's the hero Gotham deserves,
> but not the one it needs right now.
> ```

The open() built-in function requires a single argument that specifies the path to the file. Ex: `open("myfile.txt")` opens myfile.txt located in the same directory as the executing script. Full path names can also be specified, as in `open("C:\\Users\\BWayne\\tax_return.txt")`. The file.close() method closes the file, after which no more reads or writes to the file are allowed.

The most common methods to read text from a file are file.read() and file.readlines(). The file.read() method returns the file contents as a string. The file.readlines() method returns a list of strings, where the first element is the contents of the first line, the second element is the contents of the second line, and so on. Both methods can be given an optional argument that specifies the number of bytes to read from the file. Each method stops reading when the end-of-file (EOF) is detected, which indicates no more data is available.

A third method, file.readline(), returns a single line at a time, which is useful when dealing with large files where the entire file contents may not fit into the available system memory.

### PARTICIPATION ACTIVITY: Opening files and reading text.

my_file =

**1.** Complete the statement to open the file "readme.txt" for reading.
Answer: open("readme.txt") or open('readme.txt') or open("readme.txt", "r") or open('readme.txt', 'r') or open("readme.txt","r") or open('readme.txt','r')
*Hint: Use the open() function.*
*The open() function opens the specified file and returns a new file object.*

my_file = open("readme.txt") 

contents =

**2.** Complete the statement to read up to 500 bytes from "readme.txt" into the contents variable. # ....
Answer: my_file.read(500)
*Hint: Use the file.read() method, and specify the optional argument to limit the amount of read data.*
*The optional argument to the file.read() method limits the number of bytes read.*

my_file = open("readme.txt") 

lines = my_file.readlines() 

print(

**3.** Complete the program by printing the second line of "readme.txt". )
# ....
Answer: lines[1]
*Hint: The readlines() method returns a list containing each line as an element. Print the second line from the list.*
*my_file.readlines() reads the contents of readme.txt and stores each line as an element in the "lines" list.*

### Processing data from a file

One of the most common programming tasks is to read data from a file and then process that data to produce a useful result. Sometimes the data is a string, as in the example above, but often the data is a numeric value. Each unique data value is often placed on its own line. Thus, a program commonly 1) reads the contents of a file, 2) iterates over each line to process data values, and 3) computes some value, such as the average value.

> **Calculating the average of data values stored in a file.**
> The file "mydata.txt" contains 100 integers, each on its own line:
> ```python
> # Read file contents
> print ("Reading in data....")
> f = open("mydata.txt")
> lines = f.readlines()
> f.close()
> 
> # Iterate over each line
> print("\nCalculating average....")
> total = 0
> for ln in lines:
>     total += int(ln)
> 
> # Compute result
> avg = total/len(lines)
> print(f"Average value: {avg}")
> ```
> ```
> 105
> 65
> 78
> ....
> ```

Iterating over each line of a file is so common that file objects support iteration using the `for .... in` syntax. The below example echoes the contents of a file:

> **Iterating over the lines of a file.**
> ```python
> """Echo the contents of a file."""
> f = open("myfile.txt")
> 
> for line in f:
>     print(line, end="")
> 
> f.close()
> ```

### CHALLENGE ACTIVITY: Reading files. (4 Levels)

**Level 1:**

**Task:**
Complete the assignment of [...] by calling [...]'s [...]

**Explanation pattern:**
Variable [...] is assigned with the [...]

**Code structure:**
```python
___ = open(input())

___
""" Your code goes here """ ___
import builtins

original_open = builtins.open

class File(object):
    read_called = False

    def __init__(self, path, *args, **kwargs):
        self._fobj = original_open(path, *args, **kwargs)

    def read(self, n_bytes = -1):
        self.read_called = True
        return self._fobj.read(n_bytes)
    def readline(self, size=-1):
        self.read_called = True
        return self._fobj.readline(size)
    def readlines(self, hint=None):
        self.read_called = True
        return self._fobj.readlines(hint)
    def readall(self):
        self.read_called = True
        return self._fobj.readall()
    def readinto(self, b):
        self.read_called = True
        self._fobj.readinto(b)
    def _readinto(self, b, read1):
        self.read_called = True
        self._fobj._readinto(b, read1)
    def write(self, b):
        self._fobj.write(b)
    def writelines(self, lines):
        self._fobj.writelines(lines)
    def seek(self, pos, whence=0):
        self._fobj.seek(pos, whence)
    def __iter__(self):
        self.read_called = True
        return self._fobj.__iter__()
    def __next__(self):
        return self._fobj.__next__()
    def close(self):
        self._fobj.close()

def fileopen(path, *args, **kwargs):
    fobj = File(path, *args, **kwargs)
    return fobj

__builtins__.open = fileopen

import main

if not main.___.read_called:
    print('Error: ___ is not read')
```

**Level 2:**

**Task:**
Variable [...] is assigned with a file's name read from input. Perform the following tasks: Open the file named [...], and assign [...] with the file object.
[...]
Close [...].

**Explanation pattern:**
`open([...])` opens the file named [...] for reading. Variable [...] is assigned with the file object returned by `open()`. [...] Variable [...]'s `close()` closes [...].

**Code structure:**
```python
___ = input()
""" Your code goes here """
import main

try:
    if not main.___.closed:
        print('Error: ___ is not closed')
except:
    print('Error: Variable ___ is not found')
```

**Level 3:**

**Task:**
Complete the for loop to read each line from [...] into [...] using the syntax `for ... in ...`.

**Explanation pattern:**
`for [...] in [...]` assigns [...] with each line of [...]'s contents.

**Code structure:**
```python
___ = open(input())

for ___
""" Your code goes here """
___:
    # Each line read from the file ends with a newline.
    print(___, end="")  # end="" prints each line without adding another newline.
print()

___.close()
import builtins

original_open = builtins.open

class File(object):
    read_called = False

    def __init__(self, path, *args, **kwargs):
        self._fobj = original_open(path, *args, **kwargs)

    def read(self, n_bytes = -1):
        self.read_called = True
        return self._fobj.read(n_bytes)
    def readline(self, size=-1):
        self.read_called = True
        return self._fobj.readline(size)
    def readlines(self, hint=None):
        self.read_called = True
        return self._fobj.readlines(hint)
    def readall(self):
        self.read_called = True
        return self._fobj.readall()
    def readinto(self, b):
        self.read_called = True
        self._fobj.readinto(b)
    def _readinto(self, b, read1):
        self.read_called = True
        self._fobj._readinto(b, read1)
    def write(self, b):
        self._fobj.write(b)
    def writelines(self, lines):
        self._fobj.writelines(lines)
    def seek(self, pos, whence=0):
        self._fobj.seek(pos, whence)
    def __iter__(self):
        self.read_called = True
        return self._fobj.__iter__()
    def __next__(self):
        return self._fobj.__next__()
    def close(self):
        self._fobj.close()

def fileopen(path, *args, **kwargs):
    fobj = File(path, *args, **kwargs)
    return fobj

__builtins__.open = fileopen

import main

if not main.___.read_called:
    print('Error: ___ is not read')
```

**Level 4:**

**Task:**
[...] Complete the for loop [...]

**Code structure:**
```python
""" Your code goes here """
import builtins

original_open = builtins.open

class File(object):
    read_called = False

    def __init__(self, path, *args, **kwargs):
        self._fobj = original_open(path, *args, **kwargs)

    def read(self, n_bytes = -1):
        self.read_called = True
        return self._fobj.read(n_bytes)
    def readline(self, size=-1):
        self.read_called = True
        return self._fobj.readline(size)
    def readlines(self, hint=None):
        self.read_called = True
        return self._fobj.readlines(hint)
    def readall(self):
        self.read_called = True
        return self._fobj.readall()
    def readinto(self, b):
        self.read_called = True
        self._fobj.readinto(b)
    def _readinto(self, b, read1):
        self.read_called = True
        self._fobj._readinto(b, read1)
    def write(self, b):
        self._fobj.write(b)
    def writelines(self, lines):
        self._fobj.writelines(lines)
    def seek(self, pos, whence=0):
        self._fobj.seek(pos, whence)
    def __iter__(self):
        self.read_called = True
        return self._fobj.__iter__()
    def __next__(self):
        return self._fobj.__next__()
    def close(self):
        self._fobj.close()

def fileopen(path, *args, **kwargs):
    fobj = File(path, *args, **kwargs)
    return fobj

__builtins__.open = fileopen

import main

if not main.___.read_called:
    print('Error: ___ is not read')
```
'''
##########################
'''participation activity
12.1.2: Opening files and reading text.
1)
Complete the statement to open the file "readme.txt" for reading.
my_file = 


Check

Show answer
2)
Complete the statement to read up to 500 bytes from "readme.txt" into the contents variable.
my_file = open("readme.txt") 

contents = 

# ....

Check

Show answer
3)
Complete the program by printing the second line of "readme.txt".
my_file = open("readme.txt") 

lines = my_file.readlines() 

print(
)
# ....

Check

Show answer

Feedback?'''





#from Helpers.helpings import make_file, remove_path, remove_path


#from Helpers.helpings import make_file


#from Helpers.helpings import make_file, remove_path


from ast import Del


from ast import Del


[
    {"a": 1},
    {"b": 2},
]

'''activity
12.1.1: Reading files.
712910.5105864.qx3zqy7

Jump to level 1
Complete the assignment of beet_data by calling beet_file's readlines() to read beet_file's contents as a list of strings, where each string is a line in beet_file.

Click here for example
Ex: If the input is data1.txt and:
Contents of file data1.txt
Taj 31
Eve 14
Fay 34

then the output is:

['Taj 31\n', 'Eve 14\n', 'Fay 34']

main.py
beet_file = open(input())

beet_data = beet_file.readlines()

beet_file.close()

print(beet_data)
data1.txt
Taj 31
Eve 14
Fay 34
data2.txt
Jan 8
Bob 6
data3.txt
Abe 27
Mel 38
Ana 23
Del 18
'''
def temp():
    beet_file = open(input())

    beet_data = beet_file.readlines()

    beet_file.close()

    print(beet_data)
1
##########################
'''challenge activity
12.1.1: Reading files.
712910.5105864.qx3zqy7

Jump to level 1
Variable src_name is assigned with a file's name read from input. Perform the following tasks:

Open the file named src_name, and assign tie_file with the file object.
Use tie_file's read() to read the contents of src_name and assign tie_data with the string read.
Close tie_file.
Click here for example

main.py
src_name = input()

""" Your code goes here """

print(tie_data)
data1.txt
Ana violet
Dan brown
Gus sienna
data2.txt
Rob brick
Ben brown
data3.txt
Dan magenta
Aya indigo
Abe brown
Val tan
1

2

3

4

Check

Next level
1
2
3
'''

#make_file("data1.txt", "Ana violet\nDan brown\nGus sienna\n")
#make_file("data2.txt", "Rob brick\nBen brown\n")
#make_file("data3.txt", "Dan magenta\nAya indigo\nAbe brown\nVal tan\n")
#make_file("temp.py", '''
#src_name = input()
#tie_file = open(src_name)
#tie_data = tie_file.read()
#tie_file.close()
#print(tie_data)
#''')
#remove_path("temp.py")
#remove_path("data1.txt")
#remove_path("data2.txt")
#remove_path("data3.txt")

##########################
'''challenge activity
12.1.1: Reading files.
712910.5105864.qx3zqy7

Jump to level 1
Complete the for loop to read each line from beet_file into input_line using the syntax for ... in ....

Click here for example
Ex: If the input is data1.txt and:
Contents of file data1.txt
Bob 17
Rob 30

then the output is:

Bob 17
Rob 30

main.py
beet_file = open(input())

for input_line """ Your code goes here """:
    # Each line read from the file ends with a newline.
    print(input_line, end="")  # end="" prints each line without adding another newline.
print()

beet_file.close()
data1.txt
Bob 17
Rob 30
data2.txt
Cam 6
Aya 10
Dax 24
Zoe 25
data3.txt
Meg 6
Pat 27
Gus 28







1

2

3

4

Check

Next level
1
2
3
4

Feedback?'''

def none():
    beet_file = open(input())

    for input_line in beet_file:
        # Each line read from the file ends with a newline.
        print(input_line, end="")  # end="" prints each line without adding another newline.
    print()

    beet_file.close()
pass



with Scratch as a:
    with "data1.txt":
        Tia 31
        Eve 14
        Fay 34
    with "data2.txt":
        Jan 8
        Bob 6
    with "data3.txt":
        Abe 27
        Mel 38
        Ana 23
        Del 18
    with "temp.py":
        src_name = input()
        tie_file = open(src_name)
        tie_data = tie_file.read()
        tie_file.close()
        print(tie_data)
# !err: --- ERROR ---
# !err: Traceback (most recent call last):
# !err:   File "<string>", line 59, in <module>
# !err:   File "/home/codespace/.python/current/lib/python3.12/ast.py", line 52, in parse
# !err:     return compile(source, filename, mode, flags,
# !err:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# !err:   File "/workspaces/Python-Copy2/sandbox/notebook/goog.py", line 718
# !err:     print(tie_data)
# !err: IndentationError: expected an indented block after 'with' statement on line 700
