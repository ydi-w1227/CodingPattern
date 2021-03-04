# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.
#
# Example 1:
#
# Input: [2, 5, 3, 10], target=30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:
#
# Input: [8, 2, 6, 5], target=50
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
# Explanation: There are seven contiguous subarrays whose product is less than the target.

from collections import deque
def find_subarrays(arr, target):
    result = []
    product = 1
    start = 0
    for end in range(len(arr)):
        product *= arr[end]

        # define the position of start
        while product >= target and start < len(arr):
            product /= arr[start]
            start += 1

        # after start and end are set, all possible subarrays between (start, end) are valid
        # add all continuous subarray into result
        temp_list = deque()
        for i in range(end, start-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))

    return result

print(find_subarrays([2, 5, 3, 10], 30))