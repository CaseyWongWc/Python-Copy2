# 14.8 LAB: All permutations of names (zyBooks 14.8.1)
# Input: single line space-separated names, e.g. "Julia Lucas Mia"
# Output: comma-separated permutations, one per line, in the order shown.

def print_all_permutations(permList, nameList):
    if len(nameList) == 0:
        print(', '.join(permList))
    else:
        for i in range(len(nameList)):
            new_perm = permList + [nameList[i]]
            new_remain = nameList[:i] + nameList[i+1:]
            print_all_permutations(new_perm, new_remain)


if __name__ == "__main__":
    nameList = input().split(" ")
    permList = []
    print_all_permutations(permList, nameList)
