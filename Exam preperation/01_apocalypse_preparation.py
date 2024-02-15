from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

created_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    sum_of_items = textiles[0] + medicaments[-1]
    items = ""

    if sum_of_items == 30:
        items = "Patch"
        textiles.popleft()
        medicaments.pop()
    elif sum_of_items == 40:
        items = "Bandage"
        textiles.popleft()
        medicaments.pop()
    elif sum_of_items == 100:
        items = "MedKit"
        textiles.popleft()
        medicaments.pop()
    elif sum_of_items > 100:
        items = "MedKit"
        remaining_resources = sum_of_items - 100
        textiles.popleft()
        medicaments.pop()
        if medicaments:
            medicaments[-1] += remaining_resources
    else:
        textiles.popleft()
        medicaments[-1] += 10

    if items:
        created_items[items] += 1

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")
    
for item, amount in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    if amount > 0:
        print(f"{item} - {amount}")

if textiles:
    print("Textiles left:", ', '.join(map(str, textiles)))
if medicaments:
    print("Medicaments left:", ', '.join(map(str, reversed(medicaments))))