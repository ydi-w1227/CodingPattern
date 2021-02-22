# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
#
# Example 1:
#
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:
#
# Input: String="abdbca", Pattern="abc"
# Output: "bca"
# Explanation: The smallest substring having all characters of the pattern is "bca".
# Example 3:
#
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def find_substring(str1, pattern):
    matched = 0
    start = 0
    substring_start = 0
    check = {}
    min_length = len(str1) + 1

    for i in range(len(pattern)):
        current = pattern[i]
        if i not in check:
            check[current] = 0
        check[current] += 1
    print(check)

    for end in range(len(str1)):
        right_char = str1[end]
        print(right_char)
        if right_char in check:
            check[right_char] -= 1
            if check[right_char] >= 0:
                matched += 1
        print(check)
        print(matched)

        while matched == len(pattern):
            print('matched == length of pattern')
            if min_length > end - start + 1:
                min_length = end - start + 1
                substring_start = start
            print('min length: ', min_length)
            print('substring start: ', substring_start)

            left_char = str1[start]
            print('start shrinking ', left_char)
            start += 1
            if left_char in check:
                if check[left_char] == 0:
                    matched -= 1
            check[left_char] += 1
            print('matched ', matched)
            print(check)
            print('start is ', start)

    print('result: ', str1[substring_start:substring_start+min_length])
    if min_length > len(str1):
        return ""
    return str1[substring_start:substring_start+min_length]


find_substring("aabdecdad", "abc")