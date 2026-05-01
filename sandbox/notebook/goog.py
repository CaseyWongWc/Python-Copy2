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
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
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
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
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
    # val: 
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
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
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
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
        #⭐ val: 5 + 7.5 = 12.5
        f.close()
        # val: None
    with open("myfile.txt", "r") as f:
        f.read()
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
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
    # val: f = open("data.txt", "rb")
    # val: print(f)
    # val: #⭐ out: <_io.BufferedReader name='data.txt'>
    # val: f.close()
    # val: f = open("myfile.txt", "rb")
    # val: print(f)
    # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
    # val: f.close()
    # val: x = b"\x1a"
    # val: print(x)
    # val: #⭐ out: b'\x1a'
    # val: x = b"\x05\x15\xf2"
    # val: print(x)
    # val: #⭐ out: b'\x05\x15\xf2'
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
        # val: f = open("data.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='data.txt'>
        # val: f.close()
        # val: f = open("myfile.txt", "rb")
        # val: print(f)
        # val: #⭐ out: <_io.BufferedReader name='myfile.txt'>
        # val: f.close()
        # val: x = b"\x1a"
        # val: print(x)
        # val: #⭐ out: b'\x1a'
        # val: x = b"\x05\x15\xf2"
        # val: print(x)
        # val: #⭐ out: b'\x05\x15\xf2'
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
        # out: violetvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletvioletviolet

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
    # out: os.stat_result(st_mode=33206, st_ino=1313074, st_dev=1796, st_nlink=1, st_uid=1000, st_gid=1000, st_size=285, st_atime=1777677824, st_mtime=1777677824, st_ctime=1777677824)
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
    #here()
    #list_project_files()
    #lsalf()
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
            # out: b'f = open("data.txt", "rb")\nprint(f)\n#\xe2\xad\x90 out: <_io.BufferedReader name=\'data.txt\'>\nf.close()\nf = open("myfile.txt", "rb")\nprint(f)\n#\xe2\xad\x90 out: <_io.BufferedReader name=\'myfile.txt\'>\nf.close()\nx = b"\\x1a"\nprint(x)\n#\xe2\xad\x90 out: b\'\\x1a\'\nx = b"\\x05\\x15\\xf2"\nprint(x)\n#\xe2\xad\x90 out: b\'\\x05\\x15\\xf2\'\n2'
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