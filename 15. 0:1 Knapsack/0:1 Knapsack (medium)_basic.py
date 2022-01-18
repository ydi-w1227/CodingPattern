#Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’
# The goal is to get the maximum profit out of the knapsack items. Each item can only be selected once,
# as we don’t have multiple quantities of any item.
#
# Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit.
# ere are the weights and profits of the fruits:
#
# Items: { Apple, Orange, Banana, Melon }
# Weights: { 2, 3, 1, 4 }
# Profits: { 4, 5, 3, 7 }
# Knapsack capacity: 5
#
# Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:
#
# Apple + Orange (total weight 5) => 9 profit
# Apple + Banana (total weight 3) => 7 profit
# Orange + Banana (total weight 4) => 8 profit
# Banana + Melon (total weight 5) => 10 profit
#
# This shows that Banana + Melon is the best combination as it gives us the maximum profit,
# and the total weight does not exceed the capacity.

# Given two integer arrays to represent weights and profits of ‘N’ items,
# we need to find a subset of these items which will give us maximum profit
# such that their cumulative weight is not more than a given number ‘C.’
# Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
#

# p1 - calculate with profits[currentIndex]
# p2 - calculate without profits[currentIndex]
# e.g.  A(index = 0) is selected -> p1
#       or A(index = 0) is not selected -> p2 (select next, i.e. B)

def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, currentIndex):
    print('input: ', capacity, ' ', currentIndex)
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        print('current weight is: ', weights[currentIndex])
        profit1 = profits[currentIndex] + knapsack_recursive(
                profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    print('p1: ', profit1)
    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    print('p2: ', profit2)
    print('max: ', max(profit1, profit2))
    return max(profit1, profit2)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()

