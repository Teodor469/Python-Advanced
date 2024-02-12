from collections import deque

initial_fuel = [int(el) for el in input().split()]
consumption_index = deque([int(el) for el in input().split()])
quantities_needed = deque([int(el) for el in input().split()])

altitude = 0
reached_altitudes = []

while initial_fuel and consumption_index and quantities_needed:
    change = initial_fuel.pop() - consumption_index.popleft()

    if change >= quantities_needed[0]:
        quantities_needed.popleft()
        altitude += 1
        reached_altitudes.append(altitude)
        print(f"John has reached: Altitude {altitude}")
    elif change < quantities_needed[0]:
        print(f"John did not reach: Altitude {altitude + 1}")
        break

if not quantities_needed:
    print("John has reached all the altitudes and managed to reach the top!")
elif reached_altitudes:
    print("John failed to reach the top.")
    print("Reached altitudes: " + ', '.join([f"Altitude {i}" for i in reached_altitudes]))
else:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")