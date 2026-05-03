names = [
    "Ryley",
    "Edan",
    "Reagan",
    "Henry",
    "Caius",
    "Jane",
    "Guto",
    "Sonya",
    "Tyrese",
    "Johnny",
]
index = int(input())

try:
    print(f"Name: {names[index]}")
except IndexError as excpt:
    print(f"Exception! {excpt}")
    if index < 0:
        print(f"The closest name is: {names[0]}")
    else:
        print(f"The closest name is: {names[-1]}")
