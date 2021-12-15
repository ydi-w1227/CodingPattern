# Given a binary tree and a number ‘S’, find all paths in the tree
# such that the sum of all the node values of each path equals ‘S’.
# Please note that the paths can start or end at any node
# but all paths must follow direction from parent to child (top to bottom).


# add path from top to bottom
# every path calculate sum of all subpaths from bottom to top..
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])

def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        print('currentNode is None')
        return 0

    currentPath.append(currentNode.val)
    print('current node: ', currentNode.val)
    print('currentPath: ', currentPath)
    pathCount, pathSum = 0, 0

    # calculate pathSum by reverse adding from currentPath.. once a time
    # range(5, -1, -1) -> [5,4,3,2,1,0]... we only need from (length - 1) to 0
    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]
        if pathSum == S:
            pathCount += 1

    print('pathcount: ', pathCount)
    print('go to left')
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    print('out left: ', pathCount)
    print('go to right')
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)
    print('out left: ', pathCount)

    # backtrack
    del currentPath[-1]

    return pathCount

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 6)))


main()
