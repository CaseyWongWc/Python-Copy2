import sys
from pathlib import Path

NOTEBOOK_DIR = Path(__file__).resolve().parent
if str(NOTEBOOK_DIR) not in sys.path:
    sys.path.insert(0, str(NOTEBOOK_DIR))
    # val: None

from Helpers.helpings import *

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
# out: teal
# out: violet
# out: Enter year: 2009
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

#from old.inline_output import _strip_old_annotations


[
# val: [{'a': 1}, {'b': 2}]
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
# val: 1
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


'''    beet_file = open(input())

    for input_line in beet_file:
        # Each line read from the file ends with a newline.
        print(input_line, end="")  # end="" prints each line without adding another newline.
    print() 

    beet_file.close()'''
def none():
    beet_file = open(input())
    # out: data1.txt

    for input_line in beet_file:
        # Each line read from the file ends with a newline.
        print(input_line, end="")  # end="" prints each line without adding another newline.
        # out: violet
    print()
    # out: 

    beet_file.close()
    # val: None
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
    a=open("data1.txt")
    # in: data1.txt
    none()
    # val: None
    with "temp.py":
        src_name = input()
        tie_file = open(src_name)
        tie_data = tie_file.read()
        tie_file.close()
        print(tie_data)
    with open("temp.py", "r") as f:
        f.read()
        # val: src_name = input()
        # val: tie_file = open(src_name)
        # val: tie_data = tie_file.read()
        # val: tie_file.close()
        # val: print(tie_data)
        f.close()
        # val: None
##########################
'''challenge activity
12.1.1: Reading files.
712910.5105864.qx3zqy7

Jump to level 1
Each line in kiwi_file contains an integer representing the number of kiwis bought in a day. Complete the for loop to assign kiwi_sum with the sum of all the integers in kiwi_file.

Click here for example
Ex: If the input is data1.txt and:
Contents of file data1.txt
1
19
7

then the output is:

Total number of kiwis bought: 27

main.py
kiwi_file = open(input())

kiwi_sum = 0
for line in kiwi_file:
    """ Your code goes here """

kiwi_file.close()

print(f"Total number of kiwis bought: {kiwi_sum}")
data1.txt
1
19
7
data2.txt
7
14
13
10
data3.txt
2
18'''
'''
    kiwi_file = open(input())
    kiwi_sum = 0
    for line in kiwi_file:
        kiwi_sum += int(line)
    kiwi_file.close()
    print(f"Total number of kiwis bought: {kiwi_sum}")'''
with Scratch as a:
    with "data1.txt":
        1
        19
        7
    with "data2.txt":
        7
        14
        13
        10
    with "data3.txt":
        2
        18
    kiwi_file = open("data1.txt")
    # in: data1.txt
    kiwi_sum = 0
    for line in kiwi_file:
        stripped = line.strip()
        if stripped.lstrip("-").isdigit():
            kiwi_sum += int(stripped)
    kiwi_file.close()
    # val: None
    print(f"Total number of kiwis bought: {kiwi_sum}")
    # out: Total number of kiwis bought: 0
##############################################################################
'''12.2 Writing files
Writing to a file
Programs write to a file to store data permanently. The file.write() method writes a string argument to a file.

Figure 12.2.1: Writing to a file.
f = open("myfile.txt", "w")  # Open file
f.write("Example string:\n  test....")  # Write string
f.close()  # Close the file
Final contents of myfile.txt:
Example string:
  test....

Feedback?
The write() method accepts a string argument only. Integers and floating-point values must first be converted using str(), as in f.write(str(5.75)).

Figure 12.2.2: Numeric values must be converted to strings.
num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open("myfile.txt", "w")
f.write(str(num1))
f.write(" + ")
f.write(str(num2))
f.write(" = ")
f.write(str(num3))
f.close()
Final contents of myfile.txt:
5 + 7.5 = 12.5

Feedback?
When writing to a file, the mode of the file must be explicitly set in the open() function call. A mode indicates how a file is opened, such as whether or not writing to the file is allowed, if existing contents of the file are overwritten or appended, etc. The most used modes are "r" (read) and "w" (write). The mode is specified as the second argument in a call to open(), e.g., open("myfile.txt", "w") opens myfile.txt for writing. If mode is not specified the default is "r".

The below table lists common file modes:

Table 12.2.1: Modes for opening files.
Mode	Description	Allow read?	Allow write?	Create missing file?	Overwrite file?
"r"	Open the file for reading.	Yes	No	No	No
"w"	Open the file for writing. If the file does not exist, then the file is created. Contents of an existing file are overwritten.	No	Yes	Yes	Yes
"a"	Open the file for appending. If the file does not exist, then the file is created. Writes are added to the end of existing file contents.	No	Yes	Yes	No

Feedback?
Read mode "r" opens a file for reading. If the file is missing, then an error will occur.
Write mode "w" opens a file for writing. If the file is missing, then a new file is created. Contents of any existing file are overwritten.
Append mode "a" opens a file for writing. If the file is missing, then a new file is created. Writes to the file are appended to the end of an existing file's contents.
Additionally, a programmer can add a "+" character to the end of a mode, like "r+" and "w+" to specify an update mode. Update modes allow for both reading and writing of a file at the same time.

participation activity
12.2.1: File modes.
For each question, complete the statement to open myfile.txt with the appropriate mode.

1)
Data will be appended to the end of existing contents.
f = open("myfile.txt", "
")

Check

Show answer
2)
If the file exists, existing contents will be overwritten by new data. If not, data will be written to a new file.
f = open("myfile.txt", "
")

Check

Show answer
3)
Existing contents will be read, and new data will be appended.
f = open("myfile.txt", "
")

Check

Show answer

Feedback?
Output buffer
Output to a file is buffered by the interpreter before being written to the computer's hard disk. By default, data is line-buffered, meaning data is written to disk only when a newline character is output. Thus, there may be a delay between a call of write() and writing that data to the disk. The following illustrates:

participation activity
12.2.2: Output is buffered.

Start
Interpretermyfile =     (            ,    )

myfile.write(     )
myfile.write(   )


myfile.write(    ) 
open "myfile.txt"  "w"

"Num"
"5"


"\n"
# End of line - write buffer
buffermyfile.txtNum5\n
Static Figure: Begin Python code: myfile = open("myfile.txt", "w") myfile.write("Num") myfile.write("5") # End of line - write buffer myfile.write("\n") End Python code. A representation of the interpreter and buffer. A file named myfile.txt with contents "Num5\n". Step 1: Statement myfile = open("myfile.txt", "w") executes, which opens a file named myfile.txt for writing. The line of code myfile = open("myfile.txt", "w") is highlighted. Step 2: Statement myfile.write("Num") executes. The interpreter stores "N", "u", and "m" in a buffer. The line of code myfile.write("Num") is highlighted. The character "N" is stored in the buffer. The character "u" is stored in the buffer. The character "m" is stored in the buffer. Step 3: Statement myfile.write("5") executes. The interpreter stores "5" in a buffer. The line of code myfile.write("5") is highlighted. The character "5" is stored in the buffer. Step 4: Statement myfile.write("\n") executes. The interpreter stores "\n" in a buffer. Writing a newline causes the buffer to be written to the file, so "Num5" is placed in myfile.txt. The character "\n" is stored in the buffer. The buffer is written to myfile.txt. myfile.txt now contains "Num5\n".

Captions

Feedback?
A programmer can toggle buffering on/off or specify a buffer size with the optional buffering argument to the open() function. Passing 0 disables buffering (valid only for binary files, discussed in another section), passing 1 enables the default line-buffering, and a value > 1 sets a specific buffer size in bytes. Ex:f = open("myfile.txt", "w", buffering=100) will write the output buffer to disk every 100 bytes.

The flush() file method can be called to force the interpreter to flush the output buffer to disk. Additionally, the os.fsync() function may have to be called on some operating systems. Closing an open file also flushes the output buffer.

Figure 12.2.3: Using flush() to force an output buffer to write to disk.
import os

# Open a file with default line-buffering.
f = open("myfile.txt", "w")

# No newline character, so not written to disk immediately
f.write("Write me to a file, please!")

# Force output buffer to be written to disk
f.flush()
os.fsync(f.fileno())

# ....

Feedback?
participation activity
12.2.3: Writing output.
1)
The statement f.write(10.0) always produces an error.
2)
The write() method immediately writes data to a file.
3)
The flush() method (and perhaps os.fsync()) forces the output buffer to write to disk.

Feedback?
challenge activity
12.2.1: Writing files.
712910.5105864.qx3zqy7

Start
Complete the following tasks:

Use open() to open dyes_data with the "w" option for writing.
Assign dyes_file with the opened file returned by open().
Click here for example
Note: The challenge activity will read and output the file named dyes_data.


main.py

data1.txt

data2.txt

data3.txt

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

Feedback?
How was this section?

|


Provide section feedback'''
####################################################
'''Writing to a file
Programs write to a file to store data permanently. The file.write() method writes a string argument to a file.

Figure 12.2.1: Writing to a file.
f = open("myfile.txt", "w")  # Open file
f.write("Example string:\n  test....")  # Write string
f.close()  # Close the file
Final contents of myfile.txt:
Example string:
  test....

Feedback?'''
with Scratch as a:
    with "myfile.txt":
        """ Your code goes here """
        f = open("myfile.txt", "w")  # Open file
        f.write("Example string:\n  test....")  # Write string
        f.close()  # Close the file
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: Example string:
        #⭐ val:   test....
        f.close()
        # val: None
    with open("names.txt", "r") as f:
        f.read()
        # val: Tia
        # val: Lynn
        # val: Ravi
        f.close()
        # val: None
####################################################
'''Figure 12.2.2: Numeric values must be converted to strings.
num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open("myfile.txt", "w")
f.write(str(num1))
f.write(" + ")
f.write(str(num2))
f.write(" = ")
f.write(str(num3))
f.close()
Final contents of myfile.txt:
5 + 7.5 = 12.5

Feedback?'''
with Scratch as a:
    with "myfile.txt":
        num1 = 5
        num2 = 7.5
        num3 = num1 + num2

        f = open("myfile.txt", "w")
        f.write(str(num1))
        f.write(" + ")
        f.write(str(num2))
        f.write(" = ")
        f.write(str(num3))
        f.close()
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
with Scratch as a:
    with "myfile.py":
        n1=5
        n2=7.5
        n3=n1+n2

        f=open("output.txt","w")
        f.write(str(n1))
        f.write(" + ")
        f.write(str(n2))
        f.write(" = ")
        f.write(str(n3))
        f.close()
    #not native
    cmd("python3","myfile.py")
    # val: Destination
    # val: Phoenix
    # val: Milan
    # val: London
    with open("output.txt", "r") as f:
        f.read()
        # val: 5 + 7.5 = 12.5
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
####################################################
'''Table 12.2.1: Modes for opening files.
Mode	Description	Allow read?	Allow write?	Create missing file?	Overwrite file?
"r"	Open the file for reading.	Yes	No	No	No
"w"	Open the file for writing. If the file does not exist, then the file is created. Contents of an existing file are overwritten.	No	Yes	Yes	Yes
"a"	Open the file for appending. If the file does not exist, then the file is created. Writes are added to the end of existing file contents.	No	Yes	Yes	No

Feedback?'''
with Scratch as a:
    with "myfile.txt":
        f = open("myfile.txt", "r")  # Open for reading
        f.close()
    with "myfile.txt":
        f = open("myfile.txt", "w")  # Open for writing
        f.close()
    with "myfile.txt":
        f = open("myfile.txt", "a")  # Open for appending
        f.close()
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
with Scratch as e:
    with open("my123.txt", "w") as f:
        f.write("Hello\n")
        # val: 6
    with open("my123.txt", "a") as f:
        f.write(" World\n")
        # val: 7
    with open("my123.txt", "a") as f:
        f.write(" Goodbye\n")
        # val: 9
    with open("my123.txt", "r") as f:
        f.read()
        # val: Hello
        # val:  World
        # val:  Goodbye
        f.close()
        # val: None
##########################
'''Read mode "r" opens a file for reading. If the file is missing, then an error will occur.
Write mode "w" opens a file for writing. If the file is missing, then a new file is created. Contents of any existing file are overwritten.
Append mode "a" opens a file for writing. If the file is missing, then a new file is created. Writes to the file are appended to the end of an existing file's contents.
Additionally, a programmer can add a "+" character to the end of a mode, like "r+" and "w+" to specify an update mode. Update modes allow for both reading and writing of a file at the same time.'''
# "+"
with Scratch as ae:
    with "myfile.txt":
        f = open("myfile.txt", "r+")  # Open for reading and writing
        f.close()
    with "myfile.txt":
        f = open("myfile.txt", "w+")  # Open for reading and writing, truncating the file first
        f.close()
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
####################################################
'''activity
12.2.1: File modes.
For each question, complete the statement to open myfile.txt with the appropriate mode.

1)
Data will be appended to the end of existing contents.
f = open("myfile.txt", "
")

Check

Show answer
2)
If the file exists, existing contents will be overwritten by new data. If not, data will be written to a new file.
f = open("myfile.txt", "
")

Check

Show answer
3)
Existing contents will be read, and new data will be appended.
f = open("myfile.txt", "
")

Check

Show answer

Feedback?'''
with Scratch as a:
    with "myfile.txt":
        f = open("myfile.txt", "a")  # Open for appending
        f.close()
    with "myfile.txt":
        f = open("myfile.txt", "w")  # Open for writing
        f.close()
    with "myfile.txt":
        f = open("myfile.txt", "a+")  # The "a+" mode opens the file for both reading and writing, appending new writes.
        f.close()
with Scratch as e:
    with "myfile.txt":
        1
    
    with open("myfile.txt", "a+") as f:
        f.write("2")
        # val: 1
        f.readline()
        # val: 
    #not native
    ret_file = open("myfile.txt", "r")
    ret_file.read()
    # val: buyers_file_name = input()
    # val: buyer_data = input()
    # val: with open(buyers_file_name, "a") as buyers_file:
    # val:     buyers_file.write(buyer_data)
    # val:     buyers_file.write("\n")
    # val: 2
####################################################
'''Output buffer
Output to a file is buffered by the interpreter before being written to the computer's hard disk. By default, data is line-buffered, meaning data is written to disk only when a newline character is output. Thus, there may be a delay between a call of write() and writing that data to the disk. The following illustrates:

participation activity
12.2.2: Output is buffered.


1

2

3

4

Statement myfile.write("\n") executes. The interpreter stores "\n" in a buffer. Writing a newline causes the buffer to be written to the file, so "Num5" is placed in myfile.txt.
Interpretermyfile =     (            ,    )

myfile.write(     )
myfile.write(   )


myfile.write(    ) 
open "myfile.txt"  "w"

"Num"
"5"


"\n"
# End of line - write buffer
buffermyfile.txtNum5\n
Static Figure: Begin Python code: myfile = open("myfile.txt", "w") myfile.write("Num") myfile.write("5") # End of line - write buffer myfile.write("\n") End Python code. A representation of the interpreter and buffer. A file named myfile.txt with contents "Num5\n". Step 1: Statement myfile = open("myfile.txt", "w") executes, which opens a file named myfile.txt for writing. The line of code myfile = open("myfile.txt", "w") is highlighted. Step 2: Statement myfile.write("Num") executes. The interpreter stores "N", "u", and "m" in a buffer. The line of code myfile.write("Num") is highlighted. The character "N" is stored in the buffer. The character "u" is stored in the buffer. The character "m" is stored in the buffer. Step 3: Statement myfile.write("5") executes. The interpreter stores "5" in a buffer. The line of code myfile.write("5") is highlighted. The character "5" is stored in the buffer. Step 4: Statement myfile.write("\n") executes. The interpreter stores "\n" in a buffer. Writing a newline causes the buffer to be written to the file, so "Num5" is placed in myfile.txt. The character "\n" is stored in the buffer. The buffer is written to myfile.txt. myfile.txt now contains "Num5\n".

Captions
Statement myfile = open("myfile.txt", "w") executes, which opens a file named myfile.txt for writing.
Statement myfile.write("Num") executes. The interpreter stores "N", "u", and "m" in a buffer.
Statement myfile.write("5") executes. The interpreter stores "5" in a buffer.
Statement myfile.write("\n") executes. The interpreter stores "\n" in a buffer. Writing a newline causes the buffer to be written to the file, so "Num5" is placed in myfile.txt.
Playing step 4: Statement myfile.write("\n") executes. The interpreter stores "\n" in a buffer. Writing a newline causes the buffer to be written to the file, so "Num5" is placed in myfile.txt. Step finished playing

Feedback?
A programmer can toggle buffering on/off or specify a buffer size with the optional buffering argument to the open() function. Passing 0 disables buffering (valid only for binary files, discussed in another section), passing 1 enables the default line-buffering, and a value > 1 sets a specific buffer size in bytes. Ex:f = open("myfile.txt", "w", buffering=100) will write the output buffer to disk every 100 bytes.

The flush() file method can be called to force the interpreter to flush the output buffer to disk. Additionally, the os.fsync() function may have to be called on some operating systems. Closing an open file also flushes the output buffer.

Figure 12.2.3: Using flush() to force an output buffer to write to disk.
import os

# Open a file with default line-buffering.
f = open("myfile.txt", "w")

# No newline character, so not written to disk immediately
f.write("Write me to a file, please!")

# Force output buffer to be written to disk
f.flush()
os.fsync(f.fileno())

# ....'''
#flush

with Scratch as a:
    with "myfile.txt":
        f = open("myfile.txt", "w")  # Open a file with default line-buffering.
        f.write("Write me to a file, please!")  # No newline character, so not written to disk immediately
        f.flush()  # Force output buffer to be written to disk
        import os
        os.fsync(f.fileno())
        f.close()
    with open("myfile.txt", "r") as f:
        f.read()
        # val: buyers_file_name = input()
        # val: buyer_data = input()
        # val: with open(buyers_file_name, "a") as buyers_file:
        # val:     buyers_file.write(buyer_data)
        # val:     buyers_file.write("\n")
        # val: 2
        f.close()
        # val: None
####################################################
'''participation activity
12.2.3: Writing output.
1)T/F
The statement f.write(10.0) always produces an error.
2)T/F
The write() method immediately writes data to a file.
3)T/F
The flush() method (and perhaps os.fsync()) forces the output buffer to write to disk.

Feedback?'''
with Scratch as a:
    with "myfile.txt":
        f = open("myfile.txt", "w")  # Open a file with default line-buffering.
        try:
            f.write(10.0)  # This will raise an error because write() expects a string argument.
        except TypeError:
            pass
        f.write("Hello")  # This will write "Hello" to the buffer, but not immediately to disk.
        f.flush()  # This will force the output buffer to be written to disk.
        import os
        os.fsync(f.fileno())  # This may be necessary on some operating systems to ensure data is written to disk.
        f.close()
    with "inconclusion.py":
        '''
        1)T
        2)F
        3)T
        '''
####################################################
'''challenge activity
12.2.1: Writing files.
712910.5105864.qx3zqy7

Jump to level 1
Complete the following tasks:

Use open() to open dyes_data with the "w" option for writing.
Assign dyes_file with the opened file returned by open().
Click here for example
Ex: If the input for dyes_data is data3.txt, new_dye is orange, and:

Contents of file data3.txt
green
beige

then the output comes from:

New contents of file data3.txt
orange


Note: The challenge activity will read and output the file named dyes_data.


main.py
dyes_data = input()
new_dye = input()

""" Your code goes here """

dyes_file.write(new_dye)
dyes_file.write("\n")
dyes_file.close()
data1.txt
violet

data2.txt
sienna
tan
indigo

data3.txt
green
beige
'''
with "main.py":
    dyes_data = input()
    new_dye = input()

    dyes_file = open(dyes_data, "w")  # Open the file for writing

    dyes_file.write(new_dye)  # Write the new dye to the file
    dyes_file.write("\n")  # Write a newline character to the file
    dyes_file.close()  # Close the file
with "data1.txt":
    violet

with "data2.txt":
    sienna
    tan
    indigo
with "data3.txt":
    green
    beige
with open("data3.txt", "r") as f:
    f.read()
    # val: teal
    f.close()
    # val: None
####################################################
'''challenge activity
12.2.1: Writing files.
712910.5105864.qx3zqy7

Jump to level 1
Close the file paints_file.

Click here for example
Ex: If the input for paints_data is data2.txt, new_paint is ochre, and:

Contents of file data2.txt
gray

then the output comes from:

New contents of file data2.txt
ochre


Note: The challenge activity will read and output the file named paints_data.


main.py
paints_data = input()
new_paint = input()

paints_file = open(paints_data, "w")
paints_file.write(new_paint)
paints_file.write("\n")

""" Your code goes here """

data1.txt
green
red
gold

data2.txt
gray

data3.txt
brown
gray
'''

with "main.py":
    paints_data = input()
    new_paint = input()

    paints_file = open(paints_data, "w")
    paints_file.write(new_paint)
    paints_file.write("\n")
    paints_file.close()  # Close the file

'''with "data1.txt":
    green
    red
    gold
with "data2.txt":
    gray
with "data3.txt":
    brown
    gray
with open("data2.txt", "r") as f:
    f.read()
    f.close()
'''
##########################
'''Write "Coordinates: <" to file_obj.
Write xcoord and ycoord to file_obj. Separate the two values with a comma (",").
Write ">" and a newline to file_obj.
Click here for example
Ex: If the input is :

7.0
14.0
then:

New contents of file data2.txt
Coordinates: <7.0,14.0>


Note: The challenge activity will read and output file "data2.txt".
file_obj = open("data2.txt", "w")
xcoord = float(input())
ycoord = float(input())

""" Your code goes here """

file_obj.close()

'''
with "main.py":
    file_obj = open("data2.txt", "w")
    xcoord = float(input())
    ycoord = float(input())

    with open("data2.txt", "w") as file_obj:
        file_obj.write("Coordinates: <")
        file_obj.write(str(xcoord))
        file_obj.write(",")
        file_obj.write(str(ycoord))
        file_obj.write(">\n")
    file_obj.close()


with Scratch as e:

    with "data2.txt":
        7.0
        14.0
    with open("data2.txt", "r") as f:
        f.read()
        # val: 7.0
        # val: 14.0
        f.close()
        # val: None
    #not native
    ret_file = open("data2.txt", "r")
    ret_file.read()
    # val: 7.0
    # val: 14.0
    # Skipping interactive cmd("python", "main.py") here because no stdin is provided
    # in this scratch run context.
####################################################
'''challenge activity
12.2.1: Writing files.
712910.5105864.qx3zqy7

Jump to level 1
Complete the following tasks:

Use open() to open colors_data with the "a+" update mode for reading and appending at the same time.
Assign colors_file with the opened file.
Click here for example
Ex: If the input for colors_data is data3.txt, one_color_val is violet, and:

Contents of file data3.txt
teal

then the output is:

teal
violet
Note: The challenge activity will read and output the file named colors_data.


main.py
colors_data = input()
one_color_val = input()

""" Your code goes here """

colors_file.write(one_color_val)
colors_file.flush()    # Forces the output buffer to write to disk

# When a file is in update mode, 
# seek(0, 0) rewinds the file to enable reading from the beginning
colors_file.seek(0, 0)  

file_data = colors_file.read()
print(file_data)

colors_file.close()
data1.txt
magenta
gold

data2.txt
green
brick
teal

data3.txt
teal

'''
with "main.py":
    colors_data = input()
    one_color_val = input()

    colors_file = open(colors_data, "a+")  # Open the file for reading and appending

    colors_file.write(one_color_val)  # Write the new color value to the file
    colors_file.flush()  # Forces the output buffer to write to disk

    # When a file is in update mode, seek(0, 0) rewinds the file to enable reading from the beginning
    colors_file.seek(0, 0)

    file_data = colors_file.read()  # Read the contents of the file
    print(file_data)  # Print the contents of the file

    colors_file.close()  # Close the file
 
with Scratch as e:
    def none():
        colors_data = input()
        one_color_val = input()

        colors_file = open(colors_data, "a+")  # Open the file for reading and appending

        colors_file.write(one_color_val)  # Write the new color value to the file
        # val: 6
        colors_file.flush()  # Forces the output buffer to write to disk
        # val: None

        # When a file is in update mode, seek(0, 0) rewinds the file to enable reading from the beginning
        colors_file.seek(0, 0)
        # val: 0

        file_data = colors_file.read()  # Read the contents of the file
        print(file_data)  # Print the contents of the file
        # out: violetvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletviolet

        colors_file.close()  # Close the file
        # val: None

    with "data3.txt":
        teal
    with open("data3.txt", "r") as f:
        f.read()
        # val: teal
        f.close()
        # val: None
    #not native
    ret_file = open("data3.txt", "r")
    t=ret_file.read()
    t
    # val: teal
    v="violet"
    v
    # val: violet
    setin(t,v)
    # val: None
    none()
    # val: None
    ret_file.close()
    # val: None
#ho my good lord that is so crazie
##############################################################################
'''12.3 Interacting with file systems
Interacting with a file system using the OS module
A program needs to interact with the computer's file system to get the size of a file or open a file in a different directory. The computer's operating system, such as Windows or macOS, controls the file system, and a program must use functions supplied by the operating system to interact with files. The Python standard library's OS module provides an interface to operating system function calls and is thus a critical piece of a Python programmer's toolbox.

participation activity
12.3.1: Using the OS module to interact with the file system.


1

2

3

4

When the os.remove() method executes, the interpreter calls on the operating system function DeleteFile("myfile.txt"), which removes myfile.txt from the hard disk.
import os

# ....

my_file = open("myfile.txt", "r")
# ....
file_info = os.stat("myfile.txt")
# ....
os.remove("myfile.txt")
Python interpreterOperating systemopen("myfile.txt", "r")HFILE WINAPI OpenFile("myfile.txt", ....)os.stat("myfile.txt")BOOL WINAPI GetFileInformationByHandle(....)myfile.txt[size, access time,etc.]os.remove("myfile.txt")BOOL WINAPI DeleteFile("myfile.txt")Hard disk
Static figure: Begin Python code: import os # .... my_file = open("myfile.txt", "r") # .... file_info = os.stat("myfile.txt") # .... os.remove("myfile.txt") End Python code. The line of code os.remove("myfile.txt") is highlighted. A representation of the Python interpreter contains the line os.remove("myfile.txt"). A representation of the operating system contains 'BOOL WINAPI DeleteFile("myfile.txt")'. The Python interpreter is connected to the operating system which is connected to the hard disk. Step 1: The statement import os provides an interface to operating system function calls. The line of code import os is highlighted. Step 2: When open("myfile.txt", "r") executes, the interpreter calls an operating system function to open the file (OpenFile() on Windows). The line of code my_file = open("myfile.txt", "r") is highlighted. The line is interpreted by the Python interpreter and sent to the operating system. The operating system executes HFILE WINAPI OpenFile("myfile.txt", ....). The file "myfile.txt" appears. Step 3: The os module's stat() method can query file information. In Windows, the GetFileInformationByHandle(....) provides information about the file size, access time, and more.The line of code file_info = os.stat("myfile.txt") is highlighted. The line is interpreted by the Python interpreter and sent to the operating system. The operating system executes BOOL WINAPI GetFileInformationByHandle(....).myfile.txt[size, access time, etc.] appears next to the file. Step 4: The line of code os.remove("myfile.txt") is highlighted. The line is interpreted by the Python interpreter and sent to the operating system. The operating system executes BOOL WINAPI DeleteFile("myfile.txt"). The file "myfile.txt" is removed.

Captions
The statement import os provides an interface to operating system function calls.
When open("myfile.txt", "r") executes, the interpreter calls an operating system function to open the file (OpenFile() on Windows).
The os module's stat() method can query file information. In Windows, the GetFileInformationByHandle(....) provides information about the file size, access time, and more.
When the os.remove() method executes, the interpreter calls on the operating system function DeleteFile("myfile.txt"), which removes myfile.txt from the hard disk.
Playing step 4: When the os.remove() method executes, the interpreter calls on the operating system function DeleteFile("myfile.txt"), which removes myfile.txt from the hard disk. Step finished playing

Feedback?
A programmer should consider the _portability_ of a program across different operating systems to avoid scenarios where the program behaves correctly on the programmer's computer but crashes on another. Portability, the ability to access an item easily from multiple locations, must be considered when reading and writing files outside the executing program's directory since file path representations often differ between operating systems. Ex: In Windows, the path to a file is represented as "subdir\\bat_mobile.jpg", but on a Mac, the path is "subdir/bat_mobile.jpg". The character between directories, "\\"or "/", is called the path separator, and using the incorrect path separator may result in that file not being found.1

A common error is to reduce a program's portability by hardcoding file paths as string literals with operating system specific path separators. To help reduce such errors, good practice is to use the os.path module, which contains many portable functions for handling file paths. One of the most useful functions is os.path.join(), which concatenates the arguments using the correct path separator for the current operating system. Instead of writing the literal path = "subdir\\bat_mobile.jpg", a programmer should write path = os.path.join("subdir", "bat_mobile.jpg"), which will result in "subdir\\bat_mobile.jpg" on Windows and "subdir/bat_mobile.jpg" on Linux/Mac.

Figure 12.3.1: Using os.path.join() to create a portable file path string.
The program below echoes the contents of logs stored in a hierarchical directory structure organized by date, using the os.path module to build a file path string that is portable across operating systems.

import os
import datetime

curr_day = datetime.date(1997, 8, 29)

num_days = 30
for i in range(num_days):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)

    # Build path string using current OS path separator
    file_path = os.path.join("logs", year, month, day, "log.txt")

    f = open(file_path, "r")
    
    print(f"{file_path}: {f.read()}")
    f.close()

    curr_day = curr_day + datetime.timedelta(days=1)
Output on Windows:
logs\\1997\\8\\29\\log.txt:  # ....
logs\\1997\\8\\30\\log.txt:  # ....
# ....
logs\\1997\\9\\28\\log.txt:  # ....
Output on Linux:
logs/1997/8/29/log.txt:  # ....
logs/1997/8/30/log.txt:  # ....
# ....
logs/1997/9/28/log.txt:  # ....

Feedback?
On Windows systems, when using os.path.join() with a full path so that the first argument is a drive letter, such as "C:" or "D:", the separator must be included with the drive letter. For example, os.path.join("C:\\", "subdir1", "myfile.txt") returns the string "C:\\subdir1\\myfile.txt".

The inverse operation, splitting a path into individual tokens, can be done using the str.split() method. Ex: tokens = "C:\\Users\\BWayne\\tax_return.txt".split(os.path.sep) returns ["C:", "Users", "BWayne", "tax_return.txt"]. os.path.sep stores the path separator for the current operating system.

participation activity
12.3.2: Portable file paths.
1)
Fill in the arguments to os.path.join to assign file_path as "subdir\\output.txt" (on Windows).
file_path = os.path.join(
)

Check

Show answer
2)
What is returned by os.path.join("sounds", "cars", "honk.mp3") on Windows? Use quotes in the answer.

Check

Show answer
3)
What is returned by os.path.join("sounds", "cars", "honk.mp3") on macOS? Use quotes in the answer.

Check

Show answer

Feedback?
More os.path functions
The os.path module contains other helpful functions, such as checking if a given path is a directory or a file, getting the size of a file, obtaining a file's extension (e.g., .txt, .doc, .pdf), and creating and deleting directories. Some of the most common functions are listed below:

os.path.split(path) – Splits a path into a two-tuple (head, tail), where tail is the last token in the path string and head is everything else.
import os
p = os.path.join("C:\\", "Users", "BWayne", "batsuit.jpg")
print(os.path.split(p))
("C:\\Users\\BWayne", "batsuit.jpg")
os.path.exists(path) – Returns True if path exists, else returns False.
import os
p = os.path.join("C:\\", "Users", "BWayne", "batsuit.jpg")
if os.path.exists(p):
    print("Suit up....")
else:
    print("The Lamborghini then?")
If file exists:
Suit up....

If file does not exist:
The Lamborghini then?
os.path.isfile(path) – Returns True if path is an existing file, and false otherwise (e.g., path is a directory).
import os
p = os.path.join("C:\\", "Users", "BWayne", "bat_chopper")
if os.path.isfile(p):
    print("Found a file....")
else:
    print("Not a file....")
If path is a file:
Found a file....

If path is not a file:
Not a file....
os.path.getsize(path) – Returns the size in bytes of path.
import os
p = os.path.join("C:\\", "Users", "BWayne", "batsuit.jpg")
print(f"Size of file: {os.path.getsize(p)} bytes")
Size of file: 65544 bytes
Explore the links at the end of the section to see all of the available functions in the os and os.path modules.

participation activity
12.3.3: Path name manipulation functions from os.path.
1)
What is the output of the following program?
import os
p = "C:\\Programs\\Microsoft\\msword.exe"
print(os.path.split(p))
2)
What does the call
os.path.isfile("C:\\Program Files\\")
return?
3)
What does os.path.getsize(path_str) return?

Feedback?
A programmer checks every file and/or subdirectory of a specific part of the file system. Consider the following directory structure, organized by year, month, and day:

Figure 12.3.2: Directory structure organized by date.
logs/
    2009/      
        April/
                1/
                 log.txt
                 words.doc                                     
        January/
               15/
                 log.txt
               21/
                 log.txt
                 temp23.pdf
               24/
                 presentation.ppt
    2010/
        March/
             3/
              log.txt
             7/
              music.mp3

Feedback?
The os.walk() function "walks" a directory tree like the one above, visiting each subdirectory in the specified path. The following example walks a user-specified year of the above directory tree.

Figure 12.3.3: Walking a directory tree.
import os

year = input("Enter year: ")
path = os.path.join("logs", year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, "contains subdirectories:", subdirs, end=" ")
    print("and the files:", files)
Enter year:2009

logs\\2009 contains subdirectories: ["April", "January"] and the files: []
logs\\2009\\April contains subdirectories: ["1"] and the files: []
logs\\2009\\April\\1 contains subdirectories: [] and the files: ["log.txt", "words.doc"]
logs\\2009\\January contains subdirectories: ["15", "21", "24"] and the files: []
logs\\2009\\January\\15 contains subdirectories: [] and the files: ["log.txt"]
logs\\2009\\January\\21 contains subdirectories: [] and the files: ["log.txt", "temp23.pdf"]
logs\\2009\\January\\24 contains subdirectories: [] and the files: ["presentation.ppt"]

Feedback?
The os.walk() function is used as the iterable object in a for loop that yields a three-tuple for each iteration.2 The first item, dirname, contains the path to the current directory. The second item, subdirs, is a list of all the subdirectories of the current directory. The third item, files, is a list of all the files residing in the current directory.

A programmer might use os.walk() when searching for specific files within a directory tree, and the exact path is unknown. Another task is to filter files based on their file extensions (.pdf, .txt, etc.), which are a convention used to indicate the type of data that a file holds.

Exploring further:
The os module: Miscellaneous operating system interfaces
The os.path module: Common pathname manipulations
(*1) Unix-based operating systems, such as Linux and macOS, will not recognize paths using the Windows separator "\\". Generally, Windows recognizes both "/" and "\\". The double backslash "\\" is the escape sequence to represent a single backslash within a string.

(*2) os.walk() actually returns a special object called a generator, which is discussed elsewhere.

How was this section?

|


Provide section feedback'''
####################################################
'''participation activity
12.3.1: Using the OS module to interact with the file system.'''
with Scratch as e:
    import os
    # ....
    my_file = open("myfile.txt", "r")
    print(my_file)
    # out: <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>
    # ....
    file_info = os.stat("myfile.txt")
    print(file_info)
    # out: os.stat_result(st_mode=33206, st_ino=1313074, st_dev=1796, st_nlink=1, st_uid=1000, st_gid=1000, st_size=160, st_atime=1777691790, st_mtime=1777691790, st_ctime=1777691790)
    # ....
    #os.remove("myfile.txt")
####################################################
'''participation activity
12.3.2: Portable file paths.
1)
Fill in the arguments to os.path.join to assign file_path as "subdir\\output.txt" (on Windows).
file_path = os.path.join(
)

Check

Show answer
2)
What is returned by os.path.join("sounds", "cars", "honk.mp3") on Windows? Use quotes in the answer.

Check

Show answer
3)
What is returned by os.path.join("sounds", "cars", "honk.mp3") on macOS? Use quotes in the answer.

Check

Show answer

Feedback?'''
with Scratch as a:
    import os
    file_path = os.path.join("subdir", "output.txt")
    print(file_path)
    # out: subdir/output.txt
    #⭐⭐⭐ out: subdir\output.txt⭐⭐⭐
    path_win = os.path.join("sounds", "cars", "honk.mp3")
    print(path_win)
    # out: sounds/cars/honk.mp3
    #⭐⭐⭐ out: sounds\cars\honk.mp3⭐⭐⭐
    path_mac = os.path.join("sounds", "cars", "honk.mp3")
    print(path_mac)
    # out: sounds/cars/honk.mp3
    #⭐⭐⭐ out: sounds/cars/honk.mp3⭐⭐⭐
with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
####################################################
'''
participation activity
12.3.3: Path name manipulation functions from os.path.

### PARTICIPATION ACTIVITY: Path name manipulation functions from os.path.

**1.** What is the output of the following program?
  
"""
import os
p = "C:\\Programs\\Microsoft\\msword.exe"
print(os.path.split(p))
"""
- ["C:\\", "Programs", "Microsoft", "msword.exe"]
- ("C:\\Programs\\Microsoft", "msword.exe") ✓
- ("C:", "Programs", "Microsoft", "msword.exe")
*os.path.split() returns a tuple containing the final item in the path as the second element, and everything else as the first element.*

**2.** What does the call`os.path.isfile("C:\\Program Files\\")` return?
- True
- False ✓
*os.path.isfile() returns True only if the argument is a file.*

**3.** What does os.path.getsize(path_str) return?
- The length of the path_str string.
- The combined size of all files in path_str directory.
- The size in bytes of the file at path_str. ✓
*os.path.getsize() yields the size in bytes of the file at the given path argument.*
'''
with Scratch as a:
    import os
    p = "C:\\Programs\\Microsoft\\msword.exe"
    print(os.path.split(p))
    # out: ('', 'C:\\Programs\\Microsoft\\msword.exe')
    #⭐ out: ('C:\\Programs\\Microsoft', 'msword.exe')
    print(os.path.isfile("C:\\Program Files\\"))
    # out: False
    #⭐ out: False
    #✅ Note: The output may vary based on the actual file system of the environment where this code is run.
    #✅⭐ os.path.getsize() cannot be demonstrated here without an actual file, but it would return the size in bytes of the file at the given path argument.
with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    import os
    try:
        size = os.path.getsize("C:\\Programs\\Microsoft\\msword.exe")
        print(f"File size: {size} bytes")
    except FileNotFoundError:
        print("File not found.")
        # out: File not found.
####################################################
'''A programmer checks every file and/or subdirectory of a specific part of the file system. Consider the following directory structure, organized by year, month, and day:

Figure 12.3.2: Directory structure organized by date.
logs/
    2009/      
        April/
                1/
                 log.txt
                 words.doc                                     
        January/
               15/
                 log.txt
               21/
                 log.txt
                 temp23.pdf
               24/
                 presentation.ppt
    2010/
        March/
             3/
              log.txt
             7/
              music.mp3

Feedback?
The os.walk() function "walks" a directory tree like the one above, visiting each subdirectory in the specified path. The following example walks a user-specified year of the above directory tree.

Figure 12.3.3: Walking a directory tree.
import os

year = input("Enter year: ")
path = os.path.join("logs", year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, "contains subdirectories:", subdirs, end=" ")
    print("and the files:", files)
Enter year:2009

logs\\2009 contains subdirectories: ["April", "January"] and the files: []
logs\\2009\\April contains subdirectories: ["1"] and the files: []
logs\\2009\\April\\1 contains subdirectories: [] and the files: ["log.txt", "words.doc"]
logs\\2009\\January contains subdirectories: ["15", "21", "24"] and the files: []
logs\\2009\\January\\15 contains subdirectories: [] and the files: ["log.txt"]
logs\\2009\\January\\21 contains subdirectories: [] and the files: ["log.txt", "temp23.pdf"]
logs\\2009\\January\\24 contains subdirectories: [] and the files: ["presentation.ppt"]

Feedback?
The os.walk() function is used as the iterable object in a for loop that yields a three-tuple for each iteration.2 The first item, dirname, contains the path to the current directory. The second item, subdirs, is a list of all the subdirectories of the current directory. The third item, files, is a list of all the files residing in the current directory.

A programmer might use os.walk() when searching for specific files within a directory tree, and the exact path is unknown. Another task is to filter files based on their file extensions (.pdf, .txt, etc.), which are a convention used to indicate the type of data that a file holds.

Exploring further:
The os module: Miscellaneous operating system interfaces
The os.path module: Common pathname manipulations
(*1) Unix-based operating systems, such as Linux and macOS, will not recognize paths using the Windows separator "\\". Generally, Windows recognizes both "/" and "\\". The double backslash "\\" is the escape sequence to represent a single backslash within a string.

(*2) os.walk() actually returns a special object called a generator, which is discussed elsewhere.'''
with Scratch as e:
    import os
    setin("2009")
    # val: None
    year = input("Enter year: ")
    path = os.path.join("logs", year)
    print()
    # out: 

    for dirname, subdirs, files in os.walk(path):
        print(dirname, "contains subdirectories:", subdirs, end=" ")
        print("and the files:", files)

with Scratch as e2:
    ####not native####
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    list_project_files()
    # val: ./myfile.txt
    # val: ./data2.txt
    # val: ./teal
    # val: ./mycsv2.csv
    # val: ./helpings.py
    # val: ./mycsv.py
    # val: ./mycsv3.py
    # val: ./lab_12_9/input3.csv
    # val: ./lab_12_9/input1.csv
    # val: ./lab_12_9/main.py
    # val: ./lab_12_9/input4.csv
    # val: ./lab_12_9/input2.csv
    # val: ./lab_12_9/main2.py
    # val: ./lab_12_9/input5.csv
    # val: ./main.py
    # val: ./Fig_12_5_1.py
    # val: ./myfile2.txt
    # val: ./lab_12_8.py
    # val: ./ball.bmp
    # val: ./gradeswr copy.csv
    # val: ./temp.py
    # val: ./data3.txt
    # val: ./.gitignore
    # val: ./myfile.py
    # val: ./gradeswr.csv
    # val: ./names.txt
    # val: ./inconclusion.py
    # val: ./mycsv2.py
    # val: ./to delete.py
    # val: ./myfile5.txt
    # val: ./my123.txt
    # val: ./.gitkeep
    # val: ./infile.txt
    # val: ./myfile.csv
    # val: ./myfile1.txt
    # val: ./Ron
    # val: ./lab_12_12/ParkPhotos2.txt
    # val: ./lab_12_12/main.py
    # val: ./lab_12_12/main2.py
    # val: ./lab_12_12/ParkPhotos.txt
    # val: ./lab_12_12/ParkPhotos3.txt
    # val: ./lab_12_12/ParkPhotos1.txt
    # val: ./lab_12_12/main3.py
    # val: ./lab.py
    # val: ./__pycache__/mycsv.cpython-312.pyc
    # val: ./output.txt
    # val: ./teal
    # val: 
    # val: ./lab_12_8/input1.txt
    # val: ./lab_12_8/main.py
    # val: ./lab_12_8/input3.txt
    # val: ./lab_12_8/input2.txt
    # val: ./my_script.py
    # val: ./data1.txt
    lsalf()
    # val: total 168
    # val: drwxrwxrwx+ 6 codespace codespace  4096 May  2 03:01 ./
    # val: drwxrwxrwx+ 5 codespace codespace  4096 May  1 18:47 ../
    # val: -rw-rw-rw-  1 codespace codespace    24 May  1 17:08 .gitignore
    # val: -rw-rw-rw-  1 codespace codespace     0 May  1 17:08 .gitkeep
    # val: -rw-rw-rw-  1 codespace codespace   762 May  2 00:04 Fig_12_5_1.py
    # val: -rw-rw-rw-  1 codespace codespace    10 May  2 00:45 Ron
    # val: drwxrwxrwx+ 2 codespace codespace  4096 May  2 01:38 __pycache__/
    # val: -rw-rw-rw-  1 codespace codespace 15286 May  1 22:52 ball.bmp
    # val: -rw-rw-rw-  1 codespace codespace     7 May  2 03:16 data1.txt
    # val: -rw-rw-rw-  1 codespace codespace     9 May  2 03:16 data2.txt
    # val: -rw-rw-rw-  1 codespace codespace     5 May  2 03:16 data3.txt
    # val: -rw-rw-rw-  1 codespace codespace    42 May  2 02:05 gradeswr copy.csv
    # val: -rw-rw-rw-  1 codespace codespace    44 May  2 03:01 gradeswr.csv
    # val: -rw-rw-rw-  1 codespace codespace  3106 May  1 18:57 helpings.py
    # val: -rw-rw-rw-  1 codespace codespace    20 May  2 03:16 inconclusion.py
    # val: -rw-rw-rw-  1 codespace codespace     5 May  2 03:01 infile.txt
    # val: -rw-rw-rw-  1 codespace codespace   337 May  2 02:23 lab.py
    # val: drwxrwxrwx+ 2 codespace codespace  4096 May  2 03:15 lab_12_12/
    # val: drwxrwxrwx+ 2 codespace codespace  4096 May  2 03:03 lab_12_8/
    # val: -rw-rw-rw-  1 codespace codespace   338 May  2 02:31 lab_12_8.py
    # val: drwxrwxrwx+ 2 codespace codespace  4096 May  2 02:56 lab_12_9/
    # val: -rw-rw-rw-  1 codespace codespace   545 May  2 03:16 main.py
    # val: -rw-rw-rw-  1 codespace codespace    22 May  2 03:16 my123.txt
    # val: -rw-rw-rw-  1 codespace codespace   762 May  2 03:16 my_script.py
    # val: -rw-rw-rw-  1 codespace codespace   456 May  2 03:16 mycsv.py
    # val: -rw-rw-rw-  1 codespace codespace   126 May  2 03:16 mycsv2.csv
    # val: -rw-rw-rw-  1 codespace codespace   136 May  2 03:16 mycsv2.py
    # val: -rw-rw-rw-  1 codespace codespace   364 May  2 03:16 mycsv3.py
    # val: -rw-rw-rw-  1 codespace codespace   126 May  2 03:01 myfile.csv
    # val: -rw-rw-rw-  1 codespace codespace   257 May  2 03:16 myfile.py
    # val: -rw-rw-rw-  1 codespace codespace   160 May  2 03:16 myfile.txt
    # val: -rw-rw-rw-  1 codespace codespace    80 May  2 03:16 myfile1.txt
    # val: -rw-rw-rw-  1 codespace codespace   284 May  2 03:16 myfile2.txt
    # val: -rw-rw-rw-  1 codespace codespace   187 May  2 03:16 myfile5.txt
    # val: -rw-rw-rw-  1 codespace codespace    14 May  1 17:08 names.txt
    # val: -rw-rw-rw-  1 codespace codespace    14 May  2 02:05 output.txt
    # val: -rw-rw-rw-  1 codespace codespace     6 May  1 20:58 teal
    # val: -rw-rw-rw-  1 codespace codespace  1410 May  2 03:16 teal
    # val: 
    # val: -rw-rw-rw-  1 codespace codespace   105 May  2 03:16 temp.py
    # val: -rw-rw-rw-  1 codespace codespace   921 May  2 03:12 to delete.py
    pass

##############################################################################
r'''12.4 Binary data
Binary data basics
Some files consist of data stored as a sequence of bytes, known as binary data, that is not encoded into readable text using an encoding like ASCII or UTF-8. Images, videos, and PDF files are examples of the types of files commonly stored as binary data. Opening such a file with a text editor displays text that is incomprehensible because the text editor attempts to encode raw byte values into readable characters.

A bytes object is used to represent a sequence of single byte values, such as binary data read from a file. Bytes objects are immutable, just like strings, meaning the value of a bytes object cannot change once created. A byte object can be created using the bytes() built-in function:

bytes("A text string", "ascii"): creates a sequence of bytes by encoding the string using ASCII
bytes(100): creates a sequence of 100 bytes whose values are all 0
bytes([12, 15, 20]): creates a sequence of 3 bytes with values from the list
Alternatively, a programmer can write a bytes literal, similar to a string literal, by prepending a "b" prior to the opening quote:

Figure 12.4.1: Creating a bytes object using a bytes literal.
my_bytes = b"This is a bytes literal"

print(my_bytes)
print(type(my_bytes))
b"This is a bytes literal"
<class "bytes">

Feedback?
A programmer can specify raw byte values in a string or bytes literal using the \x escape character preceding the hexadecimal value that describes the value of the byte. In the example below, the raw byte values 0x31 through 0x39 are automatically converted to the corresponding ASCII encoded values 1 - 9 when printed.

Figure 12.4.2: Byte string literals.
print(b"123456789 is the same as \x31\x32\x33\x34\x35\x36\x37\x38\x39")
b"123456789 is the same as 123456789"

Feedback?
Programs can also access files using a binary file mode by adding a "b" character to the end of the mode string in a call to open(), as in open("myfile.txt", "rb"). When using binary file mode "b" on a Windows computer, newline characters "\n" in the file are not automatically mapped to the Windows format "\r\n". In normal text mode, i.e., when not using the "b" binary mode, Python performs this translation of line-endings as a helpful feature, easing compatibility issues between Windows and other operating systems. In binary mode, the translation is not done because inserting additional characters would corrupt the binary data. On non-Windows systems, newline characters are not translated when using binary mode.

When a file is opened using a binary mode, the file.read() method returns a bytes object instead of a string. Also, the file.write() method expects a bytes argument.

participation activity
12.4.1: Binary Data.
1)
Open "data.txt" as read-only in binary mode.
f = open("data.txt", 
)

Check

Show answer
2)
Open "myfile.txt" as read-only in binary mode.
f = 


Check

Show answer
3)
Assign x with a bytes object with a single byte whose hexadecimal value is 0x1a. Use a bytes literal.
x = 


Check

Show answer
4)
Assign x with a bytes object containing three bytes with hexadecimal values 0x05, 0x15, and 0xf2. Use a bytes literal.
x = 


Check

Show answer

Feedback?
Altering the binary contents of a file
Consider a file ball.bmp that contains the following image:

Cartoon of a soccer ball on fire.
The ball.bmp file contains binary data in a format commonly called a bitmap (hence the .bmp extension at the end of the file name). Opening and reading the file with a binary mode creates a new bytes object consisting of the exact sequence of bytes found in the file's contents.

Figure 12.4.3: Inspecting the binary contents of an image file.
f = open("ball.bmp", "rb")  # Open in binary mode using "b"

# Read image binary data
contents = f.read()

print("Contents of ball.bmp:\n")
print(contents)

f.close()
Abbreviated output:
Contents of ball.bmp:

b"BMb\xe6\x00\x00\x00\x00\x00\x006\x04\x00\x00(\x00\x00\x00,\x01\x00\x00
\xc1\x00\x00\x00\x01\x00\x08\x00\x00\x00\x00\x00,\xe2\x00\x00\xc4"

Feedback?
The print(contents) statement displays the value of contents, converting each byte to human-readable character if that byte's value is a readable ASCII character (less than 128). The first portion of the file's contents is shown in the output, though the file portion is abbreviated because the image contains about 27,000 bytes. Note how the first 14 bytes of the bitmap file is "BMb\xe6\x00\x00\x00\x00\x00\x006\x04\x00\x00". This sequence constitutes the header of the binary file, which describes the bitmap's contents. The first 2 bytes "BM" indicates the type of bitmap. The following 4 bytes "b\xe6\x00\x00" indicates the size of the bitmap. The sequence "6\x04\x00\x00" indicates where in the file the RGB (red-green-blue) values for each pixel in the image are stored.

Example 12.4.1: Altering a BMP image file.
The following program reads in ball.bmp, overwrites a portion of the image with new pixel colors, and creates a new image file. Download the above image (click the link, "ball.bmp", above the image), and then run the program on your own computer, creating a new, altered version of ball.bmp. Try changing the alterations made by the program to get different colors.

import struct

ball_file = open("ball.bmp", "rb")
ball_data = ball_file.read()
ball_file.close()

# BMP image file format stores location
# of pixel RGB values in bytes 10-14
pixel_data_loc = ball_data[10:14]

# Converts byte sequence into integer object
pixel_data_loc = struct.unpack("<L", pixel_data_loc)[0]

# Create sequence of 3000 red, green, and yellow pixels each
new_pixels = b"\x01"*3000 + b"\x02"*3000 + b"\x03"*3000

# Overwrite pixels in image with new pixels
new_ball_data = ball_data[:pixel_data_loc] + \
              new_pixels + \
              ball_data[pixel_data_loc + len(new_pixels):]

# Write new image
new_ball_file = open("new_ball.bmp", "wb")
new_ball_file.write(new_ball_data)
new_ball_file.close()

One of a few sentences describing the item as precisely as possible for a blind person's screen reader, indicating main visual points. For question sets, a more thorough description may be necessary to ensure a student can answer questions.

Feedback?
The struct module
The struct module is a commonly used Python standard library module for packing values into sequences of bytes and unpacking sequences of bytes into values (like integers and strings). The struct.pack() function packs values such as strings and integers into sequences of bytes:

Figure 12.4.4: Packing values into byte sequences.
import struct

print("Result of packing 5:", end=" ")
print(struct.pack(">h", 5))

print("Result of packing 256:", end=" ")
print(struct.pack(">h", 256))

print("Result of packing 5 and 256:", end=" ")
print(struct.pack(">hh", 5, 256))
Result of packing 5: b"\x00\x05"
Result of packing 256: b"\x01\x00"
Result of packing 5 and 256: b"\x00\x05\x01\x00"

Feedback?
The first argument to struct.pack() is a format string that describes how the following arguments should be converted into bytes. The "<" character indicates the byte-order, or endianness, of the conversion, which determines whether the most significant or least significant byte is placed first in the byte sequence. ">" places the most significant byte first (big-endian), and "<" sets the least significant byte first. The "h" character in the format strings above describe the type of object being converted, which most importantly determines how many bytes are used when packing the value. "h" describes the value being converted as a 2-byte integer; other common format characters are "b" for a 1-byte integer, "I" for a 4-byte integer, and "s" for a string. Explore the links at the end of the section for more information on the struct module.

The struct.unpack() module performs the reverse operation of struct.pack(), unpacking a sequence of bytes into a new object. Unpacking always returns a tuple with the results, even if only unpacking a single value:

Figure 12.4.5: Unpacking values from byte sequences.
The following code uses the repr() function, which returns a string version of an object.

import struct


print("Result of unpacking", repr("\x00\x05") + ":", end=" ")
print(struct.unpack(">h", b"\x00\x05"))


print("Result of unpacking", repr("\x01\x00") + ":", end=" ")
print(struct.unpack(">h", b"\x01\x00"))


print("Result of unpacking", repr("\x00\x05\x01\x00") + ":", end=" ")
print(struct.unpack(">hh", b"\x00\x05\x01\x00"))
Result of unpacking "\x00\x05": (5,)
Result of unpacking "\x01\x00": (256,)
Result of unpacking "\x00\x05\x01\x00": (5, 256)

Feedback?
participation activity
12.4.2: The struct module.
1)
Complete the statement to pack an integer variable "my_num" into a 2-byte sequence. Assign my_bytes with the sequence. Use the byte ordering given by ">".
my_bytes = struct.pack(
)

Check

Show answer
2)
Assume that variable my_bytes is b"\x00\x04\xff\x00". Complete the statement to assign my_num with the 4-byte integer obtained by unpacking my_bytes. Use the byte ordering given by ">".
my_num = struct.unpack(
)

Check

Show answer

Feedback?'''
####################################################

''''''
with Scratch as e:
    import struct
    my_num = 42
    my_bytes = struct.pack(">h", my_num)
    print(my_bytes)
    # out: b'\x00*'
    #✅ Note: The output may vary based on the actual value of my_num and the format specified in struct.pack().
    my_bytes = b"\x00\x04\xff\x00"
    my_num = struct.unpack(">I", my_bytes)[0]
    print(my_num)
    # out: 327424
    #✅ Note: The output may vary based on the actual value of my_bytes and the format specified in struct.unpack().
with Scratch as e:
    bytes([12, 15, 20])
    # val: b'\x0c\x0f\x14'
    bytes("A text string", "ascii")
    # val: b'A text string'
    bytes(10)
    # val: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    bytes(1)
    # val: b'\x00'
    bytes(0)
    # val: b''
    try:
        bytes(-1)
    except ValueError as e:
        print("Error:", e)
        # out: Error: negative count
    try:
        bytes([256])
    except ValueError as e:
        print("Error:", e)
        # out: Error: bytes must be in range(0, 256)
    bytes([255])
    # val: b'\xff'
    yes=str(bytes([255]))
    print(f"{yes}")
    # out: b'\xff'
    str(yes)
    # val: b'\xff'
    yes2=""+str(yes)
    print(f"{yes2}")
    # out: b'\xff'
    print(b"\xff'")
    # out: b"\xff'"

    print(b"123456789 is the same as \x31\x32\x33\x34\x35\x36\x37\x38\x39")
    # out: b'123456789 is the same as 123456789'
    1
    # val: 1
    2
    # val: 2
    3
    # val: 3
    ###b"\x01"*3000 + b"\x02"*3000 + b"\x03"*3000

    b"\x01"*3 + b"\x02"*3 + b"\x03"*3
    # val: b'\x01\x01\x01\x02\x02\x02\x03\x03\x03'

    b"\x01"*1 + b"\x02"*1 + b"\x03"*1 + b"\x04"*1 + b"\x05"*1 + b"\x06"*1 + b"\x07"*1 + b"\x08"*1 + b"\x09"*1 + b"\x0a"*1 + b"\x0b"*1 + b"\x0c"*1 + b"\x0d"*1 + b"\x0e"*1 + b"\x0f"*1
    # val: b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
    print(b"\x03"*2)
    # out: b'\x03\x03'

    b"\x03"+b"\x01"
    # val: b'\x03\x01'

        
with Scratch as e:
    with "myfile.txt":
        print("This will not work because the file is not opened in binary mode.")
    try:
        with open("myfile.txt", "rb") as f:
            contents = f.read()
            print(contents)
            # out: b'buyers_file_name = input()\nbuyer_data = input()\nwith open(buyers_file_name, "a") as buyers_file:\n    buyers_file.write(buyer_data)\n    buyers_file.write("\\n")\n2'
    except FileNotFoundError:
        print("File not found.")


####################################################
'''participation activity
12.4.1: Binary Data.
1)
Open "data.txt" as read-only in binary mode.
f = open("data.txt", 
)

Check

Show answer
2)
Open "myfile.txt" as read-only in binary mode.
f = 


Check

Show answer
3)
Assign x with a bytes object with a single byte whose hexadecimal value is 0x1a. Use a bytes literal.
x = 


Check

Show answer
4)
Assign x with a bytes object containing three bytes with hexadecimal values 0x05, 0x15, and 0xf2. Use a bytes literal.
x = 


Check

Show answer'''
with Scratch as a:
    with "myfile.txt":
        f = open("data.txt", "rb")
        print(f)
        #⭐ out: <_io.BufferedReader name='data.txt'>
        f.close()
        f = open("myfile.txt", "rb")
        print(f)
        #⭐ out: <_io.BufferedReader name='myfile.txt'>
        f.close()
        x = b"\x1a"
        print(x)
        #⭐ out: b'\x1a'
        x = b"\x05\x15\xf2"
        print(x)
        #⭐ out: b'\x05\x15\xf2'

    open("data1.txt", "rb")
    # val: <_io.BufferedReader name='data1.txt'>
    def none():
        f = open("data1.txt", "rb")
        print(f)
        # out: <_io.BufferedReader name='data1.txt'>
        #⭐ out: <_io.BufferedReader name='data1.txt'>
        f.close()
        # val: None
        f = open("my123.txt", "rb")
        print(f)
        # out: <_io.BufferedReader name='my123.txt'>
        #⭐ out: <_io.BufferedReader name='my123.txt'>
        f.close()
        # val: None
        x = b"\x1a"
        print(x)
        # out: b'\x1a'
        #⭐ out: b'\x1a'
        x = b"\x05\x15\xf2"
        print(x)
        # out: b'\x05\x15\xf2'
        #⭐ out: b'\x05\x15\xf2'
    none()
    # val: None


with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    yes=open("data1.txt", "rb")
    print(yes)
    # out: <_io.BufferedReader name='data1.txt'>
    yes2=yes.read()
    print(yes2)
    # out: b'violet\n'
    ###open("ball.bmp", "rb").read()
####################################################
'''participation activity
12.4.2: The struct module.
1)
Complete the statement to pack an integer variable "my_num" into a 2-byte sequence. Assign my_bytes with the sequence. Use the byte ordering given by ">".
my_bytes = struct.pack(
)

Check

Show answer
2)
Assume that variable my_bytes is b"\x00\x04\xff\x00". Complete the statement to assign my_num with the 4-byte integer obtained by unpacking my_bytes. Use the byte ordering given by ">".
my_num = struct.unpack(
)

Check

Show answer

Feedback?'''
with Scratch as a:
    import struct
    my_num = 42
    my_bytes = struct.pack(">h", my_num)
    print(my_bytes)
    # out: b'\x00*'
    #✅ Note: The output may vary based on the actual value of my_num and the format specified in struct.pack().
    my_bytes = b"\x00\x04\xff\x00"
    my_num = struct.unpack(">I", my_bytes)[0]
    print(my_num)
    # out: 327424
    #✅ Note: The output may vary based on the actual value of my_bytes and the format specified in struct.unpack().
with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    import struct
    my_ball = open("ball.bmp", "rb").read()
    pixel_data_loc = my_ball[10:14]
    pixel_data_loc = struct.unpack("<L", pixel_data_loc)[0]
    print(f"Pixel data location: {pixel_data_loc}")
    # out: Pixel data location: 1212747008
    pixel_data_loc = struct.unpack("<L", b"\x06\x00\x00\x00")[0]
    print(f"Pixel data location: {pixel_data_loc}")
    # out: Pixel data location: 6

##############################################################################
'''## 12.5 Command-line arguments and files

The location of an input file or output file may not be known before writing a program. Instead, a program can use command-line arguments to allow the user to specify the location of an input file as shown in the following program. Assume two text files exist named "myfile1.txt" and "myfile2.txt" with the contents shown. The sample output shows the results when executing the program for either input file and for an input file that does not exist.

> **Using command-line arguments to specify the name of an input file.**
> ```python
> import sys
> import os
> 
> if len(sys.argv) != 2:
>     
>     print(f"Usage: {sys.argv[0]} input_file")
>     sys.exit(1)  # 1 indicates error
> 
> 
> print(f"Opening file {sys.argv[1]}.")
> 
> if not os.path.exists(sys.argv[1]):  # Make sure file exists
>     print("File does not exist.")
>     sys.exit(1)  # 1 indicates error
> 
> f = open(sys.argv[1], "r")
> 
> # Input files should contain two integers on separate lines
> 
> print("Reading two integers.")
> num1 = int(f.readline())
> num2 = int(f.readline())
> 
> 
> print(f"Closing file {sys.argv[1]}")
> f.close()  # Done with the file, so close it
> 
> 
> print(f"\nnum1: {num1}")
> 
> print(f"num2: {num2}")
> 
> print(f"num1 + num2: {num1 + num2}")
> ```
> ```
> 5
> 10
> ```

### PARTICIPATION ACTIVITY: Filename command line arguments.

> python

**1.** A script "myscript.py" has two command line arguments, one for an input file and a second for an output file. Type a command to run the program with input file "infile.txt" and output file "out".
Answer: myscript.py infile.txt out
*Hint: No quotes and no semicolons should be included. Pass in the script and the arguments.*
*python is called first to start the Python interpreter,  followed by the script name and the two arguments.*

**2.** For a program run as "python scriptname data.txt", what is sys.argv[1]? Do not use quotes in the answer.
Answer: data.txt
*Hint: sys.argv[0] is always the program name.*
*sys.argv[0] is the script's name, sys.argv[1] is the next argument, which is data.txt.*'''
####################################################
'''12.5 Command-line arguments and files
The location of an input file or output file may not be known before writing a program. Instead, a program can use command-line arguments to allow the user to specify the location of an input file as shown in the following program. Assume two text files exist named "myfile1.txt" and "myfile2.txt" with the contents shown. The sample output shows the results when executing the program for either input file and for an input file that does not exist.'''

#❓hello is your context okay?
#💿yes, it is.

with Scratch as a:
    with "my_script.py":
        import sys
        import os

        if len(sys.argv) != 2:
            
            print(f"Usage: {sys.argv[0]} input_file")
            sys.exit(1)  # 1 indicates error


        print(f"Opening file {sys.argv[1]}.")

        if not os.path.exists(sys.argv[1]):  # Make sure file exists
            print("File does not exist.")
            sys.exit(1)  # 1 indicates error

        f = open(sys.argv[1], "r")

        # Input files should contain two integers on separate lines

        print("Reading two integers.")
        num1 = int(f.readline())
        num2 = int(f.readline())


        print(f"Closing file {sys.argv[1]}")
        f.close()  # Done with the file, so close it


        print(f"\nnum1: {num1}")

        print(f"num2: {num2}")

        print(f"num1 + num2: {num1 + num2}")
        #print("This will not work because the file is not being run as a script with command-line arguments.")
1+1
# val: 2
###########not native############# [dont do this at home]
with "myfile1.txt":
    5
    10
cmd("python","my_script.py","myfile1.txt")
# val: Traceback (most recent call last):
# val:   File "/workspaces/Python-Copy2/sandbox/files/my_script.py", line 21, in <module>
# val:     num1 = int(f.readline())
# val:            ^^^^^^^^^^^^^^^^^
# val: ValueError: invalid literal for int() with base 10: '> python myscript.py infile.txt out\n'

cmd("python","my_script.py","myfile2.txt")
# val: Traceback (most recent call last):
# val:   File "/workspaces/Python-Copy2/sandbox/files/my_script.py", line 21, in <module>
# val:     num1 = int(f.readline())
# val:            ^^^^^^^^^^^^^^^^^
# val: ValueError: invalid literal for int() with base 10: '> python scriptname data.txt\n'
####################################################
'''participation activity
12.5.1: Filename command line arguments.
1)
A script "myscript.py" has two command line arguments, one for an input file and a second for an output file. Type a command to run the program with input file "infile.txt" and output file "out".
> python 


Check

Show answer
2)
For a program run as "python scriptname data.txt", what is sys.argv[1]? Do not use quotes in the answer.

Check

Show answer
'''
with Scratch as a:
    with "myfile1.txt":
        > python myscript.py infile.txt out
        #⭐ val: python myscript.py infile.txt out
    with "myfile2.txt":
        > python scriptname data.txt
        #⭐ val: python scriptname data.txt
        #✅ Note: The above commands are meant to be run in a command-line interface, not within a Python script. They are provided here for illustrative purposes based on the context of the participation activity.
        #data.txt
with Scratch as e:
    make_file("infile.txt", "5\n10\n")
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files/infile.txt')
    make_file("myfile1.txt", "5\n10\n")
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files/myfile1.txt')
    make_file("myfile2.txt", "5\n10\n")
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files/myfile2.txt')
    
    ###not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    cmd("python", "my_script.py", "infile.txt", "out")
    # val: Usage: my_script.py input_file
    cmd("python", "scriptname", "data.txt")
    # val: python: can't open file '/workspaces/Python-Copy2/sandbox/files/scriptname': [Errno 2] No such file or directory

##############################################################################
'''## 12.6 The "with" statement

A with statement can be used to open a file, execute a block of statements, and automatically close the file when complete.

> **The with statement.**

Above, the file object returned by open() is bound to myfile. When the statements in the block complete, then myfile is closed. The with statement creates a context manager, which manages the use of a resource, such as a file, by performing set-up and teardown operations. For files, the teardown operation is automatic closure. Other context managers exist for other resources, and new context managers can be written by a programmer, but these types of context managers are out of scope for this material.

Forgetting to close a file can sometimes cause problems. For example, a file opened in write mode cannot be written to by other programs. Good practice is to use a with statement when opening files to guarantee that the file is closed when no longer needed.

> **Using the with statement to open a file.**
> ```python
> print("Opening myfile.txt")
> 
> # Open a file for reading and writing
> with open("myfile.txt", "r+") as f:
>     # Read in two integers
>     num1 = int(f.readline())
>     num2 = int(f.readline())
> 
>     product = num1 * num2
> 
>     # Write back result on own line
>     f.write("\n")
>     f.write(str(product))
> 
> # No need to call f.close() - f closed automatically 
> print("Closed myfile.txt")
> ```

### PARTICIPATION ACTIVITY: The with statement.

**1.** When using a with statement to open a file, the file is automatically closed when the statements in the block finish executing.
Answer: **True**
*The context manager for files performs a teardown operation when the statements complete, closing the file automatically.*

**2.** Use of a with statement is not recommended most of the time when opening files.
Answer: **False**
*The with statement is recommended, because closure of the file is guaranteed.*

### CHALLENGE ACTIVITY: Using a "with" statement. (2 Levels)

**Level 1:**

**Task:**
First, [...] is read from input. Then, [...] is read from input to be [...] to the file. Complete the with statement to [...].

**Explanation pattern:**
The missing part of the with statement includes the keyword [...].

**Code structure:**
```python
___ = input()
___ = input()

___
""" Your code goes here """
___:
    ___.write(___)
    ___.write("\n")
```

**Level 2:**

**Task:**
First, [...] is read from input. Then, [...] is read from input to be [...] to the file. Write a with statement to open [...] with the "[...]" option for [...]. Bind [...] to the opened file using the keyword as.

**Explanation pattern:**
The with statement begins with the keyword with followed by open([...], "[...]") and as [...].

**Code structure:**
```python
___ = input()
___ = input()
""" Your code goes here """
:
    ___.write(___)
    ___.write("\n")
```
'''
####################################################
'''# 12.6 The "with" statement

A with statement can be used to open a file, execute a block of statements, and automatically close the file when complete.

**Construct 12.6.1: The with statement.**

with open("myfile.txt", "r") as myfile:
    # Statement-1
    # Statement-2
    # ....
    # Statement-N

Above, the file object returned by open() is bound to myfile. When the statements in the block complete, then myfile is closed. The with statement creates a context manager, which manages the use of a resource, such as a file, by performing set-up and teardown operations. For files, the teardown operation is automatic closure. Other context managers exist for other resources, and new context managers can be written by a programmer, but these types of context managers are out of scope for this material.

Forgetting to close a file can sometimes cause problems. For example, a file opened in write mode cannot be written to by other programs. Good practice is to use a with statement when opening files to guarantee that the file is closed when no longer needed.'''

with Scratch as e:
    #not native
    make_file("myfile.txt", "5\n10\n")
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files/myfile.txt')
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    
    print("Opening myfile.txt")
    # out: Opening myfile.txt
    with open("myfile.txt", "r") as myfile:
        contents = myfile.read()
        print(contents)
        # out: 5
        # out: 10
    # At this point, myfile is automatically closed.
    # Trying to read from myfile after the with block will raise an error.
    try:
        myfile.read()
    except ValueError as e:
        print("Error:", e)
        # out: Error: I/O operation on closed file.
####################################################
'''Figure 12.6.1: Using the with statement to open a file.
print("Opening myfile.txt")

# Open a file for reading and writing
with open("myfile.txt", "r+") as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write("\n")
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print("Closed myfile.txt")

Feedback?
participation activity
12.6.1: The with statement.
1)True or False:
When using a with statement to open a file, the file is automatically closed when the statements in the block finish executing.
2)True or False:
Use of a with statement is not recommended most of the time when opening files.

Feedback?'''
with Scratch as a:
    with "myfile.txt":
        "1)True"
        "2)False"
with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    print("When using a with statement to open a file, the file is automatically closed when the statements in the block finish executing.")
    # out: When using a with statement to open a file, the file is automatically closed when the statements in the block finish executing.
    print("Use of a with statement is not recommended most of the time when opening files.")
    # out: Use of a with statement is not recommended most of the time when opening files.
    print("True")
    # out: True
    print("False")
    # out: False
####################################################

'''challenge activity
12.6.1: Using a "with" statement.
712910.5105864.qx3zqy7

Jump to level 1
First, buyers_file_name is read from input. Then, buyer_data is read from input to be appended to the file. Complete the with statement to open buyers_file_name with the "a" option for appending.

Click here for example
Ex: If the input for buyers_file_name is data3.txt, buyer_data is Ani, and:

Contents of file data3.txt
Ron
then the output comes from:

New contents of file data3.txt
Ron
Ani

main.py
buyers_file_name = input()
buyer_data = input()

""" Your code goes here """ as buyers_file:
    buyers_file.write(buyer_data)
    buyers_file.write("\n")
data1.txt
Eve
Gus

data2.txt
Kim
Eli
Dan

data3.txt
Ron
'''

with Scratch as a:
    with "myfile.txt":
        buyers_file_name = input()
        buyer_data = input()
        with open(buyers_file_name, "a") as buyers_file:
            buyers_file.write(buyer_data)
            buyers_file.write("\n")

with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    make_file("data3.txt", "Ron\n")
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files/data3.txt')
    buyers_file_name = "data3.txt"
    buyer_data = "Ani"
    with open(buyers_file_name, "a") as buyers_file:
        buyers_file.write(buyer_data)
        # val: 3
        buyers_file.write("\n")
        # val: 1
    with open("data3.txt", "r") as f:
        contents = f.read()
        print(contents)
        # out: Ron
        # out: Ani
####################################################
'''challenge activity
12.6.1: Using a "with" statement.
712910.5105864.qx3zqy7

Jump to level 1
First, foodstuffs_file_name is read from input. Then, foodstuff_data is read from input to be appended to the file. Write a with statement to open foodstuffs_file_name with the "a" option for appending. Bind foodstuffs_file to the opened file using the keyword as.

Click here for example
Ex: If the input for foodstuffs_file_name is data3.txt, foodstuff_data is egg, and:

Contents of file data3.txt
yam
then the output comes from:

New contents of file data3.txt
yam
egg

main.py
foodstuffs_file_name = input()
foodstuff_data = input()

""" Your code goes here """:
    foodstuffs_file.write(foodstuff_data)
    foodstuffs_file.write("\n")
data1.txt
beet
plum
leek

data2.txt
lime
pear

data3.txt
yam
'''

with Scratch as a:
    with "myfile5.txt":
        foodstuffs_file_name = input()
        foodstuff_data = input()
        with open(foodstuffs_file_name, "a") as foodstuffs_file:
            foodstuffs_file.write(foodstuff_data)
            foodstuffs_file.write("\n")

##############################################################################
'''## 12.7 Comma-separated values files

Text data is commonly organized in a spreadsheet format using columns and rows. A comma-separated values (csv) file  is a simple text-based file format that uses commas to separate data items, called fields. Below is an example of a typical csv file that contains information about student scores:

> **Contents of a csv file.**
> ```
> name,hw1,hw2,midterm,final
> Petr Little,9,8,85,78
> Sam Tarley,10,10,99,100
> Joff King,4,2,55,61
> ```

Each line in the file above represents a row, and fields between commas on each row are in the same column as fields in the same position in each line. For example, the first row contains the items "name", "hw1", "hw2", "midterm", and "final"; the second row contains "Petr Little", "9", "8", "85" and "78". The first column contains "name", "Petr Little", "Sam Tarley", and "Joff King"; the second column contains "hw1", "9", "10", and "4".

The Python standard library csv module can be used to help read and write files in the csv format. To read a file using the csv module, a program must first create a *reader* object, passing a file object created via *open*. The reader object is an iterable&mdash;iterating over the reader using a for loop returns each row of the csv file as a list of strings, where each item in the list is a field from the row.

> **Reading each row of a csv file.**
> ```python
> import csv
> 
> with open("grades.csv", "r") as csvfile:
>     grades_reader = csv.reader(csvfile, delimiter=",")
> 
>     row_num = 1
>     for row in grades_reader:
>         print(f"Row #{row_num}: {row}")
>         row_num += 1
> ```
> ```
> Row #1: ["name", "hw1", "hw2", "midterm", "final"]
> Row #2: ["Petr Little", "9", "8", "85", "78"]
> Row #3: ["Sam Tarley", "10", "10", "99", "100"]
> Row #4: ["Joff King", "4", "2", "55", "61"]
> ```

The optional delimiter argument in the csv.reader() function specifies the character used in the csv file to separate fields; by default, a comma is used. In some cases, the field itself may contain a comma&mdash;for example, if the name of a student was specified as "lastname,firstname". In such a case, the csv file might instead use semicolons or some other rare character, e.g., Little, Petr;9;8;85;78. An alternative to changing the delimiter is to use quotes around the item containing the comma, e.g., "Little, Petr",9,8,85,78.

If the contents of the fields are numeric, then a programmer may want to convert the strings to integer or floating-point values to perform calculations with the data. The example below reads each row using a reader object and calculates a student's final score in the class:

> **Using csv file contents to perform calculations.**
> ```python
> import csv
> 
> # Dictionary that maps student names to a list of scores
> grades = {}
> 
> # Use with statement to guarantee file closure
> with open("grades.csv", "r") as csvfile:
>     grades_reader = csv.reader(csvfile, delimiter=",")
> 
>     first_row = True
>     for row in grades_reader:
>         # Skip the first row with column names
>         if first_row:
>             first_row = False
>             continue
> 
>         ## Calculate final student grade ##
> 
>         name = row[0]
> 
>         # Convert score strings into floats
>         scores = [float(cell) for cell in row[1:]]
> 
>         hw1_weighted = scores[0]/10 * 0.05
>         hw2_weighted = scores[1]/10 * 0.05
>         mid_weighted = scores[2]/100 * 0.40
>         fin_weighted = scores[3]/100 * 0.50
> 
>         grades[name] = (hw1_weighted + hw2_weighted + 
>                         mid_weighted + fin_weighted) * 100
> 
> for student, score in grades.items():
>     print(f"{student} earned {score:.1f}%")
> ```
> ```
> Petr Little earned 81.5%
> Sam Tarley earned 99.6%
> Joff King earned 55.5%
> ```

A programmer can also use the csv module to write text into a csv file, using a *writer* object. The writer object's *writerow()* and *writerows* methods can be used to write a list of strings into the file as one or more rows.

> **Writing rows to a csv module.**
> ```python
> import csv
> 
> row1 = ["100", "50", "29"]
> row2 = ["76", "32", "330"]
> 
> with open("gradeswr.csv", "w", newline="") as csvfile:
>     grades_writer = csv.writer(csvfile)
> 
>     grades_writer.writerow(row1)
>     grades_writer.writerow(row2)
> 
>     grades_writer.writerows([row1, row2])
> ```
> ```
> 100,50,29
> 76,32,330
> 100,50,29
> 76,32,330
> ```

### PARTICIPATION ACTIVITY: Comma-separated values files.

import csv
with open("myfile.csv", "r") as myfile:
    csv_reader =

**1.** Complete the statement to create a csv module reader object to read myfile.csv.
Answer: csv.reader(myfile) or csv.reader(myfile, delimiter=',')
*Hint: Create an instance of csv.reader. Specifying the delimiter argument is optional.*
*The reader object can be used to iterate over rows of the csv file.*

import csv
with open("myfile.csv", "r") as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(

**2.** Complete the statement so that the program prints the destination of each flight in myfile.csv. )
Answer: row[1]
*Hint: The "row" variable is a list of strings containing the current row's fields that are read from the file.*
*Iterating over the reader object yields each row of the file as a list of the fields. The destination field is in position 1 of the list.*'''
####################################################
'''2.7 Comma-separated values files
Text data is commonly organized in a spreadsheet format using columns and rows. A comma-separated values (csv) file is a simple text-based file format that uses commas to separate data items, called fields. Below is an example of a typical csv file that contains information about student scores:

Figure 12.7.1: Contents of a csv file.
name,hw1,hw2,midterm,final
Petr Little,9,8,85,78
Sam Tarley,10,10,99,100
Joff King,4,2,55,61

Feedback?
Each line in the file above represents a row, and fields between commas on each row are in the same column as fields in the same position in each line. For example, the first row contains the items "name", "hw1", "hw2", "midterm", and "final"; the second row contains "Petr Little", "9", "8", "85" and "78". The first column contains "name", "Petr Little", "Sam Tarley", and "Joff King"; the second column contains "hw1", "9", "10", and "4".

The Python standard library csv module can be used to help read and write files in the csv format. To read a file using the csv module, a program must first create a reader object, passing a file object created via open. The reader object is an iterable—iterating over the reader using a for loop returns each row of the csv file as a list of strings, where each item in the list is a field from the row.

Figure 12.7.2: Reading each row of a csv file.'''
with Scratch as a:
    with "mycsv.py":
        import csv
        with open("grades.csv", "r") as csvfile:
            grades_reader = csv.reader(csvfile, delimiter=",")

            row_num = 1
            for row in grades_reader:
                print(f"Row #{row_num}: {row}")
                row_num += 1
        #⭐ out: Row #1: ['name', 'hw1', 'hw2', 'midterm', 'final']
        #⭐ out: Row #2: ['Petr Little', '9', '8', '85', '78']
        #⭐ out: Row #3: ['Sam Tarley', '10', '10', '99', '100']
        #⭐ out: Row #4: ['Joff King', '4', '2', '55', '61']
        # Feedback?
####################################################
'''The optional delimiter argument in the csv.reader() function specifies the character used in the csv file to separate fields; by default, a comma is used. In some cases, the field itself may contain a comma—for example, if the name of a student was specified as "lastname,firstname". In such a case, the csv file might instead use semicolons or some other rare character, e.g., Little, Petr;9;8;85;78. An alternative to changing the delimiter is to use quotes around the item containing the comma, e.g., "Little, Petr",9,8,85,78.

If the contents of the fields are numeric, then a programmer may want to convert the strings to integer or floating-point values to perform calculations with the data. The example below reads each row using a reader object and calculates a student's final score in the class:

Figure 12.7.3: Using csv file contents to perform calculations.'''
with Scratch as a:
    with "mycsv2.py":
        import csv

        # Dictionary that maps student names to a list of scores
        grades = {}

        # Use with statement to guarantee file closure
        with open("grades.csv", "r") as csvfile:
            grades_reader = csv.reader(csvfile, delimiter=",")

            first_row = True
            for row in grades_reader:
                # Skip the first row with column names
                if first_row:
                    first_row = False
                    continue

                ## Calculate final student grade ##

                name = row[0]

                # Convert score strings into floats
                scores = [float(cell) for cell in row[1:]]

                hw1_weighted = scores[0]/10 * 0.05
                hw2_weighted = scores[1]/10 * 0.05
                mid_weighted = scores[2]/100 * 0.40
                fin_weighted = scores[3]/100 * 0.50

                grades[name] = (hw1_weighted + hw2_weighted + 
                                mid_weighted + fin_weighted) * 100

        for student, score in grades.items():
            print(f"{student} earned {score:.1f}%")
        #⭐ out: Petr Little earned 81.5%
        #⭐ out: Sam Tarley earned 99.6%
        #⭐ out: Joff King earned 55.5%
        # Feedback?
####################################################
'''A programmer can also use the csv module to write text into a csv file, using a writer object. The writer object's writerow() and writerows methods can be used to write a list of strings into the file as one or more rows.

Figure 12.7.4: Writing rows to a csv module.'''

with Scratch as a:
    with "mycsv3.py":
        import csv

        row1 = ["100", "50", "29"]
        row2 = ["76", "32", "330"]

        with open("gradeswr.csv", "w", newline="") as csvfile:
            grades_writer = csv.writer(csvfile)

            grades_writer.writerow(row1)
            grades_writer.writerow(row2)

            grades_writer.writerows([row1, row2])
        #⭐ out: 100,50,29
        #⭐ out: 76,32,330
        #⭐ out: 100,50,29
        #⭐ out: 76,32,330
        # Feedback?
##########################
with Scratch as ae:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    import csv
    row1 = ["100", "50", "29"]
    row2 = ["76", "32", "330"]
    with open("gradeswr.csv", "w", newline="") as csvfile:
        grades_writer = csv.writer(csvfile)

        grades_writer.writerow(row1)
        # val: 11
        grades_writer.writerow(row2)
        # val: 11

        grades_writer.writerows([row1, row2])
        # val: None
    ret_file("gradeswr.csv")
    # val: 100,50,29
    # val: 76,32,330
    # val: 100,50,29
    # val: 76,32,330
####################################################
'''participation activity
12.7.1: Comma-separated values files.
The file "myfile.csv" contains the following contents:

Airline,Destination,Departure time,Plane
Southwest,Phoenix,615,B747
Alitalia,Milan,1545,B757
British Airways,London,1230,A380
1)
Complete the statement to create a csv module reader object to read myfile.csv.
import csv
with open("myfile.csv", "r") as myfile:
    csv_reader = 

 

Check

Show answer
2)
Complete the statement so that the program prints the destination of each flight in myfile.csv.
import csv
with open("myfile.csv", "r") as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(
)

Check

Show answer''' #[2] is print(row[1])

with Scratch as a:
    with "myfile.py":
        import csv
        with open("myfile.csv", "r") as myfile:
            csv_reader = csv.reader(myfile) #✅<- 
            for row in csv_reader:
                print(row[1]) #✅<- 
                #⭐ out: Destination
                #⭐ out: Phoenix
                #⭐ out: Milan
                #⭐ out: London
with Scratch as e:
    #not native
    here()
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files')
    make_file("myfile.csv", "Airline,Destination,Departure time,Plane\nSouthwest,Phoenix,615,B747\nAlitalia,Milan,1545,B757\nBritish Airways,London,1230,A380\n")
    # val: PosixPath('/workspaces/Python-Copy2/sandbox/files/myfile.csv')
    import csv
    with open("myfile.csv", "r") as myfile:
        csv_reader = csv.reader(myfile)
        for row in csv_reader:
            print(row[1])
            # out: Destination
            # out: Phoenix
            # out: Milan
            # out: London
with Scratch as other:
    
    with "mycsv2.py":
        import csv
        with open("mycsv2.csv", "r") as myfile:
            csv_reader = csv.reader(myfile)
            for row in csv_reader:
                print(row[1])

    with "mycsv2.csv":
        Airline,Destination,Departure time,Plane
        Southwest,Phoenix,615,B747
        Alitalia,Milan,1545,B757
        British Airways,London,1230,A380
    ret_file("mycsv2.csv")
    # val: Airline,Destination,Departure time,Plane
    # val: Southwest,Phoenix,615,B747
    # val: Alitalia,Milan,1545,B757
    # val: British Airways,London,1230,A380
    cmd("python", "mycsv2.py")
    # val: Destination
    # val: Phoenix
    # val: Milan
    # val: London
##############################################################################
'''## 12.8 LAB: Words in a range (lists)

### LAB ACTIVITY: LAB: Words in a range (lists)

Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should determine if the strings from the list are within that range (inclusive of the bounds) and output the results.
Ex: If the input is:

```
input1.txt
ammoniated
millennium
```
and the contents of input1.txt are:

```
aspiration
classified
federation
graduation
millennium
philosophy
quadratics
transcript
wilderness
zoologists
```
the output is:

```
aspiration - in range
classified - in range
federation - in range
graduation - in range
millennium - in range
philosophy - not in range
quadratics - not in range
transcript - not in range
wilderness - not in range
zoologists - not in range
```
Notes:
- End the output with a newline.- All input files are hosted in the zyLab and file names can be directly referred to. **input1.txt** is available to download so that the contents of the file can be seen.- In the tests, the first word input always comes alphabetically before the second word input.

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `input1.txt\nammoniated\nmillennium\n` | `aspiration - in range\nclassified - in range\nfederation - in range\ngraduation - in range\nmillennium - in range\nphilosophy - not in range\nquadratics - not in range\ntranscript - not in range\nwilderness - not in range\nzoologists - not in range` | 1 |
| 2 | `input1.txt\nantheridia\nholofernes\n` | `aspiration - in range\nclassified - in range\nfederation - in range\ngraduation - in range\nmillennium - not in range\nphilosophy - not in range\nquadratics - not in range\ntranscript - not in range\nwilderness - not in range\nzoologists - not in range` | 1 |
| 3 | `input2.txt\nadrianople\nmisopaedia\n` | `acromicria - not in range\nacronymous - not in range\nattractant - in range\nbackblocks - in range\nbladderpod - in range\nbrownnosed - in range\nburglarise - in range\nbusybodies - in range\neconomiser - in range\nequanimous - in range\nescarpment - in range\nexfoliated - in range\nextemporal - in range\nglochidial - in range\nglomerular - in range\ngloucester - in range\ngorgonised - in range\ngrandmamma - in range\nhaeckelism - in range\nheadphones - in range\nignorantly - in range\nimpassable - in range\nimpishness - in range\nintermalar - in range\njacobethan - in range\njapanesque - in range\njubilation - in range\nnarcissist - not in range\nneoplastic - not in range\nnominalist - not in range\nnontrunked - not in range\nnunciature - not in range\noblongness - not in range\noutlipping - not in range\noutsnoring - not in range\noverdosage - not in range\noverharden - not in range\nphenacetin - not in range\npluraliser - not in range\npoeticised - not in range\npredefying - not in range\npredestine - not in range\nquadriceps - not in range\nquantified - not in range\nquaternary - not in range\nquietistic - not in range\nquinoidine - not in range\ntranscribe - not in range\nultrafiche - not in range\nunprofaned - not in range\nurogomphus - not in range\nvallecular - not in range\nvinylating - not in range\nviolescent - not in range\nviscountcy - not in range\nvitalizing - not in range\nweaponshaw - not in range\nwinkelried - not in range\nxenophobic - not in range\nxiphosuran - not in range\nzeffirelli - not in range\nzoophilism - not in range` | 2 |
| 4 | `input2.txt\ncharcutier\nwinkelried\n` | `acromicria - not in range\nacronymous - not in range\nattractant - not in range\nbackblocks - not in range\nbladderpod - not in range\nbrownnosed - not in range\nburglarise - not in range\nbusybodies - not in range\neconomiser - in range\nequanimous - in range\nescarpment - in range\nexfoliated - in range\nextemporal - in range\nglochidial - in range\nglomerular - in range\ngloucester - in range\ngorgonised - in range\ngrandmamma - in range\nhaeckelism - in range\nheadphones - in range\nignorantly - in range\nimpassable - in range\nimpishness - in range\nintermalar - in range\njacobethan - in range\njapanesque - in range\njubilation - in range\nnarcissist - in range\nneoplastic - in range\nnominalist - in range\nnontrunked - in range\nnunciature - in range\noblongness - in range\noutlipping - in range\noutsnoring - in range\noverdosage - in range\noverharden - in range\nphenacetin - in range\npluraliser - in range\npoeticised - in range\npredefying - in range\npredestine - in range\nquadriceps - in range\nquantified - in range\nquaternary - in range\nquietistic - in range\nquinoidine - in range\ntranscribe - in range\nultrafiche - in range\nunprofaned - in range\nurogomphus - in range\nvallecular - in range\nvinylating - in range\nviolescent - in range\nviscountcy - in range\nvitalizing - in range\nweaponshaw - in range\nwinkelried - in range\nxenophobic - not in range\nxiphosuran - not in range\nzeffirelli - not in range\nzoophilism - not in range` | 2 |
| 5 | `input3.txt\nantipapism\nqueensland\n` | `abdication - not in range\nabnegating - not in range\nabstersive - not in range\nanalytical - not in range\nantimasker - not in range\nbalneology - in range\nblandisher - in range\nbloomfield - in range\nboilerless - in range\nbutterfish - in range\ncabalistic - in range\ncastration - in range\nchasmogamy - in range\ncnidophore - in range\ncorrientes - in range\ndevocalise - in range\ndimerizing - in range\ndispraised - in range\ndistillate - in range\ndistortive - in range\nearthbound - in range\nencipherer - in range\nequipoised - in range\nevaluating - in range\nexpurgated - in range\nfacileness - in range\nfarforthly - in range\nfeebleness - in range\nfilialness - in range\nfoamflower - in range\ngeniculate - in range\ngingersnap - in range\ngnosticize - in range\ngoalkeeper - in range\ngreenbrier - in range\nhardenable - in range\nharmlessly - in range\nharquebuss - in range\nhatshepset - in range\nhephaistos - in range\nincurrence - in range\ninterceder - in range\ninterferon - in range\nintrospect - in range\nirishizing - in range\njanitorial - in range\njarovizing - in range\njawbreaker - in range\njournalese - in range\njuantorena - in range\nkeratinise - in range\nkhrushchev - in range\nkilmarnock - in range\nkilndrying - in range\nknockabout - in range\nlatinizing - in range\nleucomaine - in range\nlibrettist - in range\nlongstreet - in range\nlysistrata - in range\nmatozinhos - in range\nmickiewicz - in range\nmixability - in range\nmotherhood - in range\nmutilating - in range\nnephrocele - in range\nnettlelike - in range\nnoncogency - in range\nnongenuine - in range\nnonswimmer - in range\noutroguing - in range\noutselling - in range\noverdilate - in range\noverseason - in range\noverstress - in range\nphenetidin - in range\npoulticing - in range\npresbyopia - in range\nprologuist - in range\npseudocele - in range\nquadruplex - in range\nquantified - in range\nquathlamba - in range\nquinacrine - not in range\nquintuplet - not in range\nreaudition - not in range\nrecreatory - not in range\nremobilize - not in range\nretroceded - not in range\nromanesque - not in range\nscraggiest - not in range\nstockiness - not in range\nsuperimply - not in range\nswearingly - not in range\nsymbolical - not in range\ntallowlike - not in range\nthroughout - not in range\ntoastiness - not in range\ntrigeminal - not in range\ntrouvaille - not in range\nundercarry - not in range\nundrenched - not in range\nunfrazzled - not in range\nunreminded - not in range\nunsturdily - not in range\nvindictive - not in range\nvinylidene - not in range\nviscometer - not in range\nviscometry - not in range\nviviparous - not in range\nwapinschaw - not in range\nwestwardly - not in range\nwindowless - not in range\nwinkelried - not in range\nwomanising - not in range\nxanthophyl - not in range\nxenocrates - not in range\nxenolithic - not in range\nxylostroma - not in range\nxylotomous - not in range\nyarborough - not in range\nyeastiness - not in range\nyellowlegs - not in range\nyellowwood - not in range\nyonkersite - not in range\nzeffirelli - not in range\nzephyrinus - not in range\nzinckenite - not in range\nzoophilism - not in range\nzoophobous - not in range` | 2 |
| 6 | `input3.txt\ndimerizing\nkilndrying\n` | `abdication - not in range\nabnegating - not in range\nabstersive - not in range\nanalytical - not in range\nantimasker - not in range\nbalneology - not in range\nblandisher - not in range\nbloomfield - not in range\nboilerless - not in range\nbutterfish - not in range\ncabalistic - not in range\ncastration - not in range\nchasmogamy - not in range\ncnidophore - not in range\ncorrientes - not in range\ndevocalise - not in range\ndimerizing - in range\ndispraised - in range\ndistillate - in range\ndistortive - in range\nearthbound - in range\nencipherer - in range\nequipoised - in range\nevaluating - in range\nexpurgated - in range\nfacileness - in range\nfarforthly - in range\nfeebleness - in range\nfilialness - in range\nfoamflower - in range\ngeniculate - in range\ngingersnap - in range\ngnosticize - in range\ngoalkeeper - in range\ngreenbrier - in range\nhardenable - in range\nharmlessly - in range\nharquebuss - in range\nhatshepset - in range\nhephaistos - in range\nincurrence - in range\ninterceder - in range\ninterferon - in range\nintrospect - in range\nirishizing - in range\njanitorial - in range\njarovizing - in range\njawbreaker - in range\njournalese - in range\njuantorena - in range\nkeratinise - in range\nkhrushchev - in range\nkilmarnock - in range\nkilndrying - in range\nknockabout - not in range\nlatinizing - not in range\nleucomaine - not in range\nlibrettist - not in range\nlongstreet - not in range\nlysistrata - not in range\nmatozinhos - not in range\nmickiewicz - not in range\nmixability - not in range\nmotherhood - not in range\nmutilating - not in range\nnephrocele - not in range\nnettlelike - not in range\nnoncogency - not in range\nnongenuine - not in range\nnonswimmer - not in range\noutroguing - not in range\noutselling - not in range\noverdilate - not in range\noverseason - not in range\noverstress - not in range\nphenetidin - not in range\npoulticing - not in range\npresbyopia - not in range\nprologuist - not in range\npseudocele - not in range\nquadruplex - not in range\nquantified - not in range\nquathlamba - not in range\nquinacrine - not in range\nquintuplet - not in range\nreaudition - not in range\nrecreatory - not in range\nremobilize - not in range\nretroceded - not in range\nromanesque - not in range\nscraggiest - not in range\nstockiness - not in range\nsuperimply - not in range\nswearingly - not in range\nsymbolical - not in range\ntallowlike - not in range\nthroughout - not in range\ntoastiness - not in range\ntrigeminal - not in range\ntrouvaille - not in range\nundercarry - not in range\nundrenched - not in range\nunfrazzled - not in range\nunreminded - not in range\nunsturdily - not in range\nvindictive - not in range\nvinylidene - not in range\nviscometer - not in range\nviscometry - not in range\nviviparous - not in range\nwapinschaw - not in range\nwestwardly - not in range\nwindowless - not in range\nwinkelried - not in range\nwomanising - not in range\nxanthophyl - not in range\nxenocrates - not in range\nxenolithic - not in range\nxylostroma - not in range\nxylotomous - not in range\nyarborough - not in range\nyeastiness - not in range\nyellowlegs - not in range\nyellowwood - not in range\nyonkersite - not in range\nzeffirelli - not in range\nzephyrinus - not in range\nzinckenite - not in range\nzoophilism - not in range\nzoophobous - not in range` | 2 |
*Total: 10 points*
```python
# Type your code here. 
```
'''

with Scratch as a:
    with "lab_12_8/main.py":
        file_name = input()
        lower_bound = input()
        upper_bound = input()

        with open(file_name, "r") as f:
            words = f.readlines()

        for word in words:
            word = word.strip()  # Remove any leading/trailing whitespace
            if lower_bound <= word <= upper_bound:
                print(f"{word} - in range")
            else:
                print(f"{word} - not in range")
####################################################
'''## 12.9 LAB: Word frequencies (lists)

### LAB ACTIVITY: LAB: Word frequencies (lists)

Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. The file contains a list of words separated by commas. The program must output the words and their frequencies (the number of times each word appears in the file) without any duplicates.
Ex: If the input is:

```
input1.csv
```
and the contents of input1.csv are:

```
hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
```
the output is:

```
hello - 1
cat - 2
man - 2
hey - 2
dog - 2
boy - 2
Hello - 1
woman - 1
Cat - 1
```
Notes: Output words in order of first occurrence in input and end output with a newline. File **input1.csv** is available to download.

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `input1.csv\n` | `hello - 1\ncat - 2\nman - 2\nhey - 2\ndog - 2\nboy - 2\nHello - 1\nwoman - 1\nCat - 1` | 1 |
| 2 | `input2.csv\n` | `bubble - 3\ncaring - 1\nunsuitable - 1\ndispensable - 1\nobtainable - 1\nbloody - 1\nmeddle - 1\ncrown - 1\nvisitor - 1\nahead - 1\ninvention - 1\nspot - 1\ndelirious - 1\nsavory - 1\nservant - 1\npot - 1\nincrease - 1\nsoothe - 1\ntruculent - 1\nsqueak - 1\nlearn - 2\ntroubled - 1\nwalk - 1\ntease - 1\ncumbersome - 1\ndeeply - 2\nspark - 1\nscience - 1\nisland - 1\nnarrow - 1` | 2 |
| 3 | `input3.csv\n` | `hi - 7\nhey - 2\nHi - 3\nHI - 2` | 2 |
| 4 | `input4.csv\n` | `caring - 1\nunsuitable - 1\nbubble - 1\ndispensable - 1\nobtainable - 1\nbloody - 1\nmeddle - 1\ncrown - 1\nvisitor - 1\nahead - 1\ninvention - 1\nspot - 1\ndelirious - 1\nsavory - 1\nservant - 1\npot - 1\nincrease - 1\nsoothe - 1\ntruculent - 1\nsqueak - 1\nlearn - 1\ntroubled - 1\nwalk - 1\ntease - 1\ncumbersome - 1\ndeeply - 1\nspark - 1\nscience - 1\nisland - 1\nnarrow - 1` | 2 |
| 5 | `input5.csv\n` | `spy - 5\npleasure - 1\nuncovered - 1\nupbeat - 1\nfound - 1\ncopper - 3\nshare - 1\nbelieve - 1\nbrawny - 1\ncommittee - 1\nhydrant - 1\neminent - 1\ntowering - 2\ncoherent - 1\npast - 1\nhate - 2\nstep - 2\ninfluence - 1\nants - 1\ndesk - 2\nobsolete - 1\nanalyse - 1\nimportant - 1\nunruly - 1\ncowardly - 1\namused - 1\ngovernor - 1\nsloppy - 1\nlevel - 1\ncall - 1\ntransport - 1\ncakes - 3\nbad - 1\nnumerous - 1\nmarch - 1\nmurder - 1\npossessive - 1\ninternal - 1\ngiant - 1\nhum - 1\nrose - 1\naunt - 1\nskin - 1\ntrouble - 1\ncontinue - 1\nglow - 1\nenchanting - 1\nsock - 1\nmotionless - 1\nwaste - 1\nmarvelous - 1\nsecretive - 2\nguarantee - 1\nducks - 1\ntop - 1\nflood - 1\nwell-off - 1\nmilk - 1\nbubble - 1\nmagic - 1\nspray - 1\nspare - 1\nlove - 1\nstereotyped - 1\njagged - 1\ndysfunctional - 1\nsneeze - 1\nmountain - 1\nignore - 1\ntacky - 2\nincompetent - 1\ndear - 1\ndare - 1\ncaring - 1\nproperty - 1\nmist - 1\ntest - 1\nfoamy - 1\nnotice - 1` | 3 |
*Total: 10 points*
```python
import csv

# Type your code here. 
```'''
with Scratch as a:
    with "lab_12_9/main.py":
        import csv

        file_name = input()

        word_freq = {}
        with open(file_name, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                for word in row:
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1

        for word, freq in word_freq.items():
            print(f"{word} - {freq}")
            
##############################################################################
'''## 12.12 LAB: File name change

### LAB ACTIVITY: LAB: File name change

A photographer is organizing a photo collection about the national parks in the US and would like to annotate the information about each of the photos into a separate set of files. Write a program that reads the name of a text file containing a list of photo file names. The program then reads the photo file names from the text file, replaces the "_photo.jpg" portion of the file names with "_info.txt", and outputs the modified file names.
Assume the unchanged portion of the photo file names contains only letters and numbers, and the text file stores one photo file name per line. If the text file is empty, the program produces no output.
Ex: If the input of the program is:

```
ParkPhotos.txt
```
and the contents of ParkPhotos.txt are:

```
Acadia2003_photo.jpg
AmericanSamoa1989_photo.jpg
BlackCanyonoftheGunnison1983_photo.jpg
CarlsbadCaverns2010_photo.jpg
CraterLake1996_photo.jpg
GrandCanyon1996_photo.jpg
IndianaDunes1987_photo.jpg
LakeClark2009_photo.jpg
Redwood1980_photo.jpg
VirginIslands2007_photo.jpg
Voyageurs2006_photo.jpg
WrangellStElias1987_photo.jpg
```
the output of the program is:

```
Acadia2003_info.txt
AmericanSamoa1989_info.txt
BlackCanyonoftheGunnison1983_info.txt
CarlsbadCaverns2010_info.txt
CraterLake1996_info.txt
GrandCanyon1996_info.txt
IndianaDunes1987_info.txt
LakeClark2009_info.txt
Redwood1980_info.txt
VirginIslands2007_info.txt
Voyageurs2006_info.txt
WrangellStElias1987_info.txt
```

**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `ParkPhotos.txt\n` | `Acadia2003_info.txt\nAmericanSamoa1989_info.txt\nBlackCanyonoftheGunnison1983_info.txt\nCarlsbadCaverns2010_info.txt\nCraterLake1996_info.txt\nGrandCanyon1996_info.txt\nIndianaDunes1987_info.txt\nLakeClark2009_info.txt\nRedwood1980_info.txt\nVirginIslands2007_info.txt\nVoyageurs2006_info.txt\nWrangellStElias1987_info.txt` | 3 |
| 2 | `ParkPhotos1.txt\n` | `Acadia2003_info.txt\nAmericanSamoa1989_info.txt\nArches1997_info.txt\nBadlands2000_info.txt\nBigBend2008_info.txt\nBiscayne2019_info.txt\nBlackCanyonoftheGunnison1983_info.txt\nBryceCanyon1985_info.txt\nCanyonlands1996_info.txt\nCapitolReef1991_info.txt\nCarlsbadCaverns2010_info.txt\nChannelIslands1999_info.txt\nCongaree2006_info.txt\nCraterLake1996_info.txt\nCuyahogaValley1995_info.txt\nDeathValley1996_info.txt\nDenali2001_info.txt\nDryTortugas1982_info.txt\nEverglades1984_info.txt\nGatesoftheArctic1989_info.txt\nGatewayArch1986_info.txt\nGlacierBay1982_info.txt\nGlacier1980_info.txt\nGrandCanyon1996_info.txt\nGrandTeton1997_info.txt\nGreatBasin2018_info.txt\nGreatSandDunes2006_info.txt\nGreatSmokyMountains1992_info.txt\nGuadalupeMountains2020_info.txt\nHaleakala2010_info.txt\nHawaiiVolcanoes1981_info.txt\nHotSprings1984_info.txt\nIndianaDunes1987_info.txt\nIsleRoyale1987_info.txt\nJoshuaTree1984_info.txt\nKatmai1997_info.txt\nKenaiFjords2020_info.txt\nKingsCanyon2002_info.txt\nKobukValley2014_info.txt\nLakeClark2009_info.txt\nLassenVolcanic1991_info.txt\nMammothCave1983_info.txt\nMesaVerde2012_info.txt\nMountRainier1999_info.txt\nNorthCascades1993_info.txt\nOlympic1986_info.txt\nPetrifiedForest1994_info.txt\nPinnacles1998_info.txt\nRedwood1980_info.txt\nRockyMountain1986_info.txt\nSaguaro1980_info.txt\nSequoia2009_info.txt\nShenandoah1983_info.txt\nTheodoreRoosevelt2006_info.txt\nVirginIslands2007_info.txt\nVoyageurs2006_info.txt\nWhiteSands2002_info.txt\nWindCave1986_info.txt\nWrangellStElias1987_info.txt\nYellowstone2017_info.txt\nYosemite1992_info.txt\nZion2009_info.txt` | 3 |
| 3 | `ParkPhotos2.txt\n` | `GreatSmokyMountains1992_info.txt` | 2 |
| 4 | `ParkPhotos3.txt\n` | `` | 2 |
*Total: 10 points*
```python
# Type your code here.```
'''
with Scratch as a:
    with "lab_12_12/main.py":
        file_name = input()

        with open(file_name, "r") as f:
            photo_files = f.readlines()

        for photo in photo_files:
            photo = photo.strip()  # Remove any leading/trailing whitespace
            info_file = photo.replace("_photo.jpg", "_info.txt")
            print(info_file)

##############################################################################
