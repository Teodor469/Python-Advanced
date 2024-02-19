def count_chars(string):

    chars = {}

    for char in string:
        chars[char] = chars.get(char, 0) + 1

    return chars

a = input()
print(count_chars(a))