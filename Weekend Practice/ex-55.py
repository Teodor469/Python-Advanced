def fibonacci(num):
    if num <= 1:
        return num
    
    return (fibonacci(num - 1) + fibonacci(num - 2))

a = int(input())
print(fibonacci(a))
