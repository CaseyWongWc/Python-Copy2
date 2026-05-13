a=input("ask for a number:")
try:
  a=int(a)
  a
except TypeError:
  a=str(a)
  a=ord(a)
  print(f"{a} is not a number but i will solve you anyways")
except Exception as e:
   print(f"error: {e}")
   return e
finally:
  return "even" if  a%2==0 else "odd"
