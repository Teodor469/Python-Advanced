from collections import deque

monsters_armor = deque([int(el) for el in input().split(',')])
striking_impact = [int(el) for el in input().split(',')]

killed_monsters = 0

while monsters_armor and striking_impact:
    armor = monsters_armor.popleft()
    strike = striking_impact.pop()

    if strike >= armor:
        killed_monsters += 1
        strike -= armor
        
        if striking_impact:
            striking_impact[-1] += strike
        elif not striking_impact and strike > 0:
            striking_impact.append(strike)
    else:
        armor -= strike
        monsters_armor.append(armor)

if not monsters_armor:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
