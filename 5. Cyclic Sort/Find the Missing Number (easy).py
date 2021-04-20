# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
#
# Example 1:
#
# Input: [4, 0, 3, 1]
# Output: 2
# Example 2:
#
# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7


def find_missing_number(nums):
    i, n = 0, len(nums)

    # make sure the number is at correct index, then i++
    while i < n:
        right_index = nums[i]
        if right_index < n and nums[i] != nums[right_index]:
            nums[i], nums[right_index] = nums[right_index], nums[i]
        else:
            i += 1
    print(nums)

    for i in range(n):
        if nums[i] != i:
            return i
    return -1


def main():

    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()