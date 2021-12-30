# Given an array of numbers which is sorted in ascending order
# and also rotated by some arbitrary number, find if a given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array.
# If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.
#
# Example 1:
#
# Input: [10, 15, 1, 3, 8], key = 15
# Output: 1
# Explanation: '15' is present in the array at index '1'.

# Example 2:
#
# Input: [4, 5, 7, 9, 10, -1, 2], key = 10
# Output: 4
# Explanation: '10' is present in the array at index '4'.

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

    if arr[start] <= arr[mid]:  # left side is sorted in ascending order
        if key >= arr[start] and key < arr[mid]:
            end = mid - 1
        else:  # key > arr[mid]
            start = mid + 1
    else:  # right side is sorted in ascending order
        if key > arr[mid] and key <= arr[end]:
            start = mid + 1
        else:
            end = mid - 1

    # we are not able to find the element in the given array
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()
