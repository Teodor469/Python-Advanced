from collections import deque

tools = deque([int(el) for el in input().split()])
substances = [int(el) for el in input().split()]
challenges = [int(el) for el in input().split()]

while substances and tools and challenges:
    result = tools[0] * substances[-1]

    if result in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(result)
    else:
        tools[0] += 1
        tools.append(tools.popleft())
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

if challenges and not substances:
    print("Harry is lost in the temple. Oblivion awaits him.")
elif not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print("Tools:", ", ".join(map(str, tools)))

if substances:
    print("Substances:", ", ".join(map(str, substances)))

if challenges:
    print("Challenges:", ", ".join(map(str, challenges)))