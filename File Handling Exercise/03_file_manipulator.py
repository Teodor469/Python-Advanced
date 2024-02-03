import os

while True:
    command, *info = input().split('-')

    if command == "Create":
        with open(fr"File Handling Exercise/{info[0]}", "w"): pass

    elif command == "Add":
        with open(fr"File Handling Exercise/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(fr"File Handling Exercise/{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occured")

    elif command == "Delete":
        try:
            os.remove(fr"File Handling Exercise/{info[0]}")
        except FileNotFoundError:
            print("An error occured")
    elif command == "End":
        break