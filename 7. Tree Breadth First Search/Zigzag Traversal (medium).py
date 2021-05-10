# Given a binary tree, populate an array to represent its zigzag level order traversal.
# You should populate the values of all nodes of the first level from left to right,
# then right to left for the next level and keep alternating in the same manner
# for the following levels.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    leftToRight = True
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        levelNode = deque()

        for _ in range(levelSize):
            currentNode = queue.popleft()
            if leftToRight:
                levelNode.append(currentNode.val)
            else:
                levelNode.appendleft(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(levelNode))
        leftToRight = not leftToRight
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()

