from functools import reduce


def operate(operator, *nums):
    result = nums[0]

    for n in nums[1:]:
        if operator == '+':
            result += n
        elif operator == '-':
            result -= n
        elif operator == '*':
            result *= n
        elif operator == '/':
            if n != 0:
                result /= n
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda x, y: x+y, args)
    elif operator == '-':
        return reduce(lambda x, y: x-y, args)
    elif operator == '*':
        return reduce(lambda x, y: x*y, args)
    elif operator == '/':
        return reduce(lambda x, y: x/y, args)