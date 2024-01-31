import os
import re

words = os.path.join("Lab File Handling", "words.txt")
text = os.path.join("Lab File Handling", "text.txt")
output_file = os.path.join("Lab File Handling", "text1.txt")

with open(words) as file:
    searched_words_as_text = file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]


with open(text) as file:
    content = file.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    results = re.findall(pattern, content)
    words_count[searched_word] = results.count(searched_word)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_file, "a") as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")