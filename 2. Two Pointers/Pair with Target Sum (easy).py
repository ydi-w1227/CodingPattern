# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
#
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
#
# Example 1:
#
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:
#
# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

def pair_with_targetsum(arr, target_sum):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target_sum:
            print('equal')
            return [left, right]
        if arr[left] + arr[right] > target_sum:
            right -= 1
            print('right + 1: ', right)
        else:
            left += 1
            print('left + 1: ', left)
    return [-1, -1]

def pair_with_targetsum2(arr, target_sum):
    nums = {}
    for index, value in enumerate(arr):
        remains = target_sum - value
        if remains in nums:
            return [nums[remains], index]
        else:
            nums[value] = index
    return [-1, -1]

print(pair_with_targetsum2([2, 5, 9, 11], 11))