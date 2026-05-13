
# in: 2
def even_or_odd():
    raw = input("ask for a number: ")
    # out: ask for a number: 2
    try:
        n = int(raw)
    except ValueError:
        return f"{raw} is not a number 😅"
    return "even" if n % 2 == 0 else "odd"

print(even_or_odd())
# out: even

# ============================
# STEP 5 - LOOPS (copy to paper!)
# ============================

# --- for loop with range ---
for i in range(5):
    print("i =", i)
    # out: i = 0
    # out: i = 1
    # out: i = 2
    # out: i = 3
    # out: i = 4
# range(5)       -> 0,1,2,3,4
# range(2,6)     -> 2,3,4,5
# range(0,10,2)  -> 0,2,4,6,8  (step)

# --- for loop over a list ---
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)
    # out: apple
    # out: banana
    # out: cherry

# --- while loop ---
n = 1
while n < 100:
    print(n)
    # out: 1
    # out: 2
    # out: 4
    # out: 8
    # out: 16
    # out: 32
    # out: 64
    n = n * 2     # 1,2,4,8,16,32,64
# WARNING: forget to change n -> infinite loop!

# --- break and continue ---
for i in range(10):
    if i == 3:
        continue   # skip this iteration
    if i == 7:
        break      # exit loop entirely
    print(i)
    # out: 0
    # out: 1
    # out: 2
    # out: 4
    # out: 5
    # out: 6
# prints: 0,1,2,4,5,6

# --- mini challenge: 7 times table ---
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
    # out: 7 x 1 = 7
    # out: 7 x 2 = 14
    # out: 7 x 3 = 21
    # out: 7 x 4 = 28
    # out: 7 x 5 = 35
    # out: 7 x 6 = 42
    # out: 7 x 7 = 49
    # out: 7 x 8 = 56
    # out: 7 x 9 = 63
    # out: 7 x 10 = 70
list(range(1,11))
# val: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ==================================
# STEP 6 (detour) - RECURSION
# ==================================
# Recursion = a function that CALLS ITSELF
# with a smaller version of the problem.
#
# Every recursion needs TWO things:
#   1) BASE CASE  -> when to STOP
#   2) RECURSIVE CASE -> shrink + call self
# Forget #1 -> infinite recursion -> RecursionError

# --- example 1: count down ---
def countdown(n):
    if n == 0:           # BASE CASE
        print("blastoff!")
        # out: blastoff!
        return
    print(n)
    # out: 5
    # out: 4
    # out: 3
    # out: 2
    # out: 1
    countdown(n - 1)     # RECURSIVE CASE (smaller)
    # val: None
    # val: None
    # val: None
    # val: None
    # val: None

countdown(5)
# val: None

# --- example 2: factorial (n!) ---
# 5! = 5*4*3*2*1 = 120
def fact(n):
    if n <= 1:           # BASE: 1! = 1, 0! = 1
        return 1
    return n * fact(n - 1)   # n * (n-1)!

print(fact(5))   # 120
# out: 120

# --- example 3: YOUR times-table, fixed ---
# a*b done by repeated addition
def tt(a, b):
    if b == 1:           # BASE
        return a
    return a + tt(a, b - 1)

print(tt(7, 10))   # 70
# out: 70

# --- example 4: print every row of the 7 table recursively ---
def table(a, b):
    if b > 10:           # BASE: stop after 10
        return
    print(a, "x", b, "=", a * b)
    # out: 7 x 1 = 7
    # out: 7 x 2 = 14
    # out: 7 x 3 = 21
    # out: 7 x 4 = 28
    # out: 7 x 5 = 35
    # out: 7 x 6 = 42
    # out: 7 x 7 = 49
    # out: 7 x 8 = 56
    # out: 7 x 9 = 63
    # out: 7 x 10 = 70
    table(a, b + 1)      # next row
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

table(7, 1)
# val: None

# --- HOW TO THINK ABOUT IT ---
# fact(3)
#   = 3 * fact(2)
#       = 3 * (2 * fact(1))
#           = 3 * (2 * 1)
#       = 3 * 2
#   = 6
# Each call waits for the smaller one to return.

# --- COMMON BUGS ---
# 1) No base case -> RecursionError: max depth exceeded
# 2) Base case never reached (wrong direction)
#    e.g. countdown(n+1) instead of n-1
# 3) Forgetting `return` -> function gives back None

# ==================================
# STEP 7 - LISTS (your data BFF)
# ==================================
# A list = an ORDERED collection of items.
# Square brackets, items separated by commas.

fruits = ["apple", "banana", "cherry"]
nums   = [10, 20, 30, 40, 50]
mixed  = [1, "hi", 3.14, True]   # any types allowed
empty  = []

# --- INDEXING (starts at 0!) ---
print(fruits[0])    # apple
# out: apple
print(fruits[1])    # banana
# out: banana
print(fruits[-1])   # cherry  (negative = from the end)
# out: cherry

# --- LENGTH ---
print(len(fruits))  # 3
# out: 3

# --- SLICING [start:stop]  (stop is EXCLUSIVE) ---
print(nums[1:4])    # [20, 30, 40]
# out: [20, 30, 40]
print(nums[:3])     # [10, 20, 30]
# out: [10, 20, 30]
print(nums[2:])     # [30, 40, 50]
# out: [30, 40, 50]
print(nums[::-1])   # [50,40,30,20,10] (reversed!)
# out: [50, 40, 30, 20, 10]

# --- CHANGE an item ---
fruits[1] = "blueberry"
print(fruits)       # ['apple','blueberry','cherry']
# out: ['apple', 'blueberry', 'cherry']

# --- ADD items ---
fruits.append("date")          # add to END
# val: None
fruits.insert(0, "apricot")    # add at index 0
# val: None
print(fruits)
# out: ['apricot', 'apple', 'blueberry', 'cherry', 'date']

# --- REMOVE items ---
fruits.remove("apple")   # by value
# val: None
last = fruits.pop()      # remove + return last
print(fruits, "removed:", last)
# out: ['apricot', 'blueberry', 'cherry'] removed: date

# --- LOOP through a list ---
for f in fruits:
    print("I like", f)
    # out: I like apricot
    # out: I like blueberry
    # out: I like cherry

# with index too:
for i, f in enumerate(fruits):
    print(i, "->", f)
    # out: 0 -> apricot
    # out: 1 -> blueberry
    # out: 2 -> cherry

# --- USEFUL FUNCTIONS ---
print(sum(nums))    # 150
# out: 150
print(min(nums))    # 10
# out: 10
print(max(nums))    # 50
# out: 50
print(sorted(nums)) # new sorted list
# out: [10, 20, 30, 40, 50]

# --- MEMBERSHIP ---
print("cherry" in fruits)   # True or False
# out: True

# --- LIST COMPREHENSION (fancy one-liner) ---
squares = [x*x for x in range(1, 6)]
print(squares)      # [1, 4, 9, 16, 25]
# out: [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)        # [0,2,4,...,18]
# out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# --- GOTCHA: lists are MUTABLE ---
a = [1, 2, 3]
b = a               # NOT a copy! same list, two names
b.append(4)
# val: None
print(a)            # [1,2,3,4]   <- a changed too!
# out: [1, 2, 3, 4]

c = a.copy()        # real copy
c.append(99)
# val: None
print(a, c)
# out: [1, 2, 3, 4] [1, 2, 3, 4, 99]


# ==================================
# STEP 8 - FUNCTIONS DEEP-DIVE
# ==================================
# Functions = REUSABLE blocks of code.
# Define ONCE, call MANY times.

# --- basic shape ---
def greet(name):           # 'name' is a PARAMETER
    return "Hi " + name    # returns a value

msg = greet("Casey")       # "Casey" is the ARGUMENT
print(msg)                 # Hi Casey
# out: Hi Casey

# --- multiple parameters ---
def add(a, b):
    return a + b

print(add(3, 5))           # 8
# out: 8

# --- DEFAULT values ---
def greet2(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet2("Casey"))                 # Hello, Casey!
# out: Hello, Casey!
print(greet2("Casey", "Yo"))           # Yo, Casey!
# out: Yo, Casey!
print(greet2(name="Casey", greeting="Hey"))  # KEYWORD args
# out: Hey, Casey!

# --- return MULTIPLE values (as a tuple) ---
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 7, 1, 9, 3])
print(lo, hi)              # 1 9
# out: 1 9

# --- *args  -> any number of positional args ---
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))   # 10
# out: 10

# --- **kwargs -> any number of keyword args ---
def describe(**info):
    for k, v in info.items():
        print(k, "=", v)
        # out: name = Casey
        # out: age = 20
        # out: school = CPP

describe(name="Casey", age=20, school="CPP")
# val: None

# --- SCOPE: variables inside a function are LOCAL ---
x = 10
def f():
    x = 99       # local x, doesn't touch outer x
    print("inside:", x)
    # out: inside: 99
f()
# val: None
print("outside:", x)   # still 10
# out: outside: 10

# To modify the outer one (rare, usually avoid):
# def f(): global x; x = 99

# --- DOCSTRINGS (write what the function does) ---
def square(n):
    """Return n squared."""
    return n * n

help(square)   # shows the docstring
# val: None

# --- LAMBDA: tiny anonymous functions ---
double = lambda x: x * 2
print(double(7))           # 14
# out: 14

# Often used with sorted/map/filter:
pairs = [("a", 3), ("b", 1), ("c", 2)]
print(sorted(pairs, key=lambda p: p[1]))
# out: [('b', 1), ('c', 2), ('a', 3)]
# sorted by the 2nd element

# --- THE GOLDEN RULES ---
# 1) One function = one job.
# 2) Name it like a verb: get_user(), calc_total()
# 3) Inputs come in via parameters, outputs via return.
# 4) Avoid using globals; pass things in.
# 5) Add a docstring for anything non-obvious.
###########
###
with _ as OUTS1:
    class A:
        def __init__(self):
            self.a=0
            A
            # val: <class '__main__.__sc_1__.<locals>.A'>
            # val: <class '__main__.__sc_1__.<locals>.A'>
        def __repr__(self):
            print(f"😨")
            # out: 😨
            # out: 😨
            # out: 😨
            return f"A({self.a})"
        def __str__(self):
            return f"A({self.a})"

    c,b=A(),A()
    c
    # val: A(0)
    # OUTS1.out: 😨
    
    
OUTS1
# val: Scratch(c=A(0), b=A(0), A=<class '__main__.__sc_1__.<locals>.A'>, out=['😨'], err=[], outs='😨')
