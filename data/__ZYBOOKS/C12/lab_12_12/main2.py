file_name = input()

with open(file_name, "r") as f:
    photo_names = f.readlines()

for photo_name in photo_names:
    photo_name = photo_name.strip()
    info_name = photo_name.replace("_photo.jpg", "_info.txt")
    print(info_name)