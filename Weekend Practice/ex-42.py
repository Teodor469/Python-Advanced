def power_set(input_set):
    if not input_set:
        return [[]]
    
    first_subset = power_set(input_set[1:])

    second_subset = [[input_set[0]] + subset for subset in first_subset]

    return first_subset + second_subset

input_set = [1, 2, 3]
result = power_set(input_set)
print(f"The power set of {input_set} is: {result}")