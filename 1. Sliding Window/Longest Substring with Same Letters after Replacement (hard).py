# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
#
# Example 1:
#
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:
#
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:
#
# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

def length_of_longest_substring(str, k):
    maxRepeat = 0
    maxLength = 0
    start = 0
    check = {}

    for end in range(len(str)):
        right = str[end]
        print('Current char is: ', right)
        print('Current windowSize is: ', end - start + 1)
        if right not in check:
            check[right] = 0
        check[right] += 1
        print(check)
        maxRepeat = max(maxRepeat, check[right])
        print('maxRepeat is ', maxRepeat)
        if k + maxRepeat < end - start + 1:
            print('substring ', str[start:end+1])

            left = str[start]
            print('remove left ', left)
            check[left] -= 1
            start += 1
            print('new start is ', start)
        maxLength = max(maxLength, end - start + 1)
        print(maxLength)

    return maxLength

length_of_longest_substring('abccde', 1)