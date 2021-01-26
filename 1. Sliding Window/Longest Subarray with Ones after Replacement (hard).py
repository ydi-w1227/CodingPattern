#
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
#
# Example 1:
#
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:
#
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

def length_of_longest_substring(arr, k):
    oneCount = 0
    start = 0
    longest = 0

    for end in range(len(arr)):
        print('current ', arr[end])
        if arr[end] == 1:
            oneCount += 1
        print('oneCount ', oneCount)

        if end - start + 1 - oneCount > k:
            print('> k ')
            if arr[start] == 1:
                oneCount -= 1
            start += 1
            print('oneCount after -1 ', oneCount)
            print('start after +1 ', start)

        longest = max(longest, end - start + 1)
        print('longest ', longest)
        print('\n')
    return longest

length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)