# Given a binary tree, find the length of its diameter.
# The diameter of a tree is the number of nodes on the longest path
# between any two leaf nodes.
# The diameter of a tree may or may not pass through the root.
#
# Note: You can always assume that there are at least two leaf nodes
# in the given tree.


# traverse all the nodes, for each node
#   1. get height of both left and right of currentNode
#       here, take currentNode as root,
#       heights on both side need to be max of both side + 1
#   2. can get currentNode's diameter.. (leftHeight + rightHeight + 1)

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):
        if currentNode is None:
            return 0

        print('currentNode: ', currentNode.val)

        print('come to left')
        leftTreeHeight = self.calculate_height(currentNode.left)
        print('out from left: ', leftTreeHeight)
        print('come to right')
        rightTreeHeight = self.calculate_height(currentNode.right)
        print('out from right: ', rightTreeHeight)


        if leftTreeHeight is not None and rightTreeHeight is not None:
            # diameter of current node
            diameter = leftTreeHeight + rightTreeHeight + 1
            print('for current node ' + str(currentNode.val) + ', diameter is : ', diameter)
            # update the tree diameter
            self.treeDiameter = max(self.treeDiameter, diameter)
            print('record current max diameter: ', self.treeDiameter)

        print('--return max height for currentNode: ', max(leftTreeHeight, rightTreeHeight) + 1)
        # return max height of current node
        return max(leftTreeHeight, rightTreeHeight) + 1


def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  # root.left.left = None
  # root.right.left.left = TreeNode(7)
  # root.right.left.right = TreeNode(8)
  # root.right.right.left = TreeNode(9)
  # root.right.left.right.left = TreeNode(10)
  # root.right.right.left.left = TreeNode(11)
  # print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
