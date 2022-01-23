# create a matrix and store the value (i.e. max(profit1, profit2)) which is already calculated
# looking for value from matrix first, if exists then return, if not then calculate it
# rest of the code similar to basic solution
# to update value in matrix, needs to calculate max(profit1, profit2) like basic solution, then return it
# matrix should be #profits rows, #capacity columns, i.e. how much profit it will be when we have #capacity left..
#       -> end goal is to make capacity as closer to 0 as possible
#                        or till the last elements in array

# In the top-down approach, a complex algorithm is broken down into smaller fragments,
# better known as ‘modules.’
# These modules are then further broken down into smaller fragments until they can no longer be fragmented.
# This process is called ‘modularization.


def solve_knapsack(profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):

    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(
        dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()






