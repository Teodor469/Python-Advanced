a = input()
stack = []

for i in range(len(a)):
    if a[i] == '(':
        stack.append(i)
    elif a[i] == ')':
        start_index = stack.pop()
        end_index = i + 1
        print(a[start_index:end_index])