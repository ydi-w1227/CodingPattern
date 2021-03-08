# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
#
# Example 1:
#
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Example 2:
#
# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.

def search_pairs(arr, target, i, j, quadruplets):
    left = j + 1
    right = len(arr) - 1
    while left < right:
        current_sum = arr[i] + arr[j] + arr[left] + arr[right]

        if current_sum == target:
            quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left-1] == arr[left]:
                left += 1
            while left < right and arr[right+1] == arr[right]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1


def search_quadruplets(arr, target):
    quadruplets = []
    arr.sort()

    print('sorted arr: ', arr)
    for i in range(0, len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)
    print(quadruplets)
    return quadruplets

search_quadruplets([4, 1, 2, -1, 1, -3], target=1)