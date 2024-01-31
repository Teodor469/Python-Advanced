clothes = [int(el) for el in input().split()]
rack_capacity = int(input())
rack_copy = rack_capacity
reset_counter = 1

while clothes:
    hung_cloth = clothes.pop()
    if rack_copy - hung_cloth < 0:
        rack_copy = rack_capacity
        reset_counter += 1
    rack_copy -= hung_cloth

print(reset_counter)