a = input()
parenthesis = []

for index in range(len(a)):
    if a[index] == "(":
        parenthesis.append(index)
    elif a[index] == ")":
        start_index = parenthesis.pop()
        end_index = index + 1
        print(a[start_index:end_index])