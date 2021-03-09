# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
#
# Example 1:
#
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:
#
# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:
#
# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:
#
# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

def backspace_compare(str1, str2):
    first = len(str1) - 1
    second = len(str2) - 1

    while first >= 0 or second >= 0:
        i1 = getNextValidIndex(str1, first)
        i2 = getNextValidIndex(str2, second)
        if i1 < 0 and i2 < 0: # reach both end
            return True
        if i1 < 0 or i2 < 0: # reach one end
            return False
        if str1[i1] != str2[i2]:
            return False

        first = i1 - 1
        second = i2 - 1
    return True


def getNextValidIndex(string, index):
    # return next valid index which value is not #, also after applied backspace operation
    backspace_count = 0
    while index >= 0:
        if string[index] == '#': # found backspace char
            backspace_count += 1
        elif backspace_count > 0: # found non backspace char
            backspace_count -= 1
        else:                       # non backspace char and backspace count == 0
            break
        index -= 1 # only in if.. elif.. those two conditions , index will -1
    return index


print(backspace_compare("xy#z", "xzz#"))
print(backspace_compare("xy#z", "xyz#"))
print(backspace_compare("xp#", "xyz##"))
print(backspace_compare("xywrrmp", "xywrrmu#p"))