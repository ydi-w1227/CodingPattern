# Given a string and a pattern, find out if the string contains any permutation of the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
#
# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters, it will have n!n! permutations.
#
# Example 1:
#
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:
#
# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:
#
# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:
#
# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def find_permutation(str, pattern):
    start = 0
    checkPattern = {}
    patternLen = len(pattern)
    matched = 0

    for char in pattern:
        if pattern not in checkPattern:
            checkPattern[char] = 0
        checkPattern[char] += 1
    print('check: ', checkPattern)

    for end in range(len((str))):
        current = str[end]
        print('current: ', current)
        if current in checkPattern:
            print('match')
            checkPattern[current] -= 1
            if checkPattern[current] == 0:
                matched += 1
        if matched == len(checkPattern):
            print('true')
            return True

        if end - start + 1 > patternLen:
            start += 1
            leftChar = str[start]
            if leftChar in checkPattern:
                if checkPattern[leftChar] == 0:
                    matched -= 1
                checkPattern[leftChar] += 1
        print(checkPattern)
    print('false')
    return False


# find_permutation('oidbcaf', 'abc')
find_permutation("odicf", "dc")
# find_permutation("bcdxabcdy", "bcdyabcdx")
# find_permutation("aaacb", "abc")