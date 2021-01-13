# Given a string, find the length of the longest substring in it with no more than K distinct characters.
#
# Example 1:
#
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:
#
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:
#
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_substring_with_k_distinct(str, k):
    start = 0
    substr = ''
    longest_substring = ''

    for end in range(len(str)):
        substr += str[end]
        print('Currently substring is ', substr)
        print('Current longest substring ', longest_substring)

        if not len(set(substr)) <= k:
            print('Currently substring is not valid ', substr)

            while not len(set(substr)) <= k:
                print('start shrinking from ', substr)
                start += 1
                print(' index for original string is from ', start, ' to ', end)
                substr = str[start:end + 1]
                print(' to ', substr)

        else:
            longest_substring = substr if len(longest_substring) < len(substr) else longest_substring
    print(longest_substring)
    return len(longest_substring)



longest_substring_with_k_distinct('araaci', 2)
longest_substring_with_k_distinct('araaci', 1)
longest_substring_with_k_distinct('cbbebi', 3)