
with open("test123.py", "w") as file:
# out: This is a test file.
    file.write('print("This is a test file.")\n')
    # val: 30
    for thing in range(0,5):
        print(thing)
        # out: 0
        # out: 1
        # out: 2
        # out: 3
        # out: 4
import test123
'''with bash:
    git status
    bash push_replit.sh
    .git add


    
'''

with "demo_run.py" as RUN:
    print("saved AND run as a subprocess")
    for i in range(3):
        print("tick", i)
        # out: saved AND run as a subprocess
        # out: tick 0
        # out: tick 1
        # out: tick 2
with bash:
    echo "hi from the shell"
    # out: hi from the shell
    pwd
    # out: /workspaces/Python-Copy2/sandbox/files
    ls | head -3
    # out: README.MD
    # out: S10_1
    # out: __pycache__
    ls -alf
    # out: data2.txt
    # out: helpings.py
    # out: main.py
    # out: .run_blocks
    # out: temp.py
    # out: data3.txt
    # out: test123.py
    # out: push_replit.sh
    # out: names.txt
    # out: demo_run.py
    # out: ..
    # out: __pycache__
    # out: README.MD
    # out: .
    # out: S10_1
    # out: data1.txt
    # out: tally.py
    cat data1.txt
    # out: Tia 31
    # out: Eve 14
    # out: Fay 34
    cat demo_run.py
    # out: print("saved AND run as a subprocess")
    # out: for i in range(3):
    # out:     print("tick", i)
    
