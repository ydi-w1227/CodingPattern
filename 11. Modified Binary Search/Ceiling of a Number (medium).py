# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
#
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
#
# Example 1:
#
# Input: [4, 6, 10], key = 6
# Output: 1
# Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
# Example 2:
#
# Input: [1, 3, 8, 10, 15], key = 12
# Output: 4
# Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
# Example 3:
#
# Input: [4, 6, 10], key = 17
# Output: -1
# Explanation: There is no number greater than or equal to '17' in the given array.
# Example 4:
#
# Input: [4, 6, 10], key = -1
# Output: 0
# Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.



# here,in general case we supposed value of key is always in between of arr[start] and arr[end]

# We will try to search for the ‘key’ in the given array. If we find the ‘key’, we return its index as the ceiling.
# If we can’t find the ‘key’, the next big number will be pointed out by the index start.

# say at last step, arr[mid] < key, start will point to mid + 1 which is next larger number than mid..
# e.g. 13, 15, 16, key = 14
# s1 = 13, e1 = 16, m1 = 15.. 15 > 14, means when index > m1, value > key
# s2 = 13, e2 = 13, m2 = 13.. since 13 < 14, means we can say, just now.. when index < m1, value < key
# so start points to mid + 1 in next step.. which is the first value > key and it will be the result
#
# if arr[mid] > key, start doesn't move and end will point to mid - 1
# if this is the last step, which means start == mid and end will move to mid - 1 which will break the loop
# thinking in a way that the last value start and mid points to must be larger than half of the array already (right half of array)
# we look into right half, means all left half is smaller than key
# we keep adjust the range..
# supposed this last value is larger than key.. means when we move end = mid - 1, it will be smaller than key..
# i.e. mid - 1 must be smaller than key, so that we shrink the range and not include it in previous steps..

# e.g. 12, 13, 16, key = 14
# s1 = 12, e1 = 16, m1 = 13.. 13 < 14, means when index < m1, value < key
# s2 = 16, e2 = 16, m2 = 16.. since 14 < 16, means we can say, just now.. when index > m1, value > key
# so in this case, we will move end pointer which breaks the loop..
# and our start already points to the result.. (boundary)

# counter case will be 12, 13, 14, key = 15, however we consider value of key should be between the start to end of the array.. so this is not in discussion..

# so start points to mid + 1 in next step.. which will be the result
#
# Since we are always adjusting our range to find the ‘key’,
# when we exit the loop, the start of our range will point to the smallest number greater than the ‘key’
#



def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    if key > arr[n - 1]:  # if the 'key' is bigger than the biggest element
        return -1

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # found the key
            return mid

    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    # we are not able to find the element in the given array, so the next big number will be arr[start]
    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
