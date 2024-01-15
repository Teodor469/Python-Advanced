def count_of_letters(word):
    vowels = 'aeiou'
    count = 1

    for element in word:
        if element in vowels:
            count += 1

    return count