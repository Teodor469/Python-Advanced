import os

file_name = "text.txt"

if os.path.exists(file_name):
    try:
        with open(file_name) as file:
            print("File found")
    except FileNotFoundError:
        print("File is not found despite existence. There might be an issue with file permissions.")
else:
    print("File does not exist in the specified location.")