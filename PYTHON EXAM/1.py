from collections import deque

amount_of_money_in_pocket = deque([int(x) for x in input().split()]) #LAST ELEMENT
prices_of_foods = deque([int(x) for x in input().split()]) #FIRST ELEMENT 

foods_eaten = 0

while amount_of_money_in_pocket and prices_of_foods:
    money_value = amount_of_money_in_pocket.pop()
    price_value = prices_of_foods[0]

    if money_value == price_value:
        prices_of_foods.popleft()
        foods_eaten += 1
    
    elif money_value > price_value:
        change = money_value - price_value
        if amount_of_money_in_pocket:
            amount_of_money_in_pocket[-1] += change
        prices_of_foods.popleft()
        foods_eaten += 1

    elif money_value < price_value:
        prices_of_foods.popleft()

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")

elif foods_eaten > 1:
    print(f"Henry ate: {foods_eaten} foods.")

elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")

if not foods_eaten:
    print("Henry remained hungry. He will try next weekend again.")
