symbols = ("-", ",", ".", "!", "?")

with open(r"File Handling Exercise/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    reversed_words = ' '.join(text[row].split()[::-1])
    print(reversed_words)
