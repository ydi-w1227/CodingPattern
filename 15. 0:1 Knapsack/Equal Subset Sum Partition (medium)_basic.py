# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements
# in both subsets is equal.
#
# Example 1:
#
# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
# Example 2:
#
# Input: {1, 1, 3, 4, 7}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
# Example 3:
#
# Input: {2, 3, 4, 6}
# Output: False
# Explanation: The given set cannot be partitioned into two subsets with equal sum.


def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    return can_partition_recursive(num, s / 2, 0)


def can_partition_recursive(num, remain, currentIndex):
    print('remain: ', remain, ' currentIndex: ', currentIndex)
    if remain == 0:
        return True
    n = len(num)
    if currentIndex >= n or n == 0:
        return False

    if num[currentIndex] <= remain:
        # depth first: any branch of the tree if true, then return true and break the loop
        if can_partition_recursive(num, remain - num[currentIndex], currentIndex + 1):
            return True

    return can_partition_recursive(num, remain, currentIndex + 1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    # print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    # print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
