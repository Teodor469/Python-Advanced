def sum_of_all(num, idx):
    if idx == len(num) - 1:
        return num[idx]
    return num[idx] + sum_of_all(num, idx + 1)
    
number = [int(x) for x in input().split()]
print(sum_of_all(number, 0))