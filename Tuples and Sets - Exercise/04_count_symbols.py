# occurances = {}

# for letter in input():
#     occurances[letter] = occurances.get(letter, 0) + 1

# for letter, times in sorted(occurances.items()):
#     print(f"{letter}: {times} time/s")

text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")