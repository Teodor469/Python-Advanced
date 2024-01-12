# def are_parentheses_balanced(user_input):
#     stack = []
#     open_parentheses = '({['
#     closing_parentheses = ')}]'

#     for index, char in enumerate(user_input):
#         if char in open_parentheses:
#             stack.append((char, index))
#         elif char in closing_parentheses:
#             if not stack or not is_matching(stack[-1][0], char):
#                 return 'NO'
#             stack.pop()

#     return 'YES' if not stack else 'NO'

# def is_matching(opening, closing):
#     return (opening == '(' and closing == ')') or \
#            (opening == '{' and closing == '}') or \
#            (opening == '[' and closing == ']')

# user_input = input()
# result = are_parentheses_balanced(user_input)
# print(result)


user_input = input()

stack = []
open_parentheses = '({['
close_parentheses = ']})'
parentheses_pairs = {')': '(', '}': '{', ']': '['}

for char in user_input:
    if char in open_parentheses:
        stack.append(char)
    elif char in close_parentheses:
        if not stack or parentheses_pairs[char] != stack[-1]:
            print('NO')
            break
        else:
            stack.pop()
else:
    print('YES' if not stack else 'NO')
