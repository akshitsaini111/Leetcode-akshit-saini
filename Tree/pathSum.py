class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root, targetSum):
        def dfs(node, total):
            if not node:
                return
            total += node.val
            if not node.left and not node.right:
                return total == targetSum
            l = dfs(node.left, total)
            r = dfs(node.right, total)
            return l or r

        res = dfs(root, 0)
        return res
