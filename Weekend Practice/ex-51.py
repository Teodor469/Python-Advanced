parentheses_sequence = input()

open_brackets = '([{'
closed_brackets = ')]}'

stack = []

for bracket in parentheses_sequence:
    if bracket in open_brackets:
        stack.append(bracket)
    elif bracket in closed_brackets:
        if not stack:
            print("NO")
            break
        top = stack.pop()
        if open_brackets.index(top) != closed_brackets.index(bracket):
            print("NO")
            break
else:
    if not stack:
        print("YES")
    else:
        print("NO")
