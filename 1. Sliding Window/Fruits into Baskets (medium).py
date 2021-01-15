# Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
#
# You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both the baskets.
#
# Example 1:
#
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:
#
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
from functools import reduce

def fruits_into_baskets(fruits):
    start = 0
    maxNumber = 0
    check = {}
    rememberCombo = []

    for end in range(len(fruits)):
        endFruit = fruits[end]
        if fruits[end] not in check:
            check[endFruit] = 0
        check[endFruit] += 1
        print(fruits[end+1:])

        print(check)

        while len(check.keys()) > 2:
            startFruit = fruits[start]
            check[startFruit] -= 1
            if check[startFruit] == 0:
                del check[startFruit]
            start += 1
        maxNumber = max(maxNumber, end - start + 1)
        rememberCombo = fruits[start:end+1] if len(rememberCombo) < len(fruits[start:end+1]) else rememberCombo



        print(maxNumber)
        print(check)
        print(rememberCombo)
    return maxNumber

fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])