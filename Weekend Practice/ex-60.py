def is_palindrome(input_string):
    if input_string.lower() == input_string[::-1].lower():
        return True
    return False

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))