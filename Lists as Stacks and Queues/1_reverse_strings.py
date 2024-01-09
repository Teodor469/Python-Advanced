# a = list(input())
# while a:
#     print(a.pop(), end="")

text = list(input())
stack = []
for i in range(len(text)):
    stack.append(text.pop())
print("".join(stack))