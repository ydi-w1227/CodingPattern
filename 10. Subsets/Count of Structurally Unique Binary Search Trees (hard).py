# Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST)
# that can store values 1 to ‘n’.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.
# Example 2:
#
# Input: 3
# Output: 5
# Explanation: There will be 5 unique BSTs that can store numbers from 1 to 3.

# there are n nodes, loop through every node, and consider it as a root.
# e.g. take i as root, (i - 1) nodes goes to left, (n - i) goes to right.
# since node smaller than i goes to left, node larger than i goes to right
# e.g. n = 3, i = 1, which takes a node (i.e. node 1) as root..
# for left side, i - 1 which is 0.. means there is no node on the left side (i.e smaller than 1..)
# which considered as the only one option for left side (i.e. end of the path)
# for right side, n - i which is 2, in this case, means there are two nodes on right subtree
#
# go into recursive loop again.. consider these two nodes..
# n = 2, i = 1, left = 0, right = 1 means when i = 1 (i.e. node 2) as root, one on the right
# n = 2, i = 2, left = 1, right = 0 means when i = 2 (i.e. node 3) as root, one on the left
# go to next loop for each side, this is the end of the recursive loop
# loop through until n <= 1 means 1 or 0 nodes... which considered as the only one option for current side (i.e. end of the path)
#
# another example.. say from a root node, left subtree has 2 options, right subtree has 2 options,
# then there are 4 cases in total.. with those 2*2 combination on both side..
# thats why for each root node, or sub-root node, we calculate how many combinations are there and added as part of the final result


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
    print('current n: ', n)
    if n <= 1:
        return 1
    count = 0
    for i in range(1, n+1):
        print('index: ', i)
        # making 'i' root of the tree
        # left will have i - 1 nodes
        # right will have n - i nodes
        print('go to left: ', i - 1)
        countOfLeftSubtrees = count_trees(i - 1)
        print('left count: ', countOfLeftSubtrees)
        print('go to right: ', n - i)
        countOfRightSubtrees = count_trees(n - i)
        print('right count: ', countOfLeftSubtrees)
        count += (countOfLeftSubtrees * countOfRightSubtrees)
        print('count: ', count)
        print('\n')
    return count


def count_trees_2(n):
    return count_trees_rec({}, n)


def count_trees_rec(map, n):
    if n in map:
        return map[n]

    if n <= 1:
        return 1
    count = 0
    for i in range(1, n+1):
        # making 'i' the root of the tree
        countOfLeftSubtrees = count_trees_rec(map, i - 1)
        countOfRightSubtrees = count_trees_rec(map, n - i)
        count += (countOfLeftSubtrees * countOfRightSubtrees)

    map[n] = count
    return count


def main():
  # print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))
  # print("Total trees: " + str(count_trees_2(2)))
  # print("Total trees: " + str(count_trees_2(3)))

main()






