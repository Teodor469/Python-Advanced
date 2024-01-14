user_input = input()

opening_brackets = '([{'
closing_brackets = ')]}'

stack = []

for char in user_input:
    if char in opening_brackets:
        stack.append(char)
    elif char in closing_brackets:
        if not stack:
            print("NO")
            break
        top = stack.pop()
        if opening_brackets.index(top) != closing_brackets.index(char):
            print("NO")
            break
        
    
else:
    if not stack:
        print("YES")
    else:
        print("NO")