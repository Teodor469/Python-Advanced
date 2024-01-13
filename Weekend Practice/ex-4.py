from  collections import deque

children = deque(input().split())
toss = int(input()) - 1

while len(children) > 1:
    children.rotate(-toss)
    removed_kid = children.popleft()
    print(f"Removed {removed_kid}")
print(f"Last is {children.popleft()}")