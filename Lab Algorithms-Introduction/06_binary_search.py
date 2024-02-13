def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_element = numbers[mid_idx]

        if mid_element == target:
            return mid_idx
        elif mid_element < target:
            left = mid_idx + 1
        elif mid_element > target:
            right = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))