# Given a binary tree where each node can only have a digit (0-9) value,
# each root-to-leaf path will represent a number.
# Find the total sum of all the numbers represented by all paths.


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):

  path_sum = find_sum_of_path(root, 0)
  return path_sum

def find_sum_of_path(currentNode, path_sum):
    if currentNode is None:
        return 0

    print('currentNode: ', currentNode.val)
    path_sum = path_sum * 10 + currentNode.val
    print('current path sum: ', path_sum)

    # if current node is a leaf, return current path sum
    if currentNode.left is None and currentNode.right is None:
        return path_sum

    # traverse left and right sub tree
    temp = find_sum_of_path(currentNode.left, path_sum) + find_sum_of_path(currentNode.right, path_sum)
    print('temp is ', temp)
    return temp

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
