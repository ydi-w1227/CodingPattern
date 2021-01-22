# Given a string, find the length of the longest substring, which has no repeating characters.
#
# Example 1:
#
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:
#
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:
#
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".


def non_repeat_substring(str):
  start = 0
  maxLength = 0
  check = {}

  for end in range(len(str)):
    right = str[end]
    print('current char is ', right)
    if right in check:
      print('current char exists ')
      start = max(start, check[right]+1)
      print(start)
    check[right] = end
    print(check)
    maxLength = max(maxLength, end-start+1)
    print("current max string is ", str[start:end+1])
  return maxLength



non_repeat_substring("pwabwkew")
# mistake made: start = duplicate character index
# counter example: when end = 4, maxLength is 4 (pwab)
#                   start jump to 4, but it supposed to be 2, maxLength is 5 (abwke)

# start > check[rights]+1 (when end=3, b's last index is 0, start=2 )
non_repeat_substring("baabcd")