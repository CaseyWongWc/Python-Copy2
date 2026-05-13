def f(b):
  print(b,end=" ")
  if b<0:
    return
  f(b-3)
  print(b,end="")
f(5)
