# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
#
# Example 1: #
# Input: {1, 1, 2, 3}, S=4
# Output: 3
# The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
# Note that we have two similar sets {1, 3}, because we have two '1' in our input.
# Example 2: #
# Input: {1, 2, 7, 1, 5}, S=9
# Output: 3
# The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

def count_subsets(num, sum):
    return count_subsets_recursive(num, sum, 0)


def count_subsets_recursive(num, sum, currentIndex):
    # base checks

    # this condition should be checked first!!
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # recursive call after selecting the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[currentIndex] <= sum:
        sum1 = count_subsets_recursive(
            num, sum - num[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = count_subsets_recursive(num, sum, currentIndex + 1)

    return sum1 + sum2


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
