# Problem Statement#
# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.
#

# Example 1:
#
# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

# Example 2:
#
# Input: [4, 6, 10], key = 4
# Output: 4

# Example 3:
#
# Input: [1, 3, 8, 10, 15], key = 12
# Output: 10

# Example 4:
#
# Input: [4, 6, 10], key = 17
# Output: 10



# We will try to search for the ‘key’ in the given array.
# - If we find the ‘key’ we will return it as the minimum difference number.
# - If we can’t find the ‘key’, (at the end of the loop) we can find the differences
#   between the ‘key’ and the numbers pointed out by indices start and end,
#   as these two numbers will be closest to the ‘key’.
#   (because when start > end, it is either start = mid + 1 or end = mid - 1)
#
# The number that gives minimum difference will be our required number.

# at last step, if arr[mid] < key
#   - start points to mid+1.. all values on left side of start (not include start) should be smaller than key
#   - end points to the value smaller than key
#
# if arr[mid] > key
#   - end points to mid-1..all value on right side of end (not include end) supposed to be larger than key
#   - start points to the value larger than key
#       nodes on left side of start always smaller than key.. so currently key point to a value smaller than key..

# note: sorted array, every round , nodes on left side of start (not include start) should be smaller than key,
#                                   nodes on right side of end (not include end) should be larger than key.



def search_min_diff_element(arr, key):
    if key < arr[0]:
        return arr[0]
    n = len(arr)

    if key > arr[n - 1]:
        return arr[n - 1]

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]

    print('start: ', start)
    print('end: ', end)

    # at the end of the while loop, 'start == end+1'
    # we are not able to find the element in the given array
    # return the element which is closest to the 'key'
    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    # print(search_min_diff_element([4, 6, 10], 4))
    # print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    # print(search_min_diff_element([4, 6, 10], 17))


main()
