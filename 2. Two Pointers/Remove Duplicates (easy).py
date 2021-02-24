# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
#
# Example 1:
#
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:
#
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].


# shift left
def remove_duplicates(arr):
    non_duplicate_index = 0

    for check_duplicate in range(1, len(arr)):
        if arr[check_duplicate] != arr[non_duplicate_index]:
            non_duplicate_index += 1
            arr[non_duplicate_index] = arr[check_duplicate]
    return non_duplicate_index + 1

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
# print(remove_duplicates([2, 2, 2, 11]))


