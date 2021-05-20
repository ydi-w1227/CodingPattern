# Given a binary tree and a number ‘S’, find if the tree has a path
# from root-to-leaf such that the sum of all the node values
# of that path equals ‘S’.
# https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    print('has_path(',root.val if root else 'None' ,', ', sum, ')')
    if root is None:
        return False

    # if the current node is a leaf
    # and its value is equal to the sum,
    # we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    # state = has_path(root.left, sum-root.val) or has_path(root.right, sum-root.val)
    # print(state)
    # return state
    return has_path(root.left, sum-root.val) or has_path(root.right, sum-root.val)

def hasPathSum(root, target):
    if not root:
        return False

    stk = [(root, root.val)]

    while stk:
        node, val = stk.pop(0)
        print('node:' , node.val, ', val', val)


        if val == target and not node.left and not node.right:
            return True
        else:
            if node.left:
                stk.append((node.left, val + node.left.val))
            if node.right:
                stk.append((node.right, val + node.right.val))

    return False

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(hasPathSum(root, 23)))
    # print("Tree has path: " + str(has_path(root, 16)))


main()
