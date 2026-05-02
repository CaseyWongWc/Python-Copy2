with "helpings.py":
    from pickle import GLOBAL
    from pathlib import Path
    import shutil
    import subprocess
    import builtins


    ROOT = Path.cwd()


    def here():
        return ROOT


    def make_dir(path):
        p = ROOT / path
        p.mkdir(parents=True, exist_ok=True)
        return p


    def make_file(path, content=""):
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return p


    def remove_path(path):
        p = ROOT / path
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()
        return p


    def run_cmd(*cmd):
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode


    def cmd(*cmd):
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
        if result.stderr:
            return result.stderr
        return result.stdout


    def ret_file(path):
        p = ROOT / path
        return p.read_text(encoding="utf-8")


    def list_project_files():
        return cmd("find", ".", "-maxdepth", "2", "-type", "f")


    def lsalf():
        return cmd("ls", "-alF")


    def INFO():
        return str(ROOT) + "\n" + cmd("date") + list_project_files()


    def setin(*inputs):
        """
        A helper function to set test inputs for the input() function.
        Usage:
        setin("input1", "input2", "input3")
        This will set up the input() function to return "input1" on the first call,
        "input2" on the second call, and so on.
        To reset to normal input behavior, call setin() with no arguments or None:
        setin()
        """
        if inputs:
            input_iter = iter(inputs)

            def mock_input(prompt=""):
                try:
                    value = next(input_iter)
                    print(f"{prompt}{value}")
                    return value
                except StopIteration:
                    raise EOFError("No more inputs for testing")

            builtins.input = mock_input
        else:
            builtins.input = builtins._original_input_backup


    def quiz(section_id, questions, prompt_label="Answer"):
        """
        Run a multi-question participation activity.

        questions = list of (question_text, expected_answer) tuples.
        Uses your existing setin() for staged inputs.

        Example:
            setin("True", "False", "True")
            quiz("11.1.2", [
                ("car_sticker_price", True),
                ("todays_temperature", False),
                ("inventory_quantity", True),
            ])
        """
        print(f"━━━ ✏️  Quiz {section_id} ━━━")
        correct = 0
        for i, (item, expected) in enumerate(questions, 1):
            try:
                answer = input(f"  {i}) {item}: ")
            except EOFError:
                print(f"  ⚠️  No more staged inputs at question {i}")
                break

            ok = str(answer).strip().lower() == str(expected).strip().lower()
            if ok:
                print(f"     ✅ Correct!")
                correct += 1
            else:
                print(f"     ❌ Got '{answer}', expected '{expected}'")

        total = len(questions)
        print(f"━━━ Score: {correct}/{total} ━━━\n")
        return correct, total

with "README.MD":
    # zyBooks Chapter 10 (Sections 10.1–10.12)
    ---

    ## Checklist + scores

    | Section | Earned | Possible | Status | Notes |
    | --- | --- | --- | --- | --- |
    | --- | ---: | ---: | --- | --- |
    | 10.1 | 3 | 10 | ⏳ In progress | Participation: 10.1.1 (1/1), 10.1.2 (2/2). Challenges: 10.1.1 (0/4), 10.1.2 (0/3). |
    | 10.2 | 0 | 9 | ⬜ Not started | Participation: 10.2.1 (0/1), 10.2.2 (0/3). Challenges: 10.2.1 (0/3), 10.2.2 (0/2). |
    | 10.3 | 0 | 7 | ⬜ Not started | Participation: 10.3.1 (0/1). Challenges: 10.3.1 (0/4), 10.3.2 (0/2). |
    | 10.4 | 0 | 4 | ⬜ Not started | Participation: 10.4.1 (0/3). Challenge: 10.4.1 (0/1). |
    | 10.5 | 0 | 4 | ⬜ Not started | Participation: 10.5.1 (0/1), 10.5.2 (0/2). Challenge: 10.5.1 (0/1). |
    | 10.6 | 0 | 3 | ⬜ Not started | Participation: 10.6.1 (0/3). |
    | 10.7 | 0 | 10 | ⬜ Not started | Lab: 10.7.1 (0/10). |
    | 10.8 | 0 | 10 | ⬜ Not started | Lab: 10.8.1 (0/10). |
    | 10.9 | 0 | 10 | ⬜ Not started | Lab: 10.9.1 (0/10). |
    | 10.10 | 0 | 10 | ⬜ Not started | Lab: 10.10.1 (0/10). |
    | 10.11 | 0 | 10 | ⬜ Not started | Lab: 10.11.1 (0/10). |
    | 10.12 | 0 | 10 | ⬜ Not started | Lab: 10.12.1 (0/10). |

    ---

    ## Links

    - [Section 10.1](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/1)
    - [Section 10.2](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/2)
    - [Section 10.3](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/3)
    - [Section 10.4](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/4)
    - [Section 10.5](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/5)
    - [Section 10.6](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/6)
    - [Section 10.7](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/7)
    - [Section 10.8](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/8)
    - [Section 10.9](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/9)
    - [Section 10.10](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/10)
    - [Section 10.11](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/11)
    - [Section 10.12](https://learn.zybooks.com/zybook/CPPCS2520NguyenSpring2026/chapter/10/section/12)

2+3
# val: 5
######### val: 5
##############################################################################
##############################################################################
print(r'''{1
# out: {1
# out:       7
# out:                         9
# out:       
# out:       3
# out: 
# out:                     5
# out:            2}
      7
                        9
      
      3

                    5
           2}''')

print(1+2)
# out: 3

2;3
# val: 2
# val: 3
5
# val: 5

7
# val: 7
2
# val: 2
4
# val: 4
from Helpers.helpings import *
INFO()
# val: /home/runner/workspace/sandbox/files
# val: Sat May  2 12:31:11 PM UTC 2026
# val: ./names.txt
# val: ./data1.txt
# val: ./data2.txt
# val: ./data3.txt
# val: ./temp.py
# val: ./main.py
# val: ./README.MD
# val: ./S10_1/README.MD
# val: ./helpings.py
#✨️✨️✨️✨️✨️✨️✨️✨️✨️✨️


# in: 123
user_input = ""
while user_input != "q":
    weight = int(input("Enter weight (in pounds): "))
    height = int(input("Enter height (in inches): "))

    bmi = (float(weight) / float(height * height)) * 703
    print(f"BMI: {bmi}")
    print("(CDC: 18.6-24.9 normal)\n")
    # Source www.cdc.gov

    user_input = input('Enter any key ("q" to quit): ')
# !err: --- ERROR ---
# !err: Traceback (most recent call last):
# !err:   File "<string>", line 132, in <module>
# !err:   File "/home/runner/workspace/sandbox/notebook/goog.py", line 194, in <module>
# !err:     2;3
# !err:     ^^^^
# !err: NameError: name 'cache' is not defined
