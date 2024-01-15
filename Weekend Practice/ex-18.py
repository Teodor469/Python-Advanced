def contamination(text, char):
    if text and char:
        return char * len(text)
    else:
        return ''

a = input()
b = input()

print(contamination(a, b))