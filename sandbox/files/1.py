def cd(n):
  if n==0: 
    print("Happy new Year!")
    return
  print(n)
  cd(n-1)
cd(3)
