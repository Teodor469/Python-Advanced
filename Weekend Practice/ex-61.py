def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))  # Output: 3 (e, o, o)
print(count_vowels("Programming is fun"))  # Output: 5 (o, a, i, o, i)