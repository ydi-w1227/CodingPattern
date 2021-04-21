# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
#
# Example 1:
#
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
# Example 2:
#
# Input: [2, 4, 1, 2]
# Output: 3
# Example 3:
#
# Input: [2, 3, 2, 1]
# Output: 4

def find_missing_numbers(nums):
    missingNumbers = []
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
        if nums[index] - 1 != index:
            missingNumbers.append(index + 1)
    return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()
