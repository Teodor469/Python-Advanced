# palindrom checker

text = input()
stack = []

for i in text:
    stack.append(i)
    
reversed_word = ''
while stack:
    reversed_word += stack.pop()

if text == reversed_word:
    print('The word is palidrome')
else:
    print('The word is not a palindrome')
print(reversed_word)