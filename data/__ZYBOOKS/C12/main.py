colors_data = input()
one_color_val = input()

colors_file = open(colors_data, "a+")  # Open the file for reading and appending

colors_file.write(one_color_val)  # Write the new color value to the file
colors_file.flush()  # Forces the output buffer to write to disk

# When a file is in update mode, seek(0, 0) rewinds the file to enable reading from the beginning
colors_file.seek(0, 0)

file_data = colors_file.read()  # Read the contents of the file
print(file_data)  # Print the contents of the file

colors_file.close()  # Close the file
