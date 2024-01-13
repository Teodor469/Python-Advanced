from collections import deque

task = input()
to_do = deque()

while task:
    if task == 'Done':
        break
    elif task == 'Did that':
        while to_do:
            print(to_do.popleft())
    else:
        to_do.append(task)

    task = input()

print(f"{len(to_do)} tasks left to do")