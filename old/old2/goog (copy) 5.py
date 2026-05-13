'''def explore(remain, picked):
    #print("DEBUG:", "remain =", remain, "picked =", picked)

    if len(remain) == 0:
        print("EMIT:", picked)
        return

    for i in range(len(remain)):
        
        new_remain = remain[:i] + remain[i+1:]
        new_picked = picked + [remain[i]]
        
        print(f"RECURSE: i={i}, new_remain={new_remain}, new_picked={new_picked}",(remain[:i] , remain[i+1:],picked , [remain[i]]))
        explore(new_remain, new_picked)

explore([1, 2, 3], [])
#class 12.12 LAB: File name change
[x for x in [1,2,3]]
[x for x in [1,2,3] if x>1]
[x for x in [1,2,3] if x>1 if x<3]
import os
os.path.join("subdir", "output.txt")
os.path.join("sounds", "cars", "honk.mp3")
'''
from ctypes.wintypes import HBRUSH
with _:
    class MyClass:

        def __init__(self):
            self.x = 1
            print("WAAAAWAAA")
            # out: WAAAAWAAA

        def __repr__(self): # This is the method that is called by repr()
            def explore(remain, picked):
                #print("DEBUG:", "remain =", remain, "picked =", picked)

                if len(remain) == 0:
                    print("EMIT:", picked)
                    # out: EMIT: [1, 2, 3]
                    # out: EMIT: [1, 3, 2]
                    # out: EMIT: [2, 1, 3]
                    # out: EMIT: [2, 3, 1]
                    # out: EMIT: [3, 1, 2]
                    # out: EMIT: [3, 2, 1]
                    # out: EMIT: [1, 2, 3]
                    # out: EMIT: [1, 3, 2]
                    # out: EMIT: [2, 1, 3]
                    # out: EMIT: [2, 3, 1]
                    # out: EMIT: [3, 1, 2]
                    # out: EMIT: [3, 2, 1]
                    return

                for i in range(len(remain)):

                    new_remain = remain[:i] + remain[i+1:]
                    new_picked = picked + [remain[i]]

                    print(f"RECURSE: i={i}, new_remain={new_remain}, new_picked={new_picked}",(remain[:i] , remain[i+1:],picked , [remain[i]]))
                    # out: RECURSE: i=0, new_remain=[2, 3], new_picked=[1] ([], [2, 3], [], [1])
                    # out: RECURSE: i=0, new_remain=[3], new_picked=[1, 2] ([], [3], [1], [2])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[1, 2, 3] ([], [], [1, 2], [3])
                    # out: RECURSE: i=1, new_remain=[2], new_picked=[1, 3] ([2], [], [1], [3])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[1, 3, 2] ([], [], [1, 3], [2])
                    # out: RECURSE: i=1, new_remain=[1, 3], new_picked=[2] ([1], [3], [], [2])
                    # out: RECURSE: i=0, new_remain=[3], new_picked=[2, 1] ([], [3], [2], [1])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[2, 1, 3] ([], [], [2, 1], [3])
                    # out: RECURSE: i=1, new_remain=[1], new_picked=[2, 3] ([1], [], [2], [3])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[2, 3, 1] ([], [], [2, 3], [1])
                    # out: RECURSE: i=2, new_remain=[1, 2], new_picked=[3] ([1, 2], [], [], [3])
                    # out: RECURSE: i=0, new_remain=[2], new_picked=[3, 1] ([], [2], [3], [1])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[3, 1, 2] ([], [], [3, 1], [2])
                    # out: RECURSE: i=1, new_remain=[1], new_picked=[3, 2] ([1], [], [3], [2])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[3, 2, 1] ([], [], [3, 2], [1])
                    # out: RECURSE: i=0, new_remain=[2, 3], new_picked=[1] ([], [2, 3], [], [1])
                    # out: RECURSE: i=0, new_remain=[3], new_picked=[1, 2] ([], [3], [1], [2])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[1, 2, 3] ([], [], [1, 2], [3])
                    # out: RECURSE: i=1, new_remain=[2], new_picked=[1, 3] ([2], [], [1], [3])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[1, 3, 2] ([], [], [1, 3], [2])
                    # out: RECURSE: i=1, new_remain=[1, 3], new_picked=[2] ([1], [3], [], [2])
                    # out: RECURSE: i=0, new_remain=[3], new_picked=[2, 1] ([], [3], [2], [1])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[2, 1, 3] ([], [], [2, 1], [3])
                    # out: RECURSE: i=1, new_remain=[1], new_picked=[2, 3] ([1], [], [2], [3])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[2, 3, 1] ([], [], [2, 3], [1])
                    # out: RECURSE: i=2, new_remain=[1, 2], new_picked=[3] ([1, 2], [], [], [3])
                    # out: RECURSE: i=0, new_remain=[2], new_picked=[3, 1] ([], [2], [3], [1])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[3, 1, 2] ([], [], [3, 1], [2])
                    # out: RECURSE: i=1, new_remain=[1], new_picked=[3, 2] ([1], [], [3], [2])
                    # out: RECURSE: i=0, new_remain=[], new_picked=[3, 2, 1] ([], [], [3, 2], [1])
                    explore(new_remain, new_picked)
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None
                    # val: None

            explore([1, 2, 3], [])
            # val: None
            # val: None
            #class 12.12 LAB: File name change
            [x for x in [1,2,3]]
            # val: [1, 2, 3]
            # val: [1, 2, 3]
            [x for x in [1,2,3] if x>1]
            # val: [2, 3]
            # val: [2, 3]
            [x for x in [1,2,3] if x>1 if x<3]
            # val: [2]
            # val: [2]
            import os
            os.path.join("subdir", "output.txt")
            # val: subdir/output.txt
            # val: subdir/output.txt
            os.path.join("sounds", "cars", "honk.mp3")
            # val: sounds/cars/honk.mp3
            # val: sounds/cars/honk.mp3

            return "hi"
    qwqwqw=MyClass()
    qwqwqw
    # val: hi
    print(qwqwqw)
    # out: hi

with _:
    helloworld = r"""
        +------+.      +------+       +------+       +------+      .+------+
    |`.    | `.    |\     |\      |      |      /|     /|    .' |    .'|
    |  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
    |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
    +---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+
     `. |    `.|    \|     \|     |      |     |/     |/    |.'    | .'
       `+------+     +------+     +------+     +------+     +------+'

    """
    with open(helloworld,"w") as f:
        f.write("""""")
        # !err: FileNotFoundError: [Errno 2] No such file or directory: "\n    +------+.      +------+       +------+       +------+      .+------+\n|`.    | `.    |\\     |\\      |      |      /|     /|    .' |    .'|\n|  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |\n|   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |\n+---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+\n `. |    `.|    \\|     \\|     |      |     |/     |/    |.'    | .'\n   `+------+     +------+     +------+     +------+     +------+'\n\n    "
        # !err:   at line 74: # out: RECURSE: i=0, new_remain=[], new_picked=[3, 2, 1] ([], [], [3, 2], [1])



yes=f'''+------+.      +------+       +------+       +------+      .+------+
|`.    | `.    |\     |\      |      |      /|     /|    .' |    .'|
|  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
|   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
+---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+
 `. |    `.|    \|     \|     |      |     |/     |/    |.'    | .'
   `+------+     +------+     +------+     +------+     +------+'
'''

with f"""{yes}.py""" as f:
    print()
# !err: --- ERROR ---
# !err: Traceback (most recent call last):
# !err:   File "<string>", line 224, in <module>
# !err:   File "/home/runner/workspace/sandbox/notebook/goog.py", line 88, in <module>
# !err:     # out: RECURSE: i=1, new_remain=[1], new_picked=[3, 2] ([1], [], [3], [2])
# !err: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# !err: TypeError: 'str' object does not support the context manager protocol
