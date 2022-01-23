#Contrary to the top-down approach, bottom-up programming focuses on designing an algorithm
# by beginning at the very basic level and building up as it goes.

# capacity  0  1  2  3  4  5  6  7
# index   0 0  1  1  1  1  1  1  1
#         1 0  1  6  7  7  7  7  7
#         2 0  1  6  10 11 16 17 17
#         3 0  1  6  10 11 16 17 22

# matrix will store the max profit till index = i (i.e. i items)
# value will be: max(dp[i-1][capacity], profits[i] + dp[i-1][capacity-weights[i]])
#         1 - without choosing index i
#         2 - choose index i, plus max profits which is until index i-1 and capacity = capacity - weights[i]
# option 2 only be calculated when capacity - weights[i] > 0, which means still have capacity to add index i
#
#

def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)

    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()

