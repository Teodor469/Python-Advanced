text = input()

try:
    times = int(input())
    print(times*times)
except ValueError:
    print("Variable times must be an integer")