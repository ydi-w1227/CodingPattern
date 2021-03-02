# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
#
# Example 1:
#
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:
#
# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:
#
# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.

import math
def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf

    # only traverse possible index of first value of triplets
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            # exact sum
            if target_diff == 0:
                return target_sum - target_diff

            # if there is more than one solution
            if abs(target_diff) < abs(smallest_difference) or (
                    abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff  # save the closest and the biggest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_difference