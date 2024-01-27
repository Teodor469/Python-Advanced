def sum_of_all(n, idx):
    if idx <= 1:
        return 1
    else:
        return idx + sum_of_all(n, idx-1)

# Test the function
n = 5
result = sum_of_all(n, n)
print(f"The sum of numbers from 1 to {n} is {result}")
