# Given an unsorted array containing numbers, find the smallest missing positive number in it.
#
# Example 1:
#
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Example 2:
#
# Input: [3, -2, 0, 1, 2]
# Output: 4
# Example 3:
#
# Input: [3, 2, 5, 1]
# Output: 4

# to find missing positive value -> put 1 at index 0..
# make negatives and 0 and 'numbers out of index' at the last of the list

def find_first_smallest_missing_positive(nums):
    i = 0
    n = len(nums)
    while i < n:
        right_index = nums[i] - 1
        if right_index >= 0 and nums[i] <= n and nums[i] != nums[right_index]:
            nums[i], nums[right_index] = nums[right_index], nums[i]
        else:
            i += 1
    print(nums)
    for index in range(n):
        if nums[index] != index + 1:
            return index + 1
    return -1

def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))

main()