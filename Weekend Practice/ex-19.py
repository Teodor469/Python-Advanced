def two_sum(nums, target):
    complement_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_dict:
            return [complement_dict[complement], i]
        complement_dict[num] = i

input_nums = [2, 7, 11, 15]
target_sum = 9
output_result = two_sum(input_nums, target_sum)
print(output_result)