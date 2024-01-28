expression = input()

stack = []

for el in range(len(expression)):
    if expression[el] == '(':
        stack.append(el)
    elif expression[el] == ')':
        start = stack.pop()
        end = el + 1
        print(expression[start:end])

    