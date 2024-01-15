# user_input = input().split()

# r = []
# reversed_sentence = ' '.join([word[::-1] for word in user_input])
# r.append(reversed_sentence)

# print(r)


text = list(input())

while text:
    print(text.pop(), end="")