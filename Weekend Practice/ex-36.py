def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)
    
result = sum_natural(5)
print("Sum of first 5 natural numbers:", result)