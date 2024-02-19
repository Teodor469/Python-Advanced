def unique(input_string):
    ele = []
    
    for el in input_string:
        if el not in ele:
            ele.append(el)

    return ele

print(unique([1, 2, 3, 2, 4, 5, 1, 3]))  # Output: [1, 2, 3, 4, 5]
print(unique(['apple', 'banana', 'orange', 'apple', 'grape']))  # Output: ['apple', 'banana', 'orange', 'grape']