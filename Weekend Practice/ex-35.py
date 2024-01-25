def palindrome(s):
    def clean_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    cleaned_s = clean_string(s)

    # Base case: an empty string or a string with one character is a palindrome
    if len(cleaned_s) <= 1:
        return True
    # Recursive case: check if the first and last characters are equal, then check the rest
    elif cleaned_s[0] == cleaned_s[-1]:
        return palindrome(cleaned_s[1:-1])
    else:
        return False

string1 = "level"
string2 = "A man, a plan, a canal: Panama"

print(f'Is "{string1}" a palindrome? {palindrome(string1)}')
print(f'Is "{string2}" a palindrome? {palindrome(string2)}')
