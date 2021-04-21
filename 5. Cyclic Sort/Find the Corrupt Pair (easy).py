# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
#
# Example 1:
#
# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.
# Example 2:
#
# Input: [3, 1, 2, 3, 6, 4]
# Output: [3, 5]
# Explanation: '3' is duplicated and '5' is missing.

def find_corrupt_numbers(nums):
    i = 0
    n = len(nums)
    while i < n:
        right_index = nums[i] - 1
        if right_index < n and nums[i] != nums[right_index]:
            nums[i], nums[right_index] = nums[right_index], nums[i]
        else:
            i += 1
    print(nums)
    for index in range(n):
        if index + 1 != nums[index]:
            return [nums[index], index + 1]
    return [-1, -1]


def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()
