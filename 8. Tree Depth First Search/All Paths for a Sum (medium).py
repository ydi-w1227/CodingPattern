# Given a binary tree and a number ‘S’,
# find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.
#https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    find_paths_recursive_2(root, sum, [], allPaths)
    # dfs(root, sum, [], allPaths)
    return allPaths

def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return

    print('currentNode: ', currentNode.val, ' current sum: ', sum)

    # add the current node to the path
    currentPath.append(currentNode.val)
    print('currentPath: ', currentPath)

    # if the current node is a leaf and
    # its value is equal to required_sum, save the current path
    if currentNode.left is None and currentNode.right is None and sum == currentNode.val:
        allPaths.append(list(currentPath))
        print('allpath is ', allPaths)
    else:
        # if current node is not leaf or current node is leaf but sum != currentNode.val
        # traverse the left sub-tree and right sub-tree
        print('traverse left subtree')
        find_paths_recursive(currentNode.left, sum-currentNode.val, currentPath, allPaths)
        print('traverse right subtree')
        find_paths_recursive(currentNode.right, sum-currentNode.val, currentPath, allPaths)

    # when found a path and append leaf node
    # or did not find the path so jump out from recursive func
    # will do this to remove current node..

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del currentPath[-1]

def find_paths_recursive_2(currentNode, sum, currentPath, allPaths):
    # in this case, currentPath will be different each recursion
    # so doesnt need to delete any node from currentpath list
    if currentNode is None:
        return

    print('currentNode: ', currentNode.val, ' current sum: ', sum)
    print('currentPath: ', currentPath)

    if currentNode.left is None and currentNode.right is None and sum == currentNode.val:
        currentPath.append(currentNode.val)

        allPaths.append(list(currentPath))
        print('allpath is ', allPaths)
    else:
        print('traverse left subtree')
        find_paths_recursive(currentNode.left, sum - currentNode.val, currentPath + [currentNode.val], allPaths)
        print('traverse right subtree')
        find_paths_recursive(currentNode.right, sum - currentNode.val, currentPath + [currentNode.val], allPaths)

def dfs(root, sum, ls, res):
    if root:
        print('current node val: ', root.val)
        print(ls)

        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            print('== root.val', ls)
            res.append(ls)
        dfs(root.left, sum-root.val, ls+[root.val], res)
        dfs(root.right, sum-root.val, ls+[root.val], res)
    else:
        print('currentNode is None')

def find_paths_2(root, sum):
    if not root:
        return []
    print('current node: ', root.val, ' sum: ', sum)
    if not root.left and not root.right and sum == root.val:
        print([[root.val]])
        return [[root.val]]
    tmp = find_paths_2(root.left, sum - root.val) + find_paths_2(root.right, sum - root.val)
    print('tmp is: ', tmp)
    rlt = [[root.val] + i for i in tmp]
    print('rlt is: ', rlt)
    return rlt


#Problem 1: Given a binary tree, return all root-to-leaf paths.
#Solution: We can follow a similar approach. We just need to remove the “check for the path sum.”

def find_all_paths(root):
    all_path = []
    find_all_path(root, [], all_path)
    print(all_path)
    return all_path

def find_all_path(currentNode, currentPath, all_path):
    if currentNode is None:
        return

    print('currentNode: ', currentNode.val, ' with path: ', currentPath)

    if currentNode.left is None and currentNode.right is None:
        currentPath.append(currentNode.val)
        all_path.append(list(currentPath))

    else:
        find_all_path(currentNode.left, currentPath + [currentNode.val], all_path)
        find_all_path(currentNode.right, currentPath + [currentNode.val], all_path)

#Given a binary tree, find the root-to-leaf path with the maximum sum.
#Solution: We need to find the path with the maximum sum.
# As we traverse all paths, we can keep track of the path with the maximum sum.
def find_path_max(root):
    find_max(root, [], 0)
    return max_value


max_value = 0
def find_max(currentNode, currentPath, current_sum):
    global max_value
    if currentNode is None:
        return


    current_sum += currentNode.val
    currentPath.append(currentNode.val)
    print('currentNode: ', currentNode.val, ' current sum: ', current_sum)
    print('currentPath: ', currentPath)

    if currentNode.left is None and currentNode.right is None:
        max_value = max(current_sum, max_value)
        print(max_value)
    else:
        find_max(currentNode.left, currentPath, current_sum)
        find_max(currentNode.right, currentPath, current_sum)

    del currentPath[-1]

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    # print("Tree paths with sum " + str(sum) +
    #     ": " + str(find_paths_2(root, sum)))
    # print("Tree all paths are: " + str(find_all_paths(root)))
    print("Tree all paths are: " + str(find_path_max(root)))

main()
