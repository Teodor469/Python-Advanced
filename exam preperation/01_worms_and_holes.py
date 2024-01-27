from collections import deque

worms = [int(el) for el in input().split()]
holes = deque([int(el) for el in input().split()])

matches = 0
while worms and holes:
    worm = worms.pop()
    hole = holes[0]
    if worm == hole:
        matches += 1
        holes.popleft()
    else:
        worm -= 3
        holes.popleft()
        if worm > 0:
            worms.append(worm)

print(f"Matches: {matches}" if matches > 0 else "There are no matches.")
print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")