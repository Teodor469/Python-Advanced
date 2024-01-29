from collections import deque

children_name = deque(input().split())
toss = int(input()) - 1

while len(children_name) > 1:
    children_name.rotate(-toss)
    removed_kid = children_name.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {children_name.popleft()}")