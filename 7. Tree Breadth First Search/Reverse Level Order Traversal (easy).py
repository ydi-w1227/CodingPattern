# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
# i.e., the lowest level comes first.
# You should populate the values of all nodes in each level from left to right
# in separate sub-arrays.arrays


from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        # print('__repr')
        return 'Node(' + str(self.val) + ')'

    def __str__(self):
        # print('__str__')
        return str(self.val)

def traverse(root):
    result = deque()

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []

        # append currentLevel node
        for _ in range(levelSize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode)
            # add its children to the queue if exist
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # append result from left
        result.appendleft(currentLevel)

    # print([str(y) for x in result for y in x])
    # print([print(y) for x in result for y in x])
    # print([repr(x) for x in result])
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
