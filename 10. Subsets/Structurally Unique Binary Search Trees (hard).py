# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST)
# that can store values 1 to ‘n’?
#
# Example 1:
#
# Input: 2
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:
#       1               2
#        \             /
#         2           1
#
# Example 2:
#
# Input: 3
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1 to 3:
#       1               1               2              3               3
#        \               \             / \            /               /
#         2               3           1   3          1               2
#          \             /                            \             /
#           3           2                              2           1

# take i as root, from node #start (=1 in the first round) to node #(i - 1) goes to left
# because all nodes start from #start, to which are (1 less than i) will go to left, when i is root.
# for all possible nodes on the left side of root i, loop through each of them.
# i.e. take each of them as sub-root, and go through all possibilities.
#
# same as that,  from node #(n - i) to node #end (=n in the first round) goes to right,
#
# e.g. n = 3, i = 1, which takes node 1 as root right now..
# then left side will be node from 1 to i - 1 which are from 1 to 0.. which is invalid range..
# which means there is no node smaller than 1..
# right side will be from node 2 to 3
# which means there are two possible node on the right subtree side of root node 1

# so we take this (start = 2, end = 3) to the recursive loop, which means the possibilities for node 2 and node 3
# go into recursive loop again.. consider each case..
# all of the following case, start = 2, end = 3
# i in range [2,4) => i = 2 (node 2 as sub-root), left range is (2, 1) -> new (start, end)
#                                                   -> next loop will return None which means end of the path
#                                                right range is (3, 3) -> new (start, end)
#                                                   -> index = 3, left (3, 2), right (4, 3) both end
#                                               -> means that considers node 2 as sub-root, node 3 is its right subtree
#                 => i = 3 (node 3 as sub-root), left range is (2, 2) -> new (start, end)
#                                                   -> index = 2, left (2, 1) right (3, 2) both end
#                                                right range is (4, 3)
#                                               -> means that considers node 3 as sub-root, node 2 is its left subtree
#


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return 'root: ' + str(self.val if self.val else None) + \
               ' , left: ' + str(self.left.val if self.left else None) + \
               ' , right: ' + str(self.right.val if self.right else None) + ';;'


def find_unique_trees(n):
    if n <= 0:
        return []
    return findUnique_trees_recursive(1, n)


def findUnique_trees_recursive(start, end):
    result = []
    # base condition, return 'None' for an empty sub-tree
    # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
    # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
    # both of these should return 'None' for the left and the right child
    if start > end:
        print('append None')
        result.append(None)
        return result

    for i in range(start, end+1):
        print('start < end: ', start, ' ', end)
        print('- index: ', i)

        print('go to left: ', start, ' ', i-1)
        # making 'i' the root of the tree
        # from start to i-1, go to left
        leftSubtrees = findUnique_trees_recursive(start, i - 1)
        if None not in leftSubtrees:
            print('leftSubtrees: ', [str(x) for x in leftSubtrees])
        else:
            print('leftSubtrees: ', leftSubtrees)

        print('go to right: ', i+1, ' ', end)
        # from i + 1 to end, go to right
        rightSubtrees = findUnique_trees_recursive(i + 1, end)
        if None not in rightSubtrees:
            print('rightSubtrees: ', [str(x) for x in rightSubtrees])
        else:
            print('rightSubtrees: ', rightSubtrees)

        for leftTree in leftSubtrees:
            for rightTree in rightSubtrees:
                root = TreeNode(i)
                root.left = leftTree
                root.right = rightTree
                result.append(root)
                print('- append to result: ', str(root))

        print('- result: ', [str(x) for x in result])
        print('\n')

    return result


def main():
    # print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
