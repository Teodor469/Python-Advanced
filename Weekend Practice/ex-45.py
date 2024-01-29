from collections import deque

customer_name = input()
queue = deque()

while customer_name != 'End':

    if customer_name == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(customer_name)

    customer_name = input()

print(f'{len(queue)} people remaining.')