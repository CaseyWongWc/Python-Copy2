
##########################EXERCISE 6
def divide_and_convert(a,b,text):
  try:
    result=a/b
    number=int(text)
    print(f"result: {result}, number: {number}")
    # out: result: 5.0, number: 5
    # out: result: 5.0, number: 99
  except ZeroDivisionError:
    print("can't divide by zero!")
    # out: can't divide by zero!
  except ValueError:
    print(f"can't turn '{text}' into a number!")
    # out: can't turn 'cat' into a number!

divide_and_convert(10,2,"5")
divide_and_convert(10,0,"5")
divide_and_convert(10,2,"cat")
    
divide_and_convert(10,2,"99")

##########################EXERCISE 7

'''with open("a.txt","w") as a:
  a.write("hello!")

print(open("a.txt","r"))
b= open("a.txt","r")
print(b)
print(b.read()) # read whole file as one string[oh thank you autocorrect!]
b.close()
import os
os.remove("a.txt")'''


'''def s_o(name):
  try:
    f_=open(name,"r")
    content=f_.read()
  except FileNotFoundError:
    print(f"'{name}' doesn't exist")
  else:
    print(f"got it: {content.strip()}")
    f_.close()
  finally:
    print(f"done trying with {name}")
    print("---")

  with open("real.txt","w") as f_:
    f_.write("hello!")
    
  s_o("real.txt")
  s_o("Nuh_Uh.txt")''' #ack i got stuck on this one due to indentation

print(1+1)
# out: 2

def s_o(name):
    try:
      f_=open(name,"r")
      content=f_.read()
    except FileNotFoundError:
      print(f"'{name}' doesn't exist")
      # out: 'Nuh_Uh.txt' doesn't exist
    else:
      print(f"got it: {content.strip()}")
      # out: got it: hello!
      f_.close()
    finally:
      print(f"done trying with {name}")
      # out: done trying with real.txt
      # out: done trying with Nuh_Uh.txt
      print("---")
      # out: ---
      # out: ---
with open("real.txt","w") as f_:
  f_.write("hello!")

s_o("real.txt")
s_o("Nuh_Uh.txt")

##########################EXERCISE 7 SCRATCH
class hello:
  try:
    1+1 == 3
    print("yes")
    # out: yes
  except:
    print("no")
  
  print(1+1 == 3)
  # out: False
class hello:
  try:
    asdf
    print("yes")
  except:
    print("no")
    # out: no

class hello:
  try:
    asdf
    print("yes")
  except:
    asdf=1
    print("except")
    # out: except
    if asdf==1:
      print("if")
      # out: if
      del asdf
  else:
    print("else")
  finally:
    print("finally")
    # out: finally
##########################EXERCISE 8
def withdraw(bal,amt):
  if amt<0:
    raise ValueError("can't withdraw a negative amount")
  if amt>bal:
    raise ValueError(f"insufficient funds: have {bal}, want {amt}")
  return bal-amt
withdraw(100,30)
print(withdraw(100,30))
# out: 70

#temp=withdraw(100,999999999999)
#print(temp)

try:
  new_balance=withdraw(123,30)
  print(f"new balance: {new_balance}")
  # out: new balance: 93
except ValueError as err:
  print(f"oops: {err}")

class SANDBOX:
  def IneedToFaster(a,b):
    try:
      new_balance=withdraw(a,b)
      print(f"new balance: {new_balance}")
      # out: new balance: 70
    except ValueError as err:
      print(f"oops: {err}")
      # out: oops: insufficient funds: have 100, want 9999999999999999
      # out: oops: can't withdraw a negative amount
      
  IneedToFaster(100,30)
  IneedToFaster(100,9999999999999999)
  IneedToFaster(100,-5)

  def yes(a,b):
    try:
      new_balance=withdraw(a,b)
      print(f"new balance: {new_balance}")
      # out: new balance: 70
    except ValueError as err:
      print(f"oops: {err}")
      # out: oops: insufficient funds: have 100, want 9999999999999999
      # out: oops: can't withdraw a negative amount
      print(ValueError.__class__)
      # out: <class 'type'>
      # out: <class 'type'>
  yes(100,30)
  yes(100,9999999999999999)
  yes(100,-5)
del SANDBOX

##########################YIPIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
##########################AT THE BOTTOM
try:
  with open("cs2520_lec13_exceptions_exercises.md","r") as f:
    #print(f.read())
    pass
except:
   print("cs2520_lec13_exceptions_exercises.md is not found (Orrr,its buried in old folder,i think)")








