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
