# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
#
# Example 1:
#
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:
#
# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
# Example 3:
#
# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted
# Example 4:
#
# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

import math

def shortest_window_sort(arr):
    small = 0
    large = len(arr) - 1

    # find the first time when arr[small] > arr[small+1]
    while small < len(arr) - 1 and arr[small] <= arr[small + 1]:
        small += 1

    # means this array is sorted
    if small == len(arr) - 1:
        return 0

    # find the first time when arr[large-1] > arr[large]
    while large > 0 and arr[large-1] <= arr[large]:
        large -= 1

    subarr_max = -math.inf
    subarr_min = math.inf
    for key in range(small, large + 1):
        subarr_max = max(arr[key], subarr_max)
        subarr_min = min(arr[key], subarr_min)


    # extend the subarray to include bigger value which is bigger than minOfSubArray on left side of the array
    while small > 0 and arr[small-1] > subarr_min:
        small -= 1
    # extend the subarray to include smaller value which is smaller than maxOfSubArray on right side of the array
    while large < len(arr) - 1 and arr[large+1] <subarr_max:
        large += 1

    return large - small + 1


print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(shortest_window_sort([1, 2, 3]))
print(shortest_window_sort([3, 2, 1]))