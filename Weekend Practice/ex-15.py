def func(num):
    if num % 2 == 0:
        return num * 2
    else:
        return None
    
input_list = [1, 2, 3, 4, 5, 6]
output_list = [func(num) for num in input_list]
print(output_list)