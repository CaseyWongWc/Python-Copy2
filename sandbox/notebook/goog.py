with "1.py" as f:
  def cd(n):
    if n==0: 
      print("Happy new Year!")
      # out: Happy new Year!
      return
    print(n)
    # out: 3
    # out: 2
    # out: 1
    cd(n-1)
    # val: None
    # val: None
    # val: None
  cd(3)
  # val: None
  # f.out: 3
  # f.out: 2
  # f.out: 1
  # f.out: Happy new Year!
  
with "2.py" as f:
  def fact(n,res=1):
    if n==1 or n==0:
      n
      # val: 1
      return res
    n
    # val: 4
    # val: 3
    # val: 2
    return fact(n-1,n*res)
  print(fact(4))
  # out: 24
  # f.out: 24
with "3.py" as f:
  def fact(n,res=1):
    if n==1 or n==0:
      n
      # val: 0
      return res
    res=1
    for i in range(1,n+1):
      res *=i
      res
      # val: 1
      # val: 2
      # val: 6
      # val: 24
    return res
  print(fact(4))
  # out: 24
  print(fact(0))
  # out: 1
  # f.out: 24
  # f.out: 1
with  "4.py" as f:
  def fib(n):
    if n == 1 or n == 2:
      return 1
    return  fib(n-1) + fib(n-2)
  print(fib(4))
  # out: 3
  # f.out: 3
with  "5.py" as f:
    import functools

    @functools.lru_cache

    def fib(n):
        if n == 1 or n == 2:
         return 1
        return fib(n-1) + fib(n-2)
    print(fib(200))
    # out: 280571172992510140037611932413038677189525
    # f.out: 280571172992510140037611932413038677189525
with _:
  with "MYENV/hello.py" as f:
  # !err: SyntaxError: invalid syntax (body line 4)
    import pandas as pd

    df = pd.DataFrame(
      "name":['Alex', 'Ben'],
      "grade": [85,92.5]
    )
  with bash:
    touch hello.py
    python -V
    # out: Python 3.11.14
    which python3
    # out: /home/runner/workspace/.pythonlibs/bin/python3
    python -m venv .venv
    pip install pandas
    # err: error: externally-managed-environment
    # err: 
    # err: × This environment is externally managed
    # err: ╰─> This command has been disabled as it tries to modify the immutable
    # err:     `/nix/store` filesystem.
    # err:     
    # err:     To use Python with Nix and nixpkgs, have a look at the online documentation:
    # err:     <https://nixos.org/manual/nixpkgs/stable/#python>.
    # err: 
    # err: note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
    # err: hint: See PEP 668 for the detailed specification.
    # !err: exit code 1
