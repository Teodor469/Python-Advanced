decimal_number = int(input())
hexadecimals = '0123456789ABCDEF'

stack = []

while decimal_number > 0:
    hex_dec = decimal_number % 16
    stack.append(hexadecimals[hex_dec])
    decimal_number //= 16 # to update the decimal in order to not divide by the same number noumerous times

while stack:
    print(stack.pop(), end="")