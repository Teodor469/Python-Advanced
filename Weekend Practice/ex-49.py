from collections import deque

food_quantity = int(input())
orders = deque([int(el) for el in input().split()])
print(max(orders))

while orders:
    order = orders[0]
    if food_quantity >= order:
        orders.popleft()
        food_quantity -= order
        if len(orders) == 0:
            print("Orders complete")
            break
    elif food_quantity < order:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
