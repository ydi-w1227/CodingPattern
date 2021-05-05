# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level
# from left to right in separate sub-arrays.
# https://blog.csdn.net/dangzhangjing97/article/details/78928411

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    # initialize
    queue = deque()
    queue.append(root)

    while queue:
        # length of current queue
        # shows how many nodes in current level
        levelSize = len(queue)
        currentLevel = []

        # start pop up node from queue
        # iteration 'current size of queue' times.. to traverse all node in current level
        # everytime pop up one node, add its children to the queue
        # queue maximum has N/2 nodes at lowest level
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # add all node in current level in result.
        result.append(currentLevel)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
