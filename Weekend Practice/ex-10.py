a = int(input())
s = list(str(a))

stack = []

while s:
    stack.append(s.pop())

reversed_number = int(''.join(stack))

if reversed_number == a:
    print("YES")
else:
    print("NO")