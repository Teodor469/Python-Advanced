from collections import deque

quantity_of_water = int(input())
names = input()
queue = deque()

while names != 'Start':
    queue.append(names)

    names = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        water_requested = int(data[0])
        person = queue.popleft()
        if quantity_of_water >= water_requested:
            print(f"{person} got water")
            quantity_of_water -= water_requested
        else:
            print(f"{person} must wait")
    elif len(data) == 2:
        _, refill = data
        quantity_of_water += int(refill)

    command = input()

print(f"{quantity_of_water} liters left")