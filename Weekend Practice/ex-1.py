text = list(input())
stack = []

for _ in range(len(text)):
    a = text.pop() #txet - after storing the values LIFO
    stack.append(a)
print(''.join(stack))