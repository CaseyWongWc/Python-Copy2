file_name = input()

with open(file_name, "r") as f:
    photo_files = f.readlines()

for photo in photo_files:
    photo = photo.strip()  # Remove any leading/trailing whitespace
    info_file = photo.replace("_photo.jpg", "_info.txt")
    print(info_file)
