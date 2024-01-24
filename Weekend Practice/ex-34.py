def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]
    
original_list = [1, 2, 3, 4, 5]
result = reverse_list(original_list)
print("Original List:", original_list)
print("Reversed List:", result)