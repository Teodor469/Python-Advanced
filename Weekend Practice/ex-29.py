def anagrams(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    return False

print(anagrams("listen", "silent"))