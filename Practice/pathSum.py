class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def PathSum(self, root, targetSum):
        def dfs(node, total):
            if not node:
                return
            total += node.val
            if not node.left and not node.right:
                return total == targetSum

            left = dfs(root.left, total)
            right = dfs(root.right, total)
            return left or right

        res = dfs(root, 0)
        return res
