from collections import deque
customers = input()
queue = deque()

while customers != 'End':
    if customers == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(customers)

    customers = input()

print(f"{len(queue)} people remaining.")