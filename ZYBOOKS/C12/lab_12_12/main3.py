import random

##########################
def A():
    file_name = input()

    with open(file_name, "r") as f:
        photo_files = f.readlines()

    for photo in photo_files:
        photo = photo.strip()  # Remove any leading/trailing whitespace
        info_file = photo.replace("_photo.jpg", "_info.txt")
        print(info_file)
##########################
def B():
    file_name = input()

    with open(file_name, "r") as f:
        photo_names = f.readlines()

    for photo_name in photo_names:
        photo_name = photo_name.strip()
        info_name = photo_name.replace("_photo.jpg", "_info.txt")
        print(info_name)
##########################
def C():
    # Type your code here.
    a=input()
    with open(a,"r") as b:
        c = b.readlines()
    for d in c:
        d=d.strip()
        e=d.replace("_photo.jpg","_info.txt")
        print(e)
##########################

random.choice([A, B, C])()
