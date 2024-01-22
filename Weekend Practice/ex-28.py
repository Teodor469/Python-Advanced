def first_non_repeat_char(word):
    for char in word:
        if word.count(char) <= 1:
            return char
        
print(first_non_repeat_char("pppython"))