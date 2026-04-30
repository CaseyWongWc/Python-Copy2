##########################################################
of=open("sample.txt","w")
of.write("hello from Casey!!!!\n")
of.write("line two\n")
of.close()

inf=open("sample.txt","r")
content=inf.read()
print(inf)
# out: <_io.TextIOWrapper name='sample.txt' mode='r' encoding='UTF-8'>
inf.close()
print(content)
# out: hello from Casey!!!!
# out: line two

################################################################################
of=open("example.txt","w")
of.write("first line\n")
print(of)
# out: <_io.TextIOWrapper name='example.txt' mode='w' encoding='UTF-8'>
of.close()
print(of)
# out: <_io.TextIOWrapper name='example.txt' mode='w' encoding='UTF-8'>

of=open("example.txt","a")
of.write("appended line\n")
of.close()

inf=open("example.txt","r")
print(inf.read())
# out: first line
# out: appended line
inf.close()
print(inf)
# out: <_io.TextIOWrapper name='example.txt' mode='r' encoding='UTF-8'>

################################################################################
of=open("example.txt","w")
of.write(
  '''
  Alice
  Bob
  Casey
  '''
)
of.close()
inf=open("example.txt","r")
print(inf)
# out: <_io.TextIOWrapper name='example.txt' mode='r' encoding='UTF-8'>
print(inf.read())   # read whole file as one string[oh thank you autocorrect!]
# out: 
# out:   Alice
# out:   Bob
# out:   Casey
# out:   
for every in inf:
  print(every.strip())
inf.close()
print(inf)
# out: <_io.TextIOWrapper name='example.txt' mode='r' encoding='UTF-8'>

################################################################################
'''# 'with' auto-closes the file even if something crashes
with open("greeting.txt", "w") as f:
    f.write("Hi from Lec 13\n")

# Read it back, also using 'with'
with open("greeting.txt", "r") as f:
    text = f.read()

print(text)
print("file is auto-closed now")
'''
with open("MEEEEOWWWWWW.txt", "w") as nan:
  nan.write("meow\n")
  nan.write("yes\n")
print(nan)
# out: <_io.TextIOWrapper name='MEEEEOWWWWWW.txt' mode='w' encoding='UTF-8'>
with open("MEEEEOWWWWWW.txt", "r") as nan:
  text = nan.read()
  print(text)
  # out: meow
  # out: yes
  print(nan)
  # out: <_io.TextIOWrapper name='MEEEEOWWWWWW.txt' mode='r' encoding='UTF-8'>
print(text,nan)
# out: meow
# out: yes
# out:  <_io.TextIOWrapper name='MEEEEOWWWWWW.txt' mode='r' encoding='UTF-8'>
print("hello")
# out: hello
################################################################################
score = 95
name = "Casey"
print(score,name)
# out: 95 Casey

with open("score.txt", "w") as f:
    f.write(name + "\n")
    f.write(str(score) + "\n")
    print(f)
    # out: <_io.TextIOWrapper name='score.txt' mode='w' encoding='UTF-8'>
    try: 
      f.write(1)
    except:
      print("error","nuh-uh-uh~ (wavy finger)")
      # out: error nuh-uh-uh~ (wavy finger)
with open('score.txt','r') as f:
  print(f)
  # out: <_io.TextIOWrapper name='score.txt' mode='r' encoding='UTF-8'>
  read_name = f.readline().strip()
  read_score = int(f.readline().strip())
  print(read_name,read_score)
  # out: Casey 95
  print(read_score + 5)
  # out: 100

#yes
##################################################################################
a='''


hi








'''
print(a)
# out: 
# out: 
# out: 
# out: hi
a=a.strip()
print(a)
# out: hi
