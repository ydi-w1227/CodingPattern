# Given a binary tree and a number sequence,
# find if the sequence is present as a root-to-leaf path in the given tree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return False
    return path_exists(root, sequence, 0)

def path_exists(currentNode, sequence, index):
    # edge case
    # when traverse the subtree of non-None node
    # and the height of the node is less than height of the whole tree,
    # maybe its subtree is None
    if currentNode is None:
        print('currentnode is None, return False')
        return False

    seqLen = len(sequence)

    print('current node is: ', currentNode.val)
    print('compare to: ', sequence[index])

    # if node value doesnt match
    # or node height is higher than #nodes in sequence..
    # e.g. search sequence for 3 nodes.. but tree has a subtree which contains more than 3 nodes
    if index >= seqLen or currentNode.val != sequence[index]:
        return False

    # if current node is leaf and already traverse the whole sequence and all values matched
    if currentNode.left is None and currentNode.right is None and index == seqLen - 1:
        return True

    # not traverse till the leaf yet, keep traverse sub-tree
    left = path_exists(currentNode.left, sequence, index + 1)
    print('left is ', left)
    right = path_exists(currentNode.right, sequence, index + 1)
    print('right is ', right)
    return left or right


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(7)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
