user_input = int(input("Enter a number: "))

stack = []

while user_input > 0:
    binary_division = user_input % 2
    stack.append(binary_division)
    user_input //= 2

print("The binary equivalent is:", end=" ")
while stack:
    print(stack.pop(), end="")