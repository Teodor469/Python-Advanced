from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
gas_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    gas_tank += petrol

    if gas_tank >= distance:
        gas_tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_tank = 0
print(index)

# def can_complete_circle(petrol_pumps):
#     n = len(petrol_pumps)

#     for start in range(n):
#         petrol_tank = 0
#         for i in range(n):
#             petrol_tank += petrol_pumps[(start + i) % n][0] - petrol_pumps[(start + i) % n][1]

#             if petrol_tank < 0:
#                 break
#         else:
#             return start

#     return -1  # If no solution is found

# # Input reading
# N = int(input())
# petrol_pumps = []
# for _ in range(N):
#     petrol, distance = map(int, input().split())
#     petrol_pumps.append((petrol, distance))

# # Output
# result = can_complete_circle(petrol_pumps)
# print(result)
