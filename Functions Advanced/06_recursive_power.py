# def recursive_power(number, power):
#     return number ** power


# correct
def recursive_power(number, power) -> int:
    if power == 0:
        return 1
    else:
        return number * recursive_power(number, power - 1)
    
    
print(recursive_power(2, 10))