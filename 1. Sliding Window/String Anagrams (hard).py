# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
#
# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
#
# Example 1:
#
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:
#
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

# worse scenario time complexity is O(M+N),
# maybe because need to traverse N times for str,
# also worse case is every index is included in result... (abcabcabc, abc)
# in that case, every traversal char is in dict so need to check char_frequency which is O(1)
# and every time shrink window, there is a check again O(1)
# and worse case is: need to check all char in pattern (M) totally in N times traverse..
# where char_frequency = len(pattern) = M means all identical char in pattern


def find_string_anagrams(str, pattern):
    result_indexes = []
    matched = 0
    char_frequency = {}
    start = 0

    # get frequency of pattern
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    print('original frequency is ', char_frequency)

    for end in range(len(str)):
        rightChar = str[end]

        # if match then -1
        if rightChar in char_frequency:
            print('in')
            char_frequency[rightChar] -= 1
            if char_frequency[rightChar] == 0:
                matched += 1

        print('frequency is ', char_frequency)
        print('matched is ', matched)

        # if matched == len(char_frequency), which means identical char is same..
        if matched == len(char_frequency):
            print('start is ', start)
            # return start index
            result_indexes.append(start)

        # shrink window, make sure current window size < pattern and check if left char is in dict..
        if end - start + 1 >= len(pattern):
            print('window len: ', end - start + 1)
            leftChar = str[start]
            print(leftChar)
            start += 1
            if leftChar in char_frequency:
                if char_frequency[leftChar] == 0:
                    matched -= 1
                char_frequency[leftChar] += 1
            print('after, frequency is ', char_frequency)
            print('after, matched is ', matched)
            print('\n')

    print(result_indexes)
    return result_indexes

# find_string_anagrams('abcabcabc', 'abc')
find_string_anagrams('abbcabc', 'abc')