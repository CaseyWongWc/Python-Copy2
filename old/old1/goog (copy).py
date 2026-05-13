import os

for name in os.listdir("."):
    info = os.stat(name)

    if os.path.isdir(name):
        marker = "/"
    else:
        marker = ""

    print(info.st_size, name + marker)
    # out: 42 .cache/
    # out: 3077 .gitignore
    # out: 84 .local/
    # out: 122 uv.lock
    # out: 157 pyproject.toml
    # out: 60 .upm/
    # out: 86 .pythonlibs/
    # out: 9927 generated-icon.png
    # out: 658 .replit
    # out: 0 .agents/
    # out: 0 test/
    # out: 12 AAAAAAAA.txt
    # out: 138 yes.py
    # out: 4570 inline_output.py
    # out: 134 .git/
    # out: 58 __pycache__/
    # out: 72 main.py
    # out: 23 customers.txt
    # out: 1235 goog.py
print(1+1)
# out: 2
for a in range(1,5):
    print(a)
    # out: 1
    # out: 2
    # out: 3
    # out: 4
with open("customers.txt", "w") as f:
    f.write("Taylor\n")
    f.write("Bruno\n")

with open("customers.txt", "r") as f:
    data = f.read()

print(data)
# out: Taylor
# out: Bruno
with open("AAAAAAAA.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
with open("AAAAAAAA.txt", "r") as f:
     data = f.read()
print(data)
# out: Hello
# out: World

###
with open("customers.txt", "a") as f:
    f.write("Echo\n")

with open("customers.txt", "r") as f:
    print(f.read())
    # out: Taylor
    # out: Bruno
    # out: Echo


with open("customers.txt", "a") as f:
    f.write("Miku\n")

with open("customers.txt", "r") as f:
    for line in f:
        print(line.rstrip())
        # out: Taylor
        # out: Bruno
        # out: Echo
        # out: Miku
with open("yes.py", "w") as hello: hello.write("print('Hello World')\nprint('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')")

with open("yes.py", "r") as hello: print(hello.read())
# out: print('Hello World')
# out: print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

with open("yes.py", "r") as hello:
    for line in hello:
        print(line.rstrip())
        # out: print('Hello World')
        # out: print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

with open("yes.py", "r") as hello:
    for line in hello:
        print(line.rstrip())
        # out: print('Hello World')
        # out: print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
