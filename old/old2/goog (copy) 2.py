with "1.py" as f:
  def cd(n):
    if n==0: 
      print("Happy new Year!")
      return
    print(n)
    cd(n-1)
  cd(3)
  
with "2.py" as f:
  def fact(n,res=1):
    if n==1 or n==0:
      n
      return res
    n
    return fact(n-1,n*res)
  print(fact(4))
with "3.py" as f:
  def fact(n,res=1):
    if n==1 or n==0:
      n
      return res
    res=1
    for i in range(1,n+1):
      res *=i
      res
    return res
  print(fact(4))
  print(fact(0))
with  "4.py" as f:
  def fib(n):
    if n == 1 or n == 2:
      return 1
    return  fib(n-1) + fib(n-2)
  print(fib(4))
with  "5.py" as f:
  import functools

  @functools.lru_cache

  def fib(n):
      if n == 1 or n == 2:
       return 1
      return fib(n-1) + fib(n-2)
  print(fib(200))

with "MYENV/hello.py" as f:
  import pandas as pd
  df = pd.DataFrame({
    "name":['Alex', 'Ben'],
    "grade": [85,92.5]
  })
    


with bash:
  touch hello.py
  python -V
  # out: Python 3.11.14
  which python3
  # out: /home/runner/workspace/.pythonlibs/bin/python3
  python -m venv .venv
  
  pip install pandas  --break-system-packages
  # out: Requirement already satisfied: pandas in /home/runner/workspace/.pythonlibs/lib/python3.11/site-packages (3.0.2)
  # out: Requirement already satisfied: numpy>=1.26.0 in /home/runner/workspace/.pythonlibs/lib/python3.11/site-packages (from pandas) (2.4.4)
  # out: Requirement already satisfied: python-dateutil>=2.8.2 in /home/runner/workspace/.pythonlibs/lib/python3.11/site-packages (from pandas) (2.9.0.post0)
  # out: Requirement already satisfied: six>=1.5 in /home/runner/workspace/.pythonlibs/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
  python -m venv MYENV
  python -V
  # out: Python 3.11.14
  which python3
  # out: /home/runner/workspace/.pythonlibs/bin/python3
  pwd
  # out: /home/runner/workspace/sandbox/files
  uv init --python 3.13.10
  # err: error: Project is already initialized in `/home/runner/workspace/sandbox/files` (`pyproject.toml` file exists)
  # !err: exit code 2
  #uv run python -V
  #uv run which python
  #python hello.py
  uv run python hello.py
  # err: error: No interpreter found for Python >=3.13.10 in search path
  # err: 
  # err: hint: A managed Python download is available for Python >=3.13.10, but Python downloads are set to 'never'
  # !err: exit code 2

1
a=1
def f():
  a=3
  a
  for i in range(3):
    print(i)
    a=2
  a
  while a>0:
    a-=1
    a
  a
f()
a
del a,f
class a:
   def __init__(self):
     self.a=1
   def f(self):
     self.a=2
     self.a
     for i in range(3):
       print(i)
       self.a=3
     self.a
     while self.a>0:
       self.a-=1
       self.a
     self.a
try:
    x = int("oops")
except ValueError as e:
    print("bad")
finally:
    print("done")
with _:
  raise NameError("1")
with _:
  raise ValueError("1")
with _:
  q
with _:
  int("oops")
with _:
  raise SyntaxError("invalid syntax")
with _:
  9/0
with _:
  class Helloworld(Exception):
     pass
  Helloworld
  with _:
    raise Helloworld("hello")
  try:
     raise Helloworld("hello")
  except Helloworld as e:
     print(e)
  else:
    pass
  finally:
    try:
      0/0
    except  ZeroDivisionError as e:
      print(e)
    else:
      pass
    finally:
      try:
        abc="abc"
        del abc
      except  NameError as e:
        print(e)
      else:
        print("my hello world 2")
 def f(b):
  print(b,end=" ")
  if b<0:
    return
  f(b-3)
  print(b,end="")
f(5)
# !err: --- ERROR ---
# !err: IndentationError on line 148: indented 1 space(s), but no open block matches that level.
# !err:   line 147 was indented 8 space(s) — pick a level that lines up with an outer block.
